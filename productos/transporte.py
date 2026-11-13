from abc import ABC, abstractmethod
 
# Producto: interfaz común para todos los transportes
class Transporte(ABC):
    @abstractmethod
    def entrega(self) -> str:
        ...
 
 

 
 
    