import unittest
from src.main import sistema_valoracion

class TestSistemaValoracion(unittest.TestCase):
    def test_evaluacion(self):
        api_key = "fake_api_key"
        titulo_oferta = "Cajero supermercado Dia"
        cv = "Contenido del CV del candidato"
        resultado = sistema_valoracion(api_key, titulo_oferta, cv)
        self.assertIn("puntuacion", resultado)
        self.assertIn("experiencias_relacionadas", resultado)
        self.assertIn("descripcion", resultado)

if __name__ == "__main__":
    unittest.main()
