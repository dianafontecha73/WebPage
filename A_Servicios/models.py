from django.db import models

# Create your models here. Para mapeo ORM

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='media/A_Servicios') # para que se busquen las imagenes en la carpeta media creada en la A_Servicios
    created=models.DateTimeField(auto_now_add=True) # para que nos dé fecha y hora inmediatamente se hace el servicio
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='servicio' # el nombre que se quiere que esté en la BBDD
        verbose_name_plural='servicios'
        
    def __str__(self):
        return self.titulo  # que nos devuelva el título de la clase Servicio

