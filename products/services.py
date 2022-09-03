from typing import List, Dict

from products.models import Product


class ProductsService:
    @staticmethod
    def filter_by_sku(sku_list: List[str]) -> List[Product]:
        return Product.objects.filter(pk__in=sku_list)

    @staticmethod
    def filter_by_attributes(attributes: Dict[str,any])-> List[Product]:
        return Product.objects.filter(**attributes)

    @staticmethod
    def get_all() -> List[Product]:
        return Product.objects.all()
