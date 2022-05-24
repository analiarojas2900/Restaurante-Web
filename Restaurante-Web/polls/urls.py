from unicodedata import name
from django.urls import path
from .views import index
from .views import Contacto
from .views import InicioSeccion
from .views import MenuNormal
from .views import MenuVegetariano
from .views import Registrar
from .views import Reserva
from .views import Form_Comida


urlpatterns = [
    path('index', index, name='index'),
    path('Contacto', Contacto, name='Contacto'),
    path('InicioSeccion', InicioSeccion, name='InicioSeccion'),
    path('MenuNormal', MenuNormal, name='MenuNormal'),
    path('MenuVegetariano', MenuVegetariano, name='MenuVegetariano'),
    path('Registrar', Registrar, name='Registrar'),
    path('Reserva', Reserva, name='Reserva'),
    path('Form_Comida', Form_Comida, name='Form_Comida'),
]