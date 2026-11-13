from productos.transporte import Transporte

class Camion(Transporte):

    def entrega(self) -> str:
        mensaje = "Entrega por tierra en una caja."
        print(mensaje)
        return mensaje