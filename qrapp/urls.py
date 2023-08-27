from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
       path('', generate_qr_code, name='index'),
]
