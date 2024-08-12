from django.shortcuts import render
from A_Servicios.models import Servicio


# Create your views here.

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request, 'A_Servicios/servicios.html', {'servicios':servicios})
