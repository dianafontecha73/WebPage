# archivo para crear la variable global que almacenará los precios de los productos
# que el usuario irá agregando al carro de compra

from A_Carrito.carrito import Carro

def importe_total_carro(request):
    total=0
    carro = request.session.get("carro", {})
    
    #if request.user.is_authenticated: # primero saber si el usuario está registrado
    
    for key, value in carro.items():
        total += float(value["precio"]) * value["cantidad"]
        
    return {"importe_total_carro":total} 