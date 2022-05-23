from django.shortcuts import render

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