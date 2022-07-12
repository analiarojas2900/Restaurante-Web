from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from CarritoApp.carrito import Carrito
from CarritoApp.models import Producto


def tienda(request):
    #return HttpResponse("Hola")
    productos = Producto.objects.all()
    return render(request, "tienda.html" , {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")

def pago(request):
    return render(request, "pago.html")