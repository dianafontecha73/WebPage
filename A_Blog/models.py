from django.db import models
from django.contrib.auth.models import User # para permitir otros usuarios 

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) # para que nos dé fecha y hora inmediatamente se hace el servicio
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria' # el nombre que se quiere que esté en la BBDD
        verbose_name_plural='categorias'
        
    def __str__(self):
        return self.nombre # la primera propiedad de clase Categoria
    
    
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True) # si el usuario quiere o no agregar imagen. Que no sea campo requerio u obligatorio
    autor=models.ForeignKey(User, on_delete=models.CASCADE) # para establecer la RELACIÓN entre el usuario y post
    categorias=models.ManyToManyField(Categoria) # la relación de varios a varios que habrá entre Categoria y Post
    created=models.DateTimeField(auto_now_add=True) # para que nos dé fecha y hora inmediatamente se hace el servicio
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='post' # el nombre que se quiere que esté en la BBDD
        verbose_name_plural='posts'
        
    def __str__(self):
        return self.titulo