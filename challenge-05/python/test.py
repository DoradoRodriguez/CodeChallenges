import unittest
import random
from solution import descontar

class TestDescuento(unittest.TestCase):
    def test_descuento_aleatorio(self):
        for _ in range(10):  # Probamos 10 casos aleatorios
            precio = random.randint(1, 1000)
            descuento = random.randint(1, 100)
            resultado = descontar(precio, descuento)
            # Verificamos que el resultado sea un número entero
            self.assertIsInstance(resultado, int)
            # Verificamos que el resultado sea menor o igual al precio original
            self.assertLessEqual(resultado, precio)
            # Verificamos que el resultado sea mayor o igual a 0
            self.assertGreaterEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main() 