from django import forms
from django.shortcuts import render,redirect
from .models import Comida
from .forms import ComidaForm

# Create your views here.
def index(request):
    return render(request,'polls/index.html')

def Contacto(request):
    return render(request, 'polls/Contacto.html')

def InicioSeccion(request):
    return render(request, 'polls/InicioSeccion.html')

def MenuNormal(request):
    return render(request, 'polls/MenuNormal.html')

def MenuVegetariano(request):
    return render(request, 'polls/MenuVegetariano.html')

def Registrar(request):
    return render(request, 'polls/Registrar.html')

def Reserva(request):
    return render(request, 'polls/Reserva.html')

def Platos(request):
    return render(request, 'polls/Platos.html')

#def Form_Comida(request):
    #form=ComidaForm()
    #return render(request, 'polls/Form_Comida.html',{'form':form})


#def Modificar_Comida(request):
    #form=ComidaForm()
    #return render(request, 'polls/Modificar_Comida.html',{'form':form})

def home(request):
    listaComidas =  Comida.objects.all() #select * from Comida
    datos = {'comidas':listaComidas}
    return render(request,"polls/Platos.html", datos)

def Form_Comida(request):
    datos = {
        'form': ComidaForm()
    }

    if request.method == 'POST':
        formulario = ComidaForm(request.POST)

        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Se guardó el plato'
        else:
            datos['mensaje'] = 'NO se guardó el plato'
 
    return render(request,"polls/Form_Comida.html", datos)

def Modificar_Comida(request, id):
    Comida = Comida.objects.get(precio = id)

    datos = {
        'form': ComidaForm(instance = Comida)
    }

    if request.method == 'POST':
        formulario = ComidaForm(data = request.POST, instance = Comida)

        if formulario.is_valid():
            formulario.save() #modificar a la BD
            datos['mensaje'] = 'Se modificó el plato'
        else:
            datos['mensaje'] = 'NO se modificó el plato'

    return render(request,"polls/Modificar_Comida.html", datos)

def Eliminar_Comida(request, id):
    Comida = Comida.objects.get(precio = id)
    Comida.delete() #delete de la BD
    return redirect(to='home')