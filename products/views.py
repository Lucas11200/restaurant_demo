from typing import List, Optional

from django.http import HttpResponse
from rest_framework.viewsets import ViewSet

from products.builders import ProductsBuilder
from products.factories import ProductsFactory
from products.models import Product, Customization
from products.services import ProductsService

products_service = ProductsService()
products_factory = ProductsFactory()
products_builder = ProductsBuilder()


class ProductsView(ViewSet):
    @staticmethod
    def get(request, sku_list: Optional[List[str]] = None):
        if sku_list and len(sku_list) > 0:
            db_products = products_factory.filter_products_by_sku(sku_list)
        else:
            body = request.data
            db_products = products_factory.filter_products_by_attributes(body)
        if db_products and len(db_products) > 0:
            response = products_builder.build(db_products)
            return HttpResponse(response)
        else:
            return HttpResponse("Not Found", 404)

    @staticmethod
    def delete(request):
        sku_list: List[str] = request.data
        db_products = products_service.filter_by_sku(sku_list)
        db_products.delete()
        return HttpResponse("ok")

    @staticmethod
    def update(request):
        # WIP TODO: finish this method (validations, error treatment)
        received_product = request.data
        product = Product.objects.get(sku=received_product.get("sku"))
        product.name = received_product.get("name")
        product.price = received_product.get("price")
        for customization in received_product.get("customizations"):
            db_customization = Customization.objects.get(sku=customization.get("sku"))
            db_customization.name = customization.get("name")
            db_customization.price = customization.get("price")
            db_customization.save()
        product.save()
        return HttpResponse("ok")

    @staticmethod
    def post(request):
        # WIP TODO: finish this method (validations, error treatment)
        received_products = request.data
        products = []
        for received_product in received_products:
            customizations = []
            for received_customization in received_product.get("customizations"):
                customizations.append(
                    Customization(
                        sku=received_customization.get("sku"),
                        name=received_customization.get("name"),
                        price=received_customization.get("price"),
                    )
                )

            cust = Customization.objects.bulk_create(customizations)

            product = Product(
                sku=received_product.get("sku"),
                name=received_product.get("name"),
                price=received_product.get("price")
            )
            product.save()
            for d in cust:
                product.customizations.add(d)
            products.append(product)

        return HttpResponse("ok")

# class CustomizationsView(ViewSet):
#     @staticmethod
#     def get(request, sku_list=None):
#         # WIP TODO: refactor this
#         if sku_list:
#             db_customizations = [Customization.objects.get(id=sku_list)]
#         else:
#             db_customizations = Customization.objects.all()
#         customizations = CustomizationSerializer(db_customizations, many=True).data
#         response = json.loads(json.dumps(customizations))
#         return HttpResponse(response)
#
#     @staticmethod
#     def post(request):
#         # WIP TODO: finish this method
#         received_customizations = request.data
#         customizations = [
#             Customization(
#                 sku=received_customizations.get("sku"),
#                 name=received_customizations.get("name"),
#                 price=received_customizations.get("price"),
#             ) for received_customizations in received_customizations
#         ]
#         Customization.objects.bulk_create(customizations)
#         return HttpResponse("ok")
