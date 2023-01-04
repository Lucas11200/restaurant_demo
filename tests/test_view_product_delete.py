from unittest.mock import MagicMock
from urllib.request import Request

from products.views import ProductsView
from products.factories import ProductsFactory
from products.services import ProductsService
import pytest

products_service = ProductsService()
products_factory = ProductsFactory()

class TestProductDelete():

    @pytest.mark.django_db
    def test_view_product(self):
        sku_list = ['777']
        product = products_factory.filter_products_by_sku(sku_list)
        if product:
            #missing 1 required positional argument: 'request'
            #O parâmetro em questão recebe um dicionário em request.data
            request = Request(data=sku_list, url=MagicMock())
            ProductsView.delete(request)

