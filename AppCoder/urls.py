from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('contacto',contacto,name='Contacto')
 
]
