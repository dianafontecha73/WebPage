from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  # para las funciones que se actualizarán automáticamente en models y son de SOLO LECTURA

admin.site.register(Servicio, ServicioAdmin)