from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
import logging


# Create your views here.

logger = logging.getLogger(__name__)

def contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method == "POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        
    # cuando el usuario pulsa el botón enviar el método POST debe rescatar esa informacion a traves de esta condición --> 
    # y luego pasar la información de urls desde GET junto el parámetro que se quiera con el return redirect
 
        if formulario_contacto.is_valid():
            nombre=formulario_contacto.cleaned_data.get("nombre")
            apellido=formulario_contacto.cleaned_data.get("apellido")
            email_usuario=formulario_contacto.cleaned_data.get("email")
            mensaje=formulario_contacto.cleaned_data.get("mensaje")
            
            email=EmailMessage("Mensaje desde la App Django",f"El usuario con nombre {nombre} de apellido {apellido} con la dirección {email_usuario} te escribe lo siguiente:\n\n{mensaje}","",["emilianauribe51@gmail.com"],reply_to=[email_usuario],)
        
            try:
                email.send()
                return redirect("/contacto/?valido")
            except Exception as e:
                logger.error(f"Error al enviar el email: {e}")
                return redirect("/contacto/?novalido")
            
    return render(request,"A_Contacto/contacto.html", {'miFormulario': FormularioContacto})