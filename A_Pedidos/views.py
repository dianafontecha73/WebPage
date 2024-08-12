from django.shortcuts import redirect, render

# importaciones necesarias para realizar la función

from django.contrib.auth.decorators import login_required # para el decorador
from A_Carrito.carrito import Carro
from A_Pedidos.models import LineaPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url="/login/logear") # para que haya disponibilidad del carrito de compra, el usuario debe estar logueado
 
 # inicio del proceso de pedido
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user) # añadir los productos que desea el usuario
    carro=Carro(request) # ir añadiendo los productos en el carro de compra
    lineas_pedido=list() # meter todo lo que esté ahí almacenado en la BBDD
    
    # con el bucle se rescata la información que se va detectando del usuario: id del producto, cantidad, 
    for key, value in carro.carrito.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
         
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    # repasar documentación Django Sending mail
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.mail
    )
    
    messages.success(request, "El pedido se ha creado correctamente")
    
    return redirect("../A_Tienda/")

# se crea la función para renderizar el email en respuesta a la solicitud del pedido
# se utiliza las propiedades de la función arriba creada de enviar_mail

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs("lineas-pedido"),
        "nombreusuario":kwargs.get("nombreusuario")    
    })
    
    # se crea una variable para que reciba toda la información de la variable mensaje(línea 50) per que omita los caracteres que estén en las tags de html
    
    mensaje_texto=strip_tags(mensaje) # strip_tags es lo que omite las etiquetas de html que puedan irse en los mails
    from_email="emilianauribe51@gmail.com"
    to=kwargs.get("emailusuario") # recuperar el emailusuario de la función enviar_mail
    
    # se recorre cada dato a quien irá enviado el email, parámetros conforme Django.docs en Sending mail
    
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)