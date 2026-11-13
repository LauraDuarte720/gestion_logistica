from productos.transporte import Transporte


class Avion(Transporte):
    """Actividad 3.5: Extensión."""
    def entrega(self) -> str:
        mensaje = "Entrega por aire en un avión de carga."
        print(mensaje)
        return mensaje