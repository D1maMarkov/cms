from datetime import datetime, timedelta

from django.conf import settings
from django.http import HttpRequest
from django.utils.timezone import now

from application.sessions.raw_session_service import get_raw_session_service
from infrastructure.logging.tasks import create_raw_logs
from infrastructure.logging.user_activity.create_json_logs import create_raw_log
from infrastructure.requests.service import get_request_service
from web.site_statistics.base_session_middleware import BaseSessionMiddleware


class RawSessionMiddleware(BaseSessionMiddleware):
    logs_array_length = 100
    logs = []
    cookie_name = settings.RAW_SESSION_COOKIE_NAME

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.searcher:
            return self.get_response(request)

        path = request.get_full_path()
        if "get-user-info" in path:
            return self.get_response(request)

        raw_session_service = get_raw_session_service(request_service=get_request_service(request))

        site = request.get_host()
        page_adress = site + path
        expires = datetime.utcnow() + timedelta(days=365 * 10)

        cookie = request.COOKIES.get(self.cookie_name)

        # cookie = None
        session_id = None

        if not cookie or ("/" not in cookie):
            session_data = raw_session_service.get_initial_raw_session(request.user_agent.is_mobile)
            session_db = self.raw_session_repository.create(**session_data.__dict__)
            session_id = session_db.id

            session_data = raw_session_service.check_headers(session_db)

            self.raw_session_repository.update(
                session_id,
                ban_rate=session_data.ban_rate,
            )
        else:
            session_id = int(cookie.split("/")[1])

        if not self.raw_session_repository.is_exists_by_id(session_id):
            session_data = raw_session_service.get_initial_raw_session(request.user_agent.is_mobile)
            session_db = self.raw_session_repository.create(**session_data.__dict__)
            session_id = session_db.id

            session_data = raw_session_service.check_headers(session_db)

            self.raw_session_repository.update(
                session_id,
                ban_rate=session_data.ban_rate,
            )

        session_data = self.raw_session_repository.get(session_id)

        reject_capcha_penalty = self.user_session_repository.get_reject_capcha_penalty()

        if session_data.show_capcha:
            if not self.url_parser.is_source(path) and "submit-capcha" not in path:
                session_data.ban_rate += reject_capcha_penalty
                self.penalty_logger(session_id, f"Отказ от капчи, {reject_capcha_penalty}, {path}")

        session_db = self.raw_session_repository.get(session_id)

        request.raw_session = session_db

        response = self.get_response(request)
        response.set_cookie(self.cookie_name, f"{session_id}/{session_id}", expires=expires)

        self.logs.append(create_raw_log(session_id, page_adress, path, time=now()))

        if len(self.logs) > self.logs_array_length:
            create_raw_logs.delay(self.logs)
            self.logs.clear()

        return response
