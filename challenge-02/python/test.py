import unittest
from solution import solucion

class TestSolucion(unittest.TestCase):
    def test_solucion(self):
        self.assertEqual(solucion(5), 6)  
        self.assertEqual(solucion(-1), 0)
        self.assertEqual(solucion(0), 1)
        self.assertEqual(solucion(99), 100)

if __name__ == '__main__':
    unittest.main()