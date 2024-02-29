from django.urls import path

from . import views

# directory list
urlpatterns = [
    path("home", views.index, name="index"),
    path("products", views.products, name="products"), 
    path("shop", views.shop, name="shop")
]
