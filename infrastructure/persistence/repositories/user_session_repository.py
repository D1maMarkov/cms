from datetime import datetime

from django.db.models import F
from django.utils.timezone import now

from domain.user_sessions.repository import UserSessionRepositoryInterface
from infrastructure.persistence.models.site_statistics import (
    SessionAction,
    SessionFilters,
    SessionModel,
    UserAction,
    UserActivity,
)


class UserSessionRepository(UserSessionRepositoryInterface):
    def create_user_action(self, adress: str, text: str, session_id: int, time: datetime = now()) -> None:
        UserAction.objects.create(
            adress=adress,
            text=text,
            time=time,
            session_id=session_id,
        )

    def create_session_action(
        self, adress: str, session_id: int, time: datetime, is_page: bool, is_source: bool
    ) -> None:
        SessionAction.objects.create(
            adress=adress,
            time=time,
            is_page=is_page,
            is_source=is_source,
            session_id=session_id,
        )

    def create_user_session(self, **kwargs) -> None:
        return UserActivity.objects.create(**kwargs)

    def get_session_filters(self):
        return SessionFilters.objects.first()

    def is_raw_session_exists_by_id(self, id: int) -> bool:
        return SessionModel.objects.filter(id=id).exists()

    def is_user_session_exists_by_id(self, id: int) -> bool:
        return UserActivity.objects.filter(id=id).exists()

    def create_raw_session(self, **kwargs):
        return SessionModel.objects.create(**kwargs)

    def update_raw_session(self, id, **kwargs):
        SessionModel.objects.filter(id=id).update(**kwargs)
        return SessionModel.objects.get(id=id)

    def update_user_session(self, id: int, **kwargs):
        UserActivity.objects.filter(id=id).update(**kwargs)

    def increment_user_session_field(self, id: int, field_name: str) -> None:
        UserActivity.objects.filter(id=id).update(**{field_name: F(field_name) + 1})

    def increment_raw_session_field(self, id: int, field_name: str) -> None:
        SessionModel.objects.filter(id=id).update(**{field_name: F(field_name) + 1})

    def bulk_create_raw_session_logs(self, logs):
        new_logs = [log for log in logs if log["session_id"] in SessionModel.objects.values_list("id", flat=True)]
        SessionAction.objects.bulk_create([SessionAction(**log) for log in new_logs])

    def bulk_create_user_session_logs(self, logs):
        new_logs = [log for log in logs if log["session_id"] in UserAction.objects.values_list("id", flat=True)]
        UserAction.objects.bulk_create([UserAction(**log) for log in new_logs])

    def get_raw_session(self, id: int):
        return SessionModel.objects.get(id=id)

    def delete_user_session(self, id):
        return SessionModel.objects.filter(id=id).delete()


def get_user_session_repository() -> UserSessionRepositoryInterface:
    return UserSessionRepository()
