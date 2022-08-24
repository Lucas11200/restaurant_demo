import json
from typing import List

from products.serializers import ProductSerializer
from products.models import Product


class ProductsBuilder:
    @staticmethod
    def build(db_products: List[Product]) -> json:
        dict_products = ProductSerializer(db_products, many=True).data
        json_products = json.loads(json.dumps(dict_products))
        return json_products
