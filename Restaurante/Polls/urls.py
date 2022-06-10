from unicodedata import name
from django.urls import path
from . import views
from Polls.views import index
from Polls.views import Contacto
from Polls.views import MenuNormal
from Polls.views import MenuVegetariano
from Polls.views import Registrar
from Polls.views import Reserva
from Polls.views import Platos
from Polls.views import Form_Comida
from Polls.views import Modificar_Comida
from Polls.views import Eliminar_Comida
from Polls.views import InicioSeccion


urlpatterns = [
    path('', index, name='index'),
    path('Contacto', Contacto, name='Contacto'),
    path('MenuNormal', MenuNormal, name='MenuNormal'),
    path('MenuVegetariano', MenuVegetariano, name='MenuVegetariano'),
    path('Registrar', Registrar, name='Registrar'),
    path('Reserva', Reserva, name='Reserva'),
    path('Platos', Platos, name='Platos'),
    path('Form_Comida', Form_Comida, name='Form_Comida'),
    path('Modificar_Comida/<id>', Modificar_Comida, name='Modificar_Comida'),
    path('Eliminar_Comida/<id>', Eliminar_Comida, name='Eliminar_Comida'),
    path('InicioSeccion', InicioSeccion, name='InicioSeccion'),
]