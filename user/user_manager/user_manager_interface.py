from typing import Protocol


class UserManagerInterface(Protocol):
    def get_user_by_email(self, email: str):
        raise NotImplementedError()

    def get_user_by_phone(self, phone: str):
        raise NotImplementedError()

    def create_user(self, username: str, phone: str, email: str, **extra_fields):
        raise NotImplementedError()

    def get_user_by_id(self, id: int):
        raise NotImplementedError()
