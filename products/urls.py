from django.urls import path

from products.views import ProductsView

allowed_methods = {"get": "get", "post": "post", "delete": "delete", "patch": "update"}

urlpatterns = [
    path('/', ProductsView.as_view(allowed_methods)),
    # path('/customizations', CustomizationsView.as_view(allowed_methods)),
]
