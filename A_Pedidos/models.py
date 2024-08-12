from django.db import models
# a continuacin las que se van añadiendo
from django.contrib.auth import get_user_model
from A_Tienda.models import Producto
from django.db.models import Sum, F, FloatField

# Create your models here.

User=get_user_model()

class Pedido(models.Model):
    
# se almacen el usuario activo(user) y será clave foránea(ForeignKey) y en caso de eliminar al usuario que elimine tambien los registros realizados en cascada(User, on_delete=models.CASCADE)
   
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True) # donde se registra el momento exacto que se hace el pedido
    
    
    def __str__(self):
        return self.id # para que nos devuelva el id del pedido
    
    # se crea el decorador que nos dará como resultado el total de los productos pedidos junto con el total a pagar
    
    @property
    def total(self):
        return self.lineapedidos_set.aggregate(
            
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]
    
    class Meta:
        db_table='pedidos' # cómo se llamará la tabla
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']
        
# la clase que nos dará el control de la línea de pedido junto con  la hora en tiempo real de realizado el pedido
     
class LineaPedido(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1) # para que las cantidades por defecto aumenten de uno en uno
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    class Meta:
        db_table='lineapedidos' # cómo se llamará la tabla
        verbose_name='Línea Pedido'
        verbose_name_plural='Líneas Pedidos'
        ordering=['id']
        