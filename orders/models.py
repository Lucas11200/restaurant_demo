from django.db import models

from products.models import Product
from restaurants.models import Restaurant


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
    total_value = models.FloatField(null=False, blank=False)
