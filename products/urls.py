from django.urls import path

from products.views import ProductsView
from restaurant_demo.settings import GET_PRODUCTS_API_NAME

allowed_methods = {"get": "get", "post": "post", "delete": "delete", "patch": "update"}

urlpatterns = [
    path('/', ProductsView.as_view(allowed_methods), name=GET_PRODUCTS_API_NAME),
    # path('/customizations', CustomizationsView.as_view(allowed_methods)),
]
