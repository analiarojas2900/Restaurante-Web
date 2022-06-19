from dataclasses import fields
from django import forms
from django.forms import ModelForm
from Polls.models import Comida #, Categoria

class ComidaForm(ModelForm):
    class Meta:
        model = Comida
        fields = ['idPlato', 'precio', 'nombre','img', 'caracteristica', 'categoria']

'''
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreCategoria']

'''