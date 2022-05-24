from django import forms
from django.forms import ModelForm
from .models import Comida

class ComidaForm(ModelForm):

    class Meta:
        model = Comida
        fields = ['precio','plato','tipo']