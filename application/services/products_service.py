from typing import Any

from domain.products.repository import ProductRepositoryInterface
from domain.products.service import ProductsServiceInterface
from web.catalog.serializers import ProductsSerializer


class ProductsService(ProductsServiceInterface):
    def __init__(self, repository: ProductRepositoryInterface):
        self.repository = repository

    def get_enabled_products_to_create(self, user_id: int, organization_id: int) -> list[dict[str, Any]]:
        return ProductsSerializer(
            self.repository.get_enabled_products_to_create(user_id, organization_id), many=True
        ).data

    def filter_enabled_products(self, organization_id: int, user_id: int) -> list[dict[str, Any]]:
        products = self.repository.get_enabled_products_to_create(user_id, organization_id)

        return ProductsSerializer(products, many=True).data

    def filter_user_products(self, category_id: int, user_id: int):
        return self.repository.filter_user_products(category_id, user_id)

    def get_enabled_organizations(self, user_id: int) -> dict[str, Any]:
        return self.repository.get_enabled_organizations(user_id)


def get_products_service(repository: ProductRepositoryInterface) -> ProductsServiceInterface:
    return ProductsService(repository)
