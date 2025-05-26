import unittest
from solution import tartamudeo

class TestTartamudeo(unittest.TestCase):
    def test_patron_tartamudeo(self):
        palabras_prueba = ["sobresaliente", "hola", "python", "test", "a", ""]
        
        for palabra in palabras_prueba:
            resultado = tartamudeo(palabra)
            # Verifica que el resultado tenga el formato correcto
            if len(palabra) >= 2:
                prefijo = palabra[:2]
                self.assertTrue(resultado.startswith(f"{prefijo}... {prefijo}... "))
                self.assertTrue(resultado.endswith(f"{palabra}?"))
            else:
                # Para palabras de 0 o 1 carácter
                prefijo = palabra[:1] if palabra else ""
                self.assertTrue(resultado.startswith(f"{prefijo}... {prefijo}... "))
                self.assertTrue(resultado.endswith(f"{palabra}?"))
            
            # Verifica la longitud total del resultado
            longitud_esperada = len(prefijo) * 2 + 8 + len(palabra) + 1  # 8 para "... ... " y 1 para "?"
            self.assertEqual(len(resultado), longitud_esperada)

if __name__ == '__main__':
    unittest.main() 