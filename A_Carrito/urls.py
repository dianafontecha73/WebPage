from django.urls import path
from . import views


# se usará la app_name para usos futuros de modo que despues con solo colocar app_name = 'A_Carrito' ys se obtenga todo lo que hay dentro
# evitando así la colisión entre las rutas que puedan tener el mismo nombre


app_name = 'A_Carrito'

urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),
]
