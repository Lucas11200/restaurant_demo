from django.contrib.postgres.fields import ArrayField
from django.db import models


class Customization(models.Model):
    sku = models.CharField(primary_key=True, blank=False)
    name = models.CharField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, default=0.0)


class Product(models.Model):
    sku = models.CharField(primary_key=True, blank=False)
    name = models.CharField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, default=0.0)
    customizations = ArrayField(models.ForeignKey(Customization, on_delete=models.PROTECT))
