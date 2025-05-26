import unittest
from solution import solucion

class TestSolucion(unittest.TestCase):
    def test_suma_numeros_positivos(self):
        self.assertEqual(solucion(3, 2), 5)
        self.assertEqual(solucion(7, 3), 10)
    
    def test_suma_numeros_negativos(self):
        self.assertEqual(solucion(-3, -6), -9)
    
    def test_suma_numeros_mixtos(self):
        self.assertEqual(solucion(-5, 8), 3)
        self.assertEqual(solucion(10, -4), 6)
    
    def test_suma_con_cero(self):
        self.assertEqual(solucion(0, 0), 0)
        self.assertEqual(solucion(5, 0), 5)
        self.assertEqual(solucion(0, -3), -3)

if __name__ == '__main__':
    unittest.main()
