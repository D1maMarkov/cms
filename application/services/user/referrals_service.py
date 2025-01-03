from collections.abc import Iterable

from domain.referrals.referral import ReferralInterface, UserInterface
from domain.referrals.repository import ReferralRepositoryInterface
from domain.referrals.service import ReferralServiceInterface
from domain.user.exceptions import UserDoesNotExist, UserIsNotReferral
from domain.user.validator import UserValidatorInterface
from infrastructure.persistence.repositories.referral_repository import (
    get_referral_repository,
)
from infrastructure.user.referrals_config import ReferralConfig, get_referral_config
from infrastructure.user.validator import get_user_validator


class ReferralService(ReferralServiceInterface):
    def __init__(
        self,
        validator: UserValidatorInterface,
        referral_repository: ReferralRepositoryInterface,
        referral_config: ReferralConfig,
    ) -> None:
        self.validator = validator
        self.referral_repository = referral_repository
        self.config = referral_config

    def get_referral_level(self, referral: ReferralInterface, user: UserInterface) -> int:
        sponsor = referral.sponsor
        for i in range(self.config.total_referral_level):
            if sponsor.id == user.id:
                return i + 1

            sponsor = sponsor.sponsor

        raise UserIsNotReferral(f"user '{user.full_name}' is not '{referral.full_name}'`s sponsor")

    def get_referral(self, user_id: int, user: UserInterface) -> ReferralInterface:
        referral = self.referral_repository.get(id=user_id)

        if not referral:
            raise UserDoesNotExist(f"no user with id '{user_id}'")

        referral.level = self.get_referral_level(referral, user)

        return referral

    def get_referrals(
        self, user_id: int, level: int | None = None, sorted_by: str = "created_at"
    ) -> Iterable[ReferralInterface]:
        if sorted_by:
            sorted_by = self.validator.validate_sorted_by(sorted_by)

        if level:
            level = self.validator.validate_referral_level(level)

        return self.referral_repository.filter(user_id, self.config.total_referral_level, level, sorted_by)


def get_referral_service(
    validator: UserValidatorInterface = get_user_validator(),
    repository: ReferralRepositoryInterface = get_referral_repository(),
    config: ReferralConfig = get_referral_config(),
) -> ReferralServiceInterface:
    return ReferralService(validator=validator, referral_repository=repository, referral_config=config)
