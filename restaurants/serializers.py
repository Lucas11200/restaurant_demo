from rest_framework.serializers import ModelSerializer

from restaurants.models import Address, Brand, Restaurant


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        exclude = []


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        exclude = []


class RestaurantSerializer(ModelSerializer):
    brand = BrandSerializer()
    address = AddressSerializer()

    class Meta:
        model = Restaurant
        exclude = []
