from django.shortcuts import render

# Create your views here.   
def home(request):
    lista = ["Casuela","Chorrillana","Pollo_Papas_Nuggets","Paella"]
    cli = Cliente("1-9", "Juan","20")
    contexto ={"nombre":"Cristian","comida":lista,"Cliente":cli}
    return render(request,"productos")

class Cliente:
    def __init__(self, rut, nombre,edad):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        super().__init__()
        

def index(request):
    return render(request, 'html/index.html')
    
def Contacto(request):
    return render(request, 'html/Contacto.html')