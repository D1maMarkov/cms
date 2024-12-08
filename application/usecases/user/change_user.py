from application.texts.errors import UserErrors
from domain.referrals.referral import UserInterface
from domain.user.exceptions import (
    UserWithEmailAlreadyExists,
    UserWithPhoneAlreadyExists,
)
from domain.user.repository import UserRepositoryInterface
from infrastructure.persistence.repositories.user_repository import get_user_repository


class ChangeUser:
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.repository = repository

    def __call__(
        self,
        user: UserInterface,
        phone: str,
        email: str,
        username: str,
        second_name: str,
        profile_picture: str,
        social_network: str = None,
        adress: str = None,
    ) -> bool:
        user_with_phone = self.repository.get_user_by_phone(phone)
        user_with_email = self.repository.get_user_by_email(email)

        if user_with_email != user and user_with_email and user_with_email.email_is_confirmed:
            raise UserWithEmailAlreadyExists(UserErrors.user_with_email_alredy_exists)

        elif user_with_phone != user and user_with_phone and user_with_phone.phone_is_confirmed:
            raise UserWithPhoneAlreadyExists(UserErrors.user_with_phone_alredy_exists)

        self.repository.update_user(
            id=user.id,
            username=username,
            second_name=second_name,
            phone=phone,
            profile_picture=profile_picture,
        )

        if social_network:
            self.repository.update_or_create_user_messanger(user_id=user.id, messanger_id=social_network, adress=adress)

        if user.email_is_confirmed and email != user.email:
            self.repository.change_user_email(user.id, email)

            return True

        self.repository.change_user_email(user.id, email)

        return False


def get_change_user_interactor(repository: UserRepositoryInterface = get_user_repository()) -> ChangeUser:
    return ChangeUser(repository)
