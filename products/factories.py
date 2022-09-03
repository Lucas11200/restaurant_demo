from typing import List, Optional

from products.models import Product
from products.services import ProductsService

products_service = ProductsService()


class ProductsFactory:
    @staticmethod
    def filter_products_by_sku(sku_list: Optional[List[str]] = None) -> List[Product]:
        if sku_list:
            db_products = [products_service.filter_by_sku(sku_list)]
        else:
            db_products = products_service.get_all()
        return db_products

    def filter_products_by_attributes(self, attributes):
        return products_service.filter_by_attributes(attributes)
