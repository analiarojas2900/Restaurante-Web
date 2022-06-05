from django.urls import path
from rest_comida.views import lista_comida, detalle_comida

urlpatterns = [
    path('lista_comida', lista_comida, name= "lista_comida"),
    path('detalle_comida/<id>', detalle_comida, name="detalle_comida"),
]