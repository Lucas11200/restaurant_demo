from django.contrib import admin

from .models import Customization
from .models import Product

admin.site.register(Customization)
admin.site.register(Product)
