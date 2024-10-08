from typing import Any

from application.texts.errors import UserErrors
from domain.user.exceptions import UserDoesNotExist
from domain.user.repository import UserRepositoryInterface
from domain.user.validator import UserValidatorInterface
from infrastructure.auth.jwt_processor_interface import JwtProcessorInterface


class Login:
    def __init__(
        self,
        repository: UserRepositoryInterface,
        validator: UserValidatorInterface,
        jwt_processor: JwtProcessorInterface,
    ) -> None:
        self.repository = repository
        self.validator = validator
        self.jwt_processor = jwt_processor

    def __call__(self, fields: dict[str, Any]):
        phone_or_email = fields.get("phone_or_email")
        password = fields.get("password")

        if self.validator.is_valid_phone(phone_or_email):
            user = self.repository.get_user_by_phone(phone_or_email)
            if user is None:
                raise UserDoesNotExist(UserErrors.user_by_phone_not_found.value)

        elif self.validator.is_valid_email(phone_or_email):
            user = self.repository.get_user_by_email(phone_or_email)
            if user is None:
                raise UserDoesNotExist(UserErrors.user_by_email_not_found.value)

        else:
            raise UserDoesNotExist(UserErrors.incorrect_login.value)

        if not self.repository.verify_password(user.id, password):
            raise UserDoesNotExist(UserErrors.incorrect_password.value)

        access_token = self.jwt_processor.create_access_token(user.username, user.id)

        return access_token, user
