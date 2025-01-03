from django.utils.timezone import now

from application.services.request_service_interface import RequestServiceInterface
from application.sessions.dto import SearcherDTO
from domain.user_sessions.repository import UserSessionRepositoryInterface


class SearcherService:
    def __init__(
        self, request_service: RequestServiceInterface, user_session_repository: UserSessionRepositoryInterface
    ):
        self.request_service = request_service
        self.user_session_repository = user_session_repository

    def get_initial_searcher(self) -> SearcherDTO:
        return SearcherDTO(
            ip=self.request_service.get_client_ip(),
            start_time=now().isoformat(),
            site=self.request_service.get_host(),
            headers=self.request_service.get_all_headers_to_string(),
        )

    def is_searcher(self) -> bool:
        searchers_db = self.user_session_repository.get_searchers()
        if searchers_db:
            searchers = [searcher.strip() for searcher in searchers_db.split(",")]
        else:
            searchers = []

        user_agent = self.request_service.get_all_headers()["HTTP_USER_AGENT"]

        for searcher in searchers:
            if searcher.lower() in user_agent:
                return True

        return False
