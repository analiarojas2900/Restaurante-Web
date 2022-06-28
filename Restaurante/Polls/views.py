from telnetlib import LOGOUT
from tokenize import group
from turtle import delay
from django import forms
from django.shortcuts import render,redirect
from Polls.models import Comida, Usuario
from Polls.forms import ComidaForm, UsuarioForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User, Group
from django.http import HttpRequest, HttpResponseRedirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_comida.viewsLogin import login as api_login
import json
import requests
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response as apiResponse
from rest_framework.views import APIView

def is_staff(user):
    return user.is_authenticated and user.Cliente

def index(request):
    return render(request,'Polls/index.html')

def Contacto(request):
    return render(request, 'Polls/Contacto.html')

def MenuNormal(request):
    return render(request, 'Polls/MenuNormal.html')

def MenuVegetariano(request):
    return render(request, 'Polls/MenuVegetariano.html')


def Reserva(request):
    return render(request, 'Polls/Reserva.html')



#def Form_Comida(request):
    #form=ComidaForm()
    #return render(request, 'polls/Form_Comida.html',{'form':form})


#def Modificar_Comida(request):
    #form=ComidaForm()
    #return render(request, 'polls/Modificar_Comida.html',{'form':form})
def Platos(request):
    listaComida =  Comida.objects.all() #select * from Comida
    datos = {
        'comida':listaComida
    }
    return render(request,"Polls/Platos.html", datos)

def Form_Comida(request):
    datos = {
        'form': ComidaForm()
    }

    if request.method == 'POST':
        formulario = ComidaForm(request.POST or None, request.FILES or None)

        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Se guardó el plato'
        else:
            datos['mensaje'] = 'NO se guardó el plato'
 
    return render(request,"Polls/Form_Comida.html", datos)

def Modificar_Comida(request, id):
    comida = Comida.objects.get(idPlato = id)

    datos = {
        'form': ComidaForm(instance = comida)
    }

    if request.method == 'POST':
        formulario = ComidaForm(request.POST or None, request.FILES or None, instance = comida)

        if formulario.is_valid():
            formulario.save() #modificar a la BD
            datos['mensaje'] = 'Se modificó el plato'
        else:
            datos['mensaje'] = 'NO se modificó el plato'

    return render(request,"Polls/Modificar_Comida.html", datos)

def Eliminar_Comida(request, id):
    comida = Comida.objects.get(idPlato = id)
    comida.delete() #delete de la BD
    return redirect(to='Platos')






def user_login(request):
    datos={
        'form':LoginForm()
    }
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            usernameU = request.POST['usuarioN']
            passwordU = request.POST['passwordN']
            user = authenticate(username=usernameU,password=passwordU)
            if user is not None:
                login(request,user)
                return render(request, "Polls/Recuperar.html")
    return render(request,"Polls/login.html",datos)
#recuperar contraseña
def Recuperar(request):
    return render(request,"Polls/Recuperar.html")

#se crea usuario nuevo y token
def Registrar(request): 
    datos={
        'form':UsuarioForm()
    }
    if(request.method == 'POST'):
        form=UsuarioForm(request.POST)
        if form.is_valid():
            #obtiene los datos del usuario desde formulario
            usernameN = form.cleaned_data.get('usuarioN')
            passwordN = form.cleaned_data.get('passwordN')
            passwordN2= form.cleaned_data.get('password2N')
            try:
                #se verifica existencia del usuario
                user = User.objects.get(username = usernameN)
            except User.DoesNotExist:
                #si no existe se genera un nuevo usuario validando si es que las pswrd son identicas
                if(passwordN == passwordN2):
                    user = User.objects.create_user(username=usernameN,email=usernameN,password=passwordN)
                    user = authenticate(username=usernameN, password=passwordN) #autentifican las credenciales del usuario
                    #se asigna un grupo al usuario nuevo (default comprador)
                    my_group = Group.objects.get(name='Comprador')
                    user.groups.add(my_group)
                    #se logea al usuario nuevo
                    login(request,user)
                    #comienzo de creacion de token
                    body= {"username": usernameN ,"password" : passwordN} #se genera json con info de usuario creado
                    r = requests.post('http://http://127.0.0.1:8000/api/login',data=json.dumps(body)) # se realiza la creacion de token
                    print(r.text) #se imprime token en forma  de debug
                    #fin creacion token
                    return render(request, "Polls/index.html")
    return render(request,"Polls/Registrar.html",datos)
