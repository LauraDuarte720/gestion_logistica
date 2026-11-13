import sys

from creadores.logistica import Logistica
from creadores.logistica_aerea import LogisticaAerea
from creadores.logistica_maritima import LogisticaMaritima
from creadores.logistica_terrestre import LogisticaTerrestre

# Línea de configuración
LOGISTICAS: dict[str, type[Logistica]] = {"terrestre": LogisticaTerrestre, "maritima": LogisticaMaritima, "aerea": LogisticaAerea}

def main() -> None:
    tipo = sys.argv[1] if len(sys.argv) > 1 else "terrestre"
    logistica: Logistica = LOGISTICAS[tipo]()
    logistica.planificar_entrega()


if __name__ == "__main__":
    main()