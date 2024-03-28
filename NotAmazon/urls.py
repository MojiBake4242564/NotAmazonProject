from django.urls import path

from . import views

# directory lists
urlpatterns = [
    path("home/", views.index, name="home"),
    path("registration/user_register", views.user_register, name="register"),
    path("registration/user_login", views.user_login, name="user_login"),
    path("products", views.products, name="products"), 
    path("shop", views.shop, name="shop"),
    #path("login/", views.user_login, name="login"),
]
