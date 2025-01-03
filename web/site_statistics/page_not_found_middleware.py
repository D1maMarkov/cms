from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer

from application.sessions.raw_session_service import RawSessionService
from infrastructure.admin.admin_settings import get_admin_settings
from infrastructure.requests.service import get_request_service
from web.site_statistics.base_session_middleware import BaseSessionMiddleware
from web.site_statistics.views import CapchaView


class PageNotFoundMiddleware(BaseSessionMiddleware):
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.searcher:
            return self.get_response(request)

        path = request.get_full_path()
        if "get-user-info" in path:
            return self.get_response(request)

        response = self.get_response(request)

        if response.status_code == 404 and not self.url_parser.is_source(request.path):
            raw_session = request.raw_session
            page_not_found_penalty = self.user_session_repository.get_session_filters().page_not_found_penalty
            request.raw_session = self.raw_session_repository.update(raw_session)
            self.penalty_logger(raw_session.id, f"Несуществующий адрес, {page_not_found_penalty}, {path}")

        request_service = get_request_service(request)
        raw_session_service = RawSessionService(
            request_service,
            self.user_session_repository,
            self.raw_session_repository,
            self.url_parser,
            self.penalty_logger,
            get_admin_settings(),
        )

        raw_session = request.raw_session

        site = request.get_host()
        host = site.split(":")[0]
        port = site.split(":")[1] if ":" in site else None

        ban_rate, hacking, show_capcha = raw_session_service.filter_sessions(
            raw_session,
            host,
            path,
            port,
            raw_session.id,
        )

        if ban_rate != raw_session.ban_rate or hacking != raw_session.hacking or show_capcha != raw_session.show_capcha:
            raw_session.ban_rate = ban_rate
            raw_session.hacking = hacking
            raw_session.show_capcha = show_capcha
            raw_session = self.raw_session_repository.update(
                session=raw_session, updated_fields=["ban_rate", "hacking", "show_capcha"]
            )

        if (
            raw_session.show_capcha
            and (not self.url_parser.is_source(path) and "submit-capcha" not in path)
            and not raw_session.hacking
        ):
            response = CapchaView.as_view()(request)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            try:
                response.render()
            except:
                pass

            raw_session = request.raw_session
            raw_session.show_capcha = True
            request.raw_session = self.raw_session_repository.update(raw_session)

            return response

        return response
