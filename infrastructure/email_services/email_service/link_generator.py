from application.email_services.user_email_service.link_generator_interface import (
    LinkGeneratorInterface,
)
from infrastructure.auth.jwt_processor import get_jwt_processor
from infrastructure.auth.jwt_processor_interface import JwtProcessorInterface
from infrastructure.persistence.repositories.domain_repository import (
    get_domain_repository,
)


class LinkGenerator(LinkGeneratorInterface):
    protocol = "https"

    def __init__(self, jwt_processor: JwtProcessorInterface, host: str) -> None:
        self.jwt_processor = jwt_processor
        self.host = host

    def get_url_to_confirm_email(self, user_id: int) -> str:
        token_to_confirm_email = self.jwt_processor.create_confirm_email_token(user_id)
        return f"{self.protocol}://{self.host}/user/confirm-email/{token_to_confirm_email}"

    def get_url_to_confirm_new_email(self, user_id: int) -> str:
        token_to_confirm_new_email = self.jwt_processor.create_confirm_email_token(user_id)
        return f"{self.protocol}://{self.host}/user/confirm-new-email/{token_to_confirm_new_email}"

    def get_url_to_reset_password(self, user_id: int) -> str:
        token_to_reset_password = self.jwt_processor.create_set_password_token(user_id)
        return f"{self.protocol}://{self.host}/user/password/{token_to_reset_password}"


def get_link_generator(
    jwt_processor: JwtProcessorInterface = get_jwt_processor(), host: str = get_domain_repository().get_domain_string()
) -> LinkGeneratorInterface:
    return LinkGenerator(jwt_processor, host)
