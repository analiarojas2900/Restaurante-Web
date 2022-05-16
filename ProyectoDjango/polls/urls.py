from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index' ),
    path('Contacto', views.Contacto, name='Contacto')
]