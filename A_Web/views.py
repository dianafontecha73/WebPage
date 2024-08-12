from django.shortcuts import render, HttpResponse
from A_Carrito.carrito import Carro
from A_Servicios.models import Servicio # importar del models de A_Servicios la class Servicio 


# Create your views here.

def home(request):
    
    carro=Carro(request)
    
    return render(request,"A_Web/home.html")