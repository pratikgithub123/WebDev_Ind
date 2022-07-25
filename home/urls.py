from django.contrib import admin
from django.urls import path
from .views import home, product, signup,signin,cart
from home import views

urlpatterns = [
    path("", views.home, name='home'),
    path("product", views.product, name='product'),
    path("signup", views.signup, name='signup'),
    path("signin", views.signin, name='signin'),
    path("cart", views.cart, name='cart'),
    

    
]
