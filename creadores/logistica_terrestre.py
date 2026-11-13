from creadores.logistica import Logistica
from productos.camion import Camion
from productos.transporte import Transporte

class LogisticaTerrestre(Logistica):
    def crear_transporte(self) -> Transporte:
        return Camion()
