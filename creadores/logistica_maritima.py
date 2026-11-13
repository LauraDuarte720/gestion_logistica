from creadores.logistica import Logistica
from productos.transporte import Transporte
from productos.barco import Barco


class LogisticaMaritima(Logistica):
    """Actividad 3.6: reutiliza el mismo barco en lugar de crear uno nuevo."""

    def __init__(self) -> None:
        self._barco: Barco | None = None

    def crear_transporte(self) -> Transporte:
        if self._barco is None:
            self._barco = Barco()
        return self._barco