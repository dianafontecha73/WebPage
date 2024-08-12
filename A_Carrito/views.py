from django.shortcuts import render
from A_Carrito.carrito import Carro
from A_Tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.

def inicio(request):
    carro = Carro(request)
    productos = Producto.objects.all()  # modelo Producto
    return render(request, 'A_Web/inicio.html', {'carro': carro.carro, 'productos': productos})

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto) # .agregar es la función que se creó en el archivo carrito.py
    
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto) # .eliminar es la función que se creó en el archivo carrito.py
    
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto) # .restar_producto es la función que se creó en el archivo carrito.py
    
    return redirect("Tienda")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")

