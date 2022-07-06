from django.urls import path

from restaurants.views import RestaurantsView

allowed_methods = {"get": "get", "post": "post"}

urlpatterns = [
    path('/', RestaurantsView.as_view(allowed_methods)),
    path('/<restaurant_id>', RestaurantsView.as_view(allowed_methods)),
]
