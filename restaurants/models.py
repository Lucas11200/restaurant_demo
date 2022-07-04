from django.db import models


class Brand(models.Model):
    code = models.CharField(primary_key=True, blank=False, max_length=500)
    name = models.CharField(null=False, blank=False, max_length=500)


class Address(models.Model):
    cep = models.CharField(primary_key=True, blank=False, max_length=500)  # todo: create format validator
    street = models.CharField(null=False, blank=False, max_length=500)
    number = models.CharField(null=False, blank=False, max_length=500)
    neighborhood = models.CharField(null=False, blank=False, max_length=500)
    city = models.CharField(null=False, blank=False, max_length=500)
    state = models.CharField(null=False, blank=False, max_length=500)
    country = models.CharField(null=False, blank=False, max_length=500)


class Restaurant(models.Model):
    class Meta:
        unique_together = (('brand', 'address'),)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, name='brand')
    Address = models.ForeignKey(Address, on_delete=models.CASCADE, name='address')

