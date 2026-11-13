
import unittest
 
from productos.avion import Avion
from productos.barco import Barco
from productos.camion import Camion
from productos.transporte import Transporte
from creadores.logistica import Logistica
from creadores.logistica_aerea import LogisticaAerea
from creadores.logistica_maritima import LogisticaMaritima
from creadores.logistica_terrestre import LogisticaTerrestre
 
 
class TestFactoryMethod(unittest.TestCase):
    def test_cada_creador_devuelve_su_producto(self) -> None:
        self.assertIsInstance(LogisticaTerrestre().crear_transporte(), Camion)
        self.assertIsInstance(LogisticaMaritima().crear_transporte(), Barco)
        self.assertIsInstance(LogisticaAerea().crear_transporte(), Avion)
 
    def test_productos_cumplen_interfaz_transporte(self) -> None:
        for producto in (Camion(), Barco(), Avion()):
            self.assertIsInstance(producto, Transporte)
 
    def test_planificar_entrega_con_cualquier_creador(self) -> None:
        creadores: list[Logistica] = [
            LogisticaTerrestre(), LogisticaMaritima(), LogisticaAerea()
        ]
        for logistica in creadores:
            resultado = logistica.planificar_entrega()
            self.assertIn("Entrega", resultado)
 
    def test_maritima_reutiliza_la_misma_instancia(self) -> None:
        logistica = LogisticaMaritima()
        self.assertIs(logistica.crear_transporte(), logistica.crear_transporte())
 
    def test_transporte_no_se_puede_instanciar(self) -> None:
        with self.assertRaises(TypeError):
            Transporte()  # type: ignore[abstract]
 
 
if __name__ == "__main__":
    unittest.main()