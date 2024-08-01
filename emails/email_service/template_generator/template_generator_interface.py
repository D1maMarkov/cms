from typing import Any, Protocol

from user.user_interface import UserInterface


class EmailTemplateGeneratorInterface(Protocol):
    @staticmethod
    def generate_template(template_name: str, context: dict[Any, Any]) -> str:
        raise NotImplementedError()

    def generate_confirm_email_template(self, user: UserInterface) -> str:
        raise NotImplementedError()

    def generate_reset_password_template(self, user: UserInterface) -> str:
        raise NotImplementedError()
