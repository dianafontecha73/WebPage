from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages # para usar los mensajes de error si el usuario no cumple con las normas de registro o contraseñas
# Create your views here.

class VRegistro(View): # View lo que se importa en línea 2
    
    # se crea la función get que es la que nos proporciona y muestra el formulario y lo renderiza
    def get(self, request):
        form=UserCreationForm()
        return render(request, "A_Login/registro.html", {"form":form}) # recordar que el 2do form de las llaves es el de la variable de la linea 11
    
    # se crea la función post encargada de enviar los datos a la BBDD
    def post(self, request):
        form=UserCreationForm(request.POST)
        
        # para confirmar que las contraseñs son válidas y están los caracteres aceptados por la validación Django se pne todo dentro de un if
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('Inicio')
        
        else:
           # se debe recorrer cada uno de los mensajes de error para saber cuál es que el usuario ha introducido y darle el responsive correcto 
            for mensaje in form.error_messages:
               messages.error(request, form.error_messages[mensaje]) # devolverá la variable mensaje en un string [mensaje]
               
            return render(request, "A_Login/registro.html", {"form":form})


def cerrar_sesion(request):
    logout(request)
    return redirect('Inicio')


def logear(request):
    # cuando el usuario presione el botón login se recibirá la autenticación
    
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None: # si no existe el usuario que se cree el usuario
                login(request, usuario)
                return redirect('Inicio')
            
            else:
                messages.error(request, "Usuario no válido")
                
        else:
           messages.error(request, "Información incorrecta") # tomado de Django.docs 
    
    form=AuthenticationForm()
    return render(request, "A_Login/login.html", {"form":form})
    