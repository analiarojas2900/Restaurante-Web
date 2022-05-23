from unicodedata import name
from django.urls import path
from .views import index
from .views import Contacto

urlpatterns = [
    path('index', index, name='index'),
    path('Contacto', Contacto, name='Contacto'),
]