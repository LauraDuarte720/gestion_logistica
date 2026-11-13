from creadores.logistica import Logistica
from productos.transporte import Transporte
from productos.avion import Avion


class LogisticaAerea(Logistica):
    """Actividad 3.5: Extensión."""
    def crear_transporte(self) -> Transporte:
        return Avion()