from collections.abc import Iterable
from typing import Any, Protocol

from domain.products.product import (
    OfferInterface,
    ProductCategoryInterface,
    ProductInterface,
    ProductTypeInterface,
)


class ProductRepositoryInterface(Protocol):
    def get_enabled_products_to_create(self, user_id: int, organization_id: int) -> Iterable[ProductInterface]:
        raise NotImplementedError

    def get_enabled_organizations(self, user_id: int) -> dict[str, Any]:
        raise NotImplementedError

    def get_product_types_for_catalog(self, block_id: int) -> Iterable[ProductTypeInterface]:
        raise NotImplementedError

    def get_proudct_types_for_additional_catalog(self, block_id: int) -> Iterable[ProductTypeInterface]:
        raise NotImplementedError

    def get_offers(self) -> Iterable[OfferInterface]:
        raise NotImplementedError

    def get_product_offers(self, product_id: int) -> Iterable[OfferInterface]:
        raise NotImplementedError

    def get_product_type_name(self, slug: str) -> str:
        raise NotImplementedError

    def get_product_name_from_catalog(self, product_type_slug: str, product_index: int) -> str:
        raise NotImplementedError

    def get(self, id: int = None, user_product_id: int = None) -> ProductInterface:
        raise NotImplementedError

    def filter_enabled_products(self, organization_id: int, user_id: int) -> Iterable[ProductInterface]:
        raise NotImplementedError

    def get_catalog_offers(self, products_slug: str) -> Iterable[OfferInterface]:
        raise NotImplementedError

    def get_unprivate_catalog_offers(self, products_slug: str) -> Iterable[OfferInterface]:
        raise NotImplementedError

    def get_product_categories(self, user_id: int) -> Iterable[ProductCategoryInterface]:
        raise NotImplementedError

    def get_product_for_popup(self, product_id: int) -> ProductInterface:
        raise NotImplementedError

    def get_published_offers(self, product_type_id: int) -> Iterable[OfferInterface]:
        raise NotImplementedError
