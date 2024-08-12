from django.db import models 

# Create your models here.

class CategoriaProducto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #fecha de creación
    updated=models.DateTimeField(auto_now_add=True) # fecha de actualización
    
    class Meta:
        verbose_name='categoriaProducto'
        verbose_name_plural='categoriaProductos'
        
    def __str__(self): # metodo __str__ para que nos devuelva el nombre de la categorias
        return self.nombre
    
    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE) # deriva de la clase CategoriaProducto
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True) #fecha de creación
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        
        def __str__(self):
            return self.nombre
    