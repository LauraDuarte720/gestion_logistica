from productos.transporte import Transporte


class Barco(Transporte):
    def entrega(self) -> str:
        mensaje = "Entrega por mar en un contenedor."
        print(mensaje)
        return mensaje