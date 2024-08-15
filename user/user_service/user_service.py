from django.db.models import Q

from account.serializers import ReferralSerializer
from domens.domain_service.domain_service import get_domain_service
from domens.domain_service.domain_service_interface import DomainServiceInterface
from user.models import User
from user.user_service.user_service_interface import UserServiceInterface
from user.validator.validator import get_user_validator
from user.validator.validator_interface import UserValidatorInterface


class UserService(UserServiceInterface):
    def __init__(self, domain_service: DomainServiceInterface, validator: UserValidatorInterface):
        self.validator = validator
        self.domain_service = domain_service

    def get_referrals_count(self, level, referral) -> int:
        count = 0
        for i in range(level):
            field = "sponsor__" * i + "sponsor_id"
            count += User.objects.filter(Q(**{field: referral.id})).count()

        return count

    def set_referrals(self, referrals) -> None:
        for referral in referrals:
            first_level_referrals = self.get_referrals_count(1, referral)
            referral.first_level_referrals = first_level_referrals

            all_referrals = (
                first_level_referrals + self.get_referrals_count(2, referral) + self.get_referrals_count(3, referral)
            )
            referral.referrals = f"{first_level_referrals}({all_referrals})"

    def sort_referrals(self, referrals, sorted_by):
        reverse = False

        if sorted_by[0] == "-":
            sorted_by = sorted_by[1::]
            reverse = True

        return sorted(referrals, key=lambda x: x.__getattribute__(sorted_by), reverse=reverse)

    def get_user_from_site(self, site, domain) -> User:
        if domain == self.domain_service.get_domain_model():
            return User.objects.filter(supersponsor=True).first()

        return site.user

    def get_referrals_from_users(self, users):
        referrals = []
        for user in users:
            user_referrals = User.objects.filter(sponsor_id=user.id)
            referrals.extend(list(user_referrals))

        return referrals

    def set_referral_level(self, referrals: list[User], level: int) -> list[User]:
        for referral in referrals:
            referral.level = level

        return referrals

    def get_referrals(self, user: User, level=None, sorted_by=None) -> list[User]:
        if level:
            level = self.validator.validate_referral_level(level)
        if sorted_by:
            sorted_by = self.validator.validate_sorted_by(sorted_by)

        sponsors = [user]

        if not level:
            all_referrals = []
            referrals = []
            for i in range(3):
                referrals = self.get_referrals_from_users(sponsors)
                sponsors = referrals
                self.set_referral_level(referrals, i + 1)
                self.set_referrals(referrals)

                all_referrals.extend(referrals)
            # all_referrals = []
            # all_referrals.append(User.objects.filter(sponsor_id=user.id))
            # all_referrals.append(User.objects.filter(sponsor__sponsor_id=user.id))
            # all_referrals.append(User.objects.filter(sponsor__sponsor__sponsor_id=user.id))
            # self.set_referral_level(all_referrals, 1)
            # self.set_referrals(all_referrals)

            if sorted_by:
                all_referrals = self.sort_referrals(all_referrals, sorted_by)

            return ReferralSerializer(all_referrals, many=True).data

        referrals = []
        for _ in range(level):
            referrals = self.get_referrals_from_users(sponsors)
            sponsors = referrals

        self.set_referral_level(referrals, level)
        self.set_referrals(referrals)

        if sorted_by:
            referrals = self.sort_referrals(referrals, sorted_by)

        return ReferralSerializer(referrals, many=True).data


def get_user_service() -> UserService:
    return UserService(get_domain_service(), get_user_validator())
