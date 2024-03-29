from unicodedata import name
from django.urls import path,include
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
from Polls.views import Recuperar
from Polls.views import user_login
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from CarritoApp.views import tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, pago

urlpatterns = [
    path('', user_login, name='index'),
    path('Contacto', Contacto, name='Contacto'),
    path('MenuNormal', MenuNormal, name='MenuNormal'),
    path('MenuVegetariano', MenuVegetariano, name='MenuVegetariano'),
    path('Registrar/', Registrar, name='Registrar'),
    path('Reserva', Reserva, name='Reserva'),
    path('Recuperar/', Recuperar, name='Recuperar'), 
    path('Platos', Platos, name='Platos'),
    path('Form_Comida', Form_Comida, name='Form_Comida'),
    path('Modificar_Comida/<id>', Modificar_Comida, name='Modificar_Comida'),
    path('Eliminar_Comida/<id>', Eliminar_Comida, name='Eliminar_Comida'),
    path('login/', user_login, name='login'),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="login")),
    path('logout', LogoutView.as_view()),
    path('desconectar/', views.desconectar, name= 'desconectar'),
    path('tienda/', tienda, name="tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('pago/', pago, name="pago"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)