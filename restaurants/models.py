from django.db import models


class Brand(models.Model):
    code = models.CharField(primary_key=True, blank=False)
    name = models.CharField(null=False, blank=False)


class Address(models.Model):
    cep = models.CharField(primary_key=True, blank=False)  # todo: create format validator
    street = models.CharField(null=False, blank=False)
    number = models.CharField(null=False, blank=False)
    neighborhood = models.CharField(null=False, blank=False)
    city = models.CharField(null=False, blank=False)
    state = models.CharField(null=False, blank=False)
    country = models.CharField(null=False, blank=False)


class Restaurant(models.Model):
    class Meta:
        unique_together = (('brand', 'address'),)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Address = models.ForeignKey(Address, on_delete=models.CASCADE)

