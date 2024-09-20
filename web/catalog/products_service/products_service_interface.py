from typing import Any, Protocol

from domain.user.referral import UserInterface


class ProductsServiceInterface(Protocol):
    def get_enabled_products_to_create(self, user_id: int) -> list[dict[str, Any]]:
        raise NotImplementedError()

    def filter_enabled_products(self, organization_id: int, user: UserInterface) -> list[dict[str, Any]]:
        raise NotImplementedError()

    def filter_user_products(self, category_id: int, user: UserInterface):
        raise NotImplementedError()

    def get_enabled_organizations(self, user_id: int) -> dict[str, Any]:
        raise NotImplementedError()
