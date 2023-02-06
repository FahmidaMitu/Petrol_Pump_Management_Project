from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', contact , name='contact'),
    path('bookingview', preview , name='preview'),
    path('book', book , name='book'),

]