from django import forms
from django.forms import ModelForm
from Polls.models import Comida #, Categoria

class ComidaForm(ModelForm):
    class Meta:
        model = Comida
        fields = ['idPlato', 'precio', 'nombre', 'caracteristica', 'categoria']

'''
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreCategoria']

'''