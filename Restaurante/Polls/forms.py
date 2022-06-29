from dataclasses import fields
from django import forms
from django.forms import ModelForm
from Polls.models import Comida, Usuario
from allauth.account.forms import LoginForm


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

class UsuarioForm(ModelForm):
    usuarioN = forms.CharField(widget=forms.EmailInput(attrs={'class':'login-username','placeholder':'Email'}),label='')
    passwordN = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Contraseña'}),label='')
    password2N = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Repetir Contraseña'}),label='')
    class Meta:
        model = Usuario
        fields= ['usuarioN','passwordN','password2N']

class LoginForm(ModelForm):
    usuarioN = forms.CharField(widget=forms.EmailInput(attrs={'class':'login-username','placeholder':'Email'}),label='')
    passwordN = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Contraseña'}),label='')
    class Meta:
        model=Usuario
        fields= ['usuarioN','passwordN']
