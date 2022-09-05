import ast
import unittest

import pytest
from django.urls import reverse

from rest_framework.test import APIClient

from django.conf import settings

from products.models import Product

api_client = APIClient()


def make_get_request(url_name, kwargs={}):
    url = reverse(url_name)
    return api_client.get(url, data=kwargs)


@pytest.mark.django_db
class TestView(unittest.TestCase):
    def test_get_all(self):
        payload = {'sku': '321', 'name': 'burg', 'price': 10.0}
        Product(**payload).save()
        response = make_get_request(settings.GET_PRODUCTS_API_NAME)
        raw_body = response.content
        str_body = raw_body.decode("UTF-8")
        body = ast.literal_eval(str_body)

        assert body is not None
        self.assertEqual(body, payload)

    # def test_get_by_sku(self):
    #     payload1 = {'sku': '321', 'name': 'burg', 'price': 10.0}
    #     payload2 = {'sku': '456', 'name': 'frita', 'price': 5.0}
    #     Product(**payload1).save()
    #     Product(**payload2).save()
    #     response = make_get_request(settings.GET_PRODUCTS_API_NAME, {"sku_list": ["321"]})
    #     breakpoint()
    #
    #     raw_body = response.content
    #     str_body = raw_body.decode("UTF-8")
    #     body = ast.literal_eval(str_body)
    #
    #     assert body is not None
    #     self.assertEqual(body, payload1)
