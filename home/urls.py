from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home , name="home"),
    path('cart/', cart , name="cart"),
    path('payment/', payment , name="payment"),
    path('api/gas/', api_gas)
]