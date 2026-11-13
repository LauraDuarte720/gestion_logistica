from abc import ABC, abstractmethod

from productos.transporte import Transporte


# Creadora: no conoce ninguna clase concreta de transporte
class Logistica(ABC):
    @abstractmethod
    def crear_transporte(self) -> Transporte:
        """Método fábrica."""
        ...

    def planificar_entrega(self) -> str:
        """Lógica de negocio que usa el producto creado."""
        print(f"Planificando ruta con {type(self).__name__}...")
        transporte = self.crear_transporte()
        return transporte.entrega()




