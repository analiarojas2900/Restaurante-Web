from django.shortcuts import render
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

def Form_Comida(request):
    return render(request, 'polls/Form_Comida.html')

def home(request):
    listaComida =  Comida.objects.all() #select * from Comida
    datos = {'comida':listaComida}
    return render(request,"polls/index.html", datos)

def agregar_comida(request):
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
 
    return render(request,"productos/Form_Comida.html", datos)



