from django.contrib import admin
from .models import CategoriaProducto, Producto

# Register your models here.

class CategoriaProductoAdmin(admin.ModelAdmin):
    
    readonly_fields=("created","updated") # así porque serán solo de lectura
   
class ProductoAdmin(admin.ModelAdmin):
     readonly_fields=("created","updated")
     
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)