# Actividad 3.8: versión SIN el patrón, con un if/elif en el cliente
import sys
 

from productos.avion import Avion
from productos.barco import Barco
from productos.camion import Camion
from productos.transporte import Transporte
 
 
def main() -> None:
    tipo = sys.argv[1] if len(sys.argv) > 1 else "terrestre"
 
    transporte: Transporte
    if tipo == "terrestre":
        transporte = Camion()
    elif tipo == "maritima":
        transporte = Barco()
    elif tipo == "aerea":  # cada transporte nuevo obliga a editar aquí
        transporte = Avion()
    else:
        print("Tipo no válido.")
        return
 
    print(f"Planificando ruta {tipo}...")
    transporte.entrega()
 
 
if __name__ == "__main__":
    main()