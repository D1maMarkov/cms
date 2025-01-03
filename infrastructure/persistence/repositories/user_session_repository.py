from collections.abc import Iterable
from datetime import datetime

from django.core.cache import cache
from django.db.models import F
from django.utils.timezone import now

from domain.user_sessions.repository import UserSessionRepositoryInterface
from domain.user_sessions.session import UserSessionInterface
from domain.user_sessions.session_filters import SessionFIltersHeader
from infrastructure.persistence.models.site_statistics import (
    SessionFilters,
    UserAction,
    UserActivity,
    WebSearcher,
    WebSearcherAction,
)


class UserSessionRepository(UserSessionRepositoryInterface):
    def get(self, id: int) -> UserSessionInterface | None:
        try:
            return UserActivity.objects.get(id=id)
        except UserActivity.DoesNotExist:
            return None

    def create_user_action(self, adress: str, text: str, session_id: int, time: datetime | None = None) -> None:
        if time is None:
            time = now()

        UserAction.objects.create(
            adress=adress,
            text=text,
            time=time,
            session_id=session_id,
        )

    def get_session_filter_headers(self) -> Iterable[SessionFIltersHeader]:
        filters = SessionFilters.objects.first()
        if filters:
            return filters.headers.all()

        return []

    def create(self, **kwargs) -> UserSessionInterface:
        return UserActivity.objects.create(**kwargs)

    def get_session_filters(self):
        filters = cache.get("session_filters")
        if not filters:
            filters = SessionFilters.objects.first()
            cache.set("session_filters", filters, timeout=15 * 60)

        return filters

    def get_searchers(self) -> str:
        session_filters = SessionFilters.objects.values_list("searchers").first()
        return session_filters[0] if session_filters else ""

    def is_searcher_exists_by_id(self, id: int) -> bool:
        return WebSearcher.objects.filter(id=id).exists()

    def create_searcher_log(self, **kwargs) -> None:
        WebSearcherAction.objects.create(**kwargs)

    def create_searcher(self, **kwargs) -> int:
        searcher = WebSearcher.objects.create(**kwargs)
        return searcher.id

    def update(self, session: UserSessionInterface) -> UserSessionInterface:
        if hasattr(session, "save"):
            session.save()
        return session

    def increment_user_session_field(self, id: int, field_name: str) -> None:
        UserActivity.objects.filter(id=id).update(**{field_name: F(field_name) + 1})

    def bulk_create_user_session_logs(self, logs):
        new_logs = [log for log in logs if log["session_id"] in UserActivity.objects.values_list("id", flat=True)]
        UserAction.objects.bulk_create([UserAction(**log) for log in new_logs])

    def delete_user_session(self, id: int) -> None:
        return UserActivity.objects.get(id=id).delete()

    def get_disallowed_host_penalty(self):
        return SessionFilters.objects.values_list("disallowed_host", flat=True).first()

    def delete_hacking_visitors(self, ban_limit: int) -> None:
        UserActivity.objects.filter(session__ban_rate__gte=ban_limit).delete()


def get_user_session_repository() -> UserSessionRepositoryInterface:
    return UserSessionRepository()
