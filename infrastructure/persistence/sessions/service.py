from django.utils.timezone import now

from application.common.url_parser import UrlParserInterface
from application.services.request_service import RequestServiceInterface
from application.sessions.dto import RawSessionDB, RawSessionDTO
from application.sessions.raw_session_service import RawSessionServiceInterface
from domain.user_sessions.repository import UserSessionRepositoryInterface


class RawSessionService(RawSessionServiceInterface):
    def __init__(
        self,
        request_service: RequestServiceInterface,
        user_session_repository: UserSessionRepositoryInterface,
        url_parser: UrlParserInterface,
    ):
        self.request_service = request_service
        self.user_session_repository = user_session_repository
        self.url_parser = url_parser

    def get_initial_raw_session(self, path, site, device):
        headers = self.request_service.get_all_headers_to_string()
        ip = self.request_service.get_client_ip()
        host = site.split(":")[0]
        port = site.split(":")[1] if ":" in site else None

        session_data = RawSessionDB(
            ip=ip,
            start_time=now().isoformat(),
            end_time=now().isoformat(),
            site=site,
            device=device,
            headers=headers,
        )

        # session_data = self.filter_sessions(session_data, host, path, port)

        return session_data

    def filter_sessions(self, session_data: RawSessionDTO, host: str, path: str, port: str) -> RawSessionDTO:
        session_filters = self.user_session_repository.get_session_filters()

        if session_filters:
            if host != "127.0.0.1" and host != "localhost":
                if self.url_parser.is_ip(host):
                    session_data.ban_rate += session_filters.ip_penalty

                if port:
                    session_data.ban_rate += session_filters.ports_penalty

            for disable_url in session_filters.disable_urls.splitlines():
                if disable_url in path:
                    print(disable_url, "disable_url")
                    session_data.ban_rate += session_filters.disable_urls_penalty
                    break

            if session_data.ban_rate >= session_filters.ban_limit:
                session_data.hacking = True

            if session_data.ban_rate >= session_filters.capcha_limit:
                session_data.show_capcha = True

        return session_data

    def success_capcha(self, session_id: int):
        increase_value = -self.user_session_repository.get_success_capcha_increase()
        self.user_session_repository.change_ban_rate(session_id, increase_value)


def get_raw_session_service(
    request_service: RequestServiceInterface,
    user_session_repository: UserSessionRepositoryInterface,
    url_parser: UrlParserInterface,
) -> RawSessionServiceInterface:
    return RawSessionService(
        request_service=request_service, user_session_repository=user_session_repository, url_parser=url_parser
    )
