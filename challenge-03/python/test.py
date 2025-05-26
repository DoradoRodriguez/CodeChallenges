import unittest
from solution import convertir

class TestConvertir(unittest.TestCase):
    def test_convertir_positivo(self):
        self.assertEqual(convertir(1), 60)
        self.assertEqual(convertir(2), 120)
        self.assertEqual(convertir(5), 300)

    def test_convertir_cero(self):
        self.assertEqual(convertir(0), 0)

    def test_convertir_negativo(self):
        self.assertEqual(convertir(-1), -60)
        self.assertEqual(convertir(-2), -120)

if __name__ == '__main__':
    unittest.main() 