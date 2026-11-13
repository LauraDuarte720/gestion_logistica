# Logística con Factory Method

Implementación del patrón Factory Method en Python (requiere Python 3.10+).

## Estructura
- `productos/`: `transporte.py` (producto), `camion.py` y `barco.py` (productos concretos), `avion.py` (extensión)
- `creadores/`: `logistica.py` (creadora), `logistica_terrestre.py` y `logistica_maritima.py` (creadores concretos), `logistica_aerea.py` (extensión)
- `cliente.py`: código cliente con la línea de configuración
- `alternativa_if.py`: versión sin el patrón, con `if/elif`
- `testFactoryMethod.py`: pruebas

## Ejecución
Desde la carpeta raíz del proyecto:
```bash
python3 cliente.py terrestre
python3 cliente.py maritima
python3 cliente.py aerea
python3 alternativa_if.py aerea
```

## Pruebas
```bash
python3 -m unittest -v
```