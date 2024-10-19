from typing import Any, Protocol


class WorkEmailTemplateGeneratorInterface(Protocol):
    @staticmethod
    def generate_template(template_name: str, context: dict[Any, Any]) -> str:
        raise NotImplementedError()

    def generate_success_login_in_admin_template(self, **kwargs) -> str:
        raise NotImplementedError()

    def generate_cant_login_in_admin_template(self, **kwargs) -> str:
        raise NotImplementedError()

    def generate_login_in_fake_admin(self, **kwargs) -> str:
        raise NotImplementedError()