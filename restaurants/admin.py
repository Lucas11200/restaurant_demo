from django.contrib import admin

from .models import Brand
from .models import Address
from .models import Restaurant

admin.site.register(Brand)
admin.site.register(Address)
admin.site.register(Restaurant)
