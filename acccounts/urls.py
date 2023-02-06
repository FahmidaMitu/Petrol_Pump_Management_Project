from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', acc, name="acc_view"),
    path('login', login, name="login"), 
    path('register', register, name="register"),
    path('logout', logout, name='logout'),
]