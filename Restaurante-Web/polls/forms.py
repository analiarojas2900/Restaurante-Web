from django import forms
from django.forms import ModelForm
from .models import Comida #, Categoria

class ComidaForm(ModelForm):
    class Meta:
        model = Comida
        fields = ['precio','plato','tipo','categoria']

'''
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreCategoria']

'''