from nturl2path import url2pathname
from django.urls import path
from .import views

urlpatterns=[
    path('home',views.customer_home),
    path('cart',views.display_cart)
]