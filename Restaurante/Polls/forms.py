from dataclasses import fields
from django import forms
from django.forms import ModelForm
from Polls.models import Comida, Usuarios
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

class UsuariosForm(ModelForm):
    #se da formato a cada uno de los campos dentro de la forma
    usrN = forms.CharField(widget=forms.EmailInput(attrs={'class':'login-username','placeholder':'Email'}),label='')
    pswrdN = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Contraseña'}),label='')
    pswrdN2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Repetir Contraseña'}),label='')
    class Meta:
        #se asigna modelo y orden de aparicion en html
        model = Usuarios
        fields= ['usrN','pswrdN','pswrdN2']

class LoginForm(ModelForm):
    usrN = forms.CharField(widget=forms.TextInput(attrs={'class':'login-username','placeholder':'Username'}),label='')
    pswrdN = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Contraseña'}),label='')
    class Meta:
        model=Usuarios
        fields= ['usrN','pswrdN']
