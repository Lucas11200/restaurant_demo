from django.db import models


class Customization(models.Model):
    sku = models.CharField(primary_key=True, blank=False, max_length=500)
    name = models.CharField(null=False, blank=False, max_length=500)
    price = models.FloatField(null=False, blank=False, default=0.0)


class Product(models.Model):
    sku = models.CharField(primary_key=True, blank=False, max_length=500)
    name = models.CharField(null=False, blank=False, max_length=500)
    price = models.FloatField(null=False, blank=False, default=0.0)
    customizations = models.ManyToManyField(Customization)

