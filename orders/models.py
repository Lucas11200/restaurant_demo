from django.contrib.postgres.fields import ArrayField
from django.db import models

from products.models import Product
from restaurants.models import Restaurant


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    products = ArrayField(models.ForeignKey(Product, on_delete=models.PROTECT))
    total_value = models.FloatField(null=False, blank=False)
