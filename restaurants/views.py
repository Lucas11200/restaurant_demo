import json

from django.http import HttpResponse
from rest_framework.viewsets import ViewSet

from restaurants.models import Restaurant, Brand, Address
from restaurants import serializers


class RestaurantsView(ViewSet):
    @staticmethod
    def get(request, restaurant_id=None):
        # WIP TODO: refactor this
        if restaurant_id:
            db_restaurants = [Restaurant.objects.get(id=restaurant_id)]
        else:
            db_restaurants = Restaurant.objects.all()
        restaurants = serializers.RestaurantSerializer(db_restaurants, many=True).data
        response = json.loads(json.dumps(restaurants))
        return HttpResponse(response)

    @staticmethod
    def post(request):
        # WIP TODO: finish this method
        body = request.data

        received_brand = body.get("brand", {})
        received_address = body.get("address", {})

        brand = Brand(
            code=received_brand.get("code", {}),
            name=received_brand.get("name", {}),
        )
        brand.save()

        address = Address(
            cep=received_address.get("cep"),
            street=received_address.get("street"),
            number=received_address.get("number"),
            neighborhood=received_address.get("neighborhood"),
            city=received_address.get("city"),
            state=received_address.get("state"),
            country=received_address.get("country"),
        )
        address.save()
        restaurant = Restaurant(brand_id=brand.id, address_id=address.id).save()
        return HttpResponse(restaurant)
