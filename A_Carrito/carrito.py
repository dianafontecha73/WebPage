# el constructor de la class Carro

class Carro:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro") 
    
    # si no se ha iniciado sesion y aùn no hay carro se debe crear
    
        if not carro:
            self.carro=self.session["carro"]={} # iniciar sesion y el carro está vacío
        else:
            self.carro=carro # si ya el usuario está registrado y  entra a comprar
            
    # cuando el usuario  ha agregado un producto por primera vez
    
    def agregar(self, producto):
        if (str(producto.id) not in self.carro.keys()) :
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url                
            }
    
    # para que el usuario pueda seguir agregando productos
    
        else:
            
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio 
                    break
        self.guardar_carro()
        
        
    # guardar el numero de productos seleccionados por el usuario
    
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
        
    # para eliminar productos del carro
    
    def eliminar(self, producto): 
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
            
    # restar unidades de un producto pero no eliminarlo
     
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"])-producto.precio
                
            # en el caso que al eliminar unidades quede en 0, eliminar el producto
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()
        
    # para vaciar o limpiar carro
    
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
        