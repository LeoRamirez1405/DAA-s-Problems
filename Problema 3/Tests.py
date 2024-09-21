import unittest
from setCoverBacktrack import set_cover
# from setCoverBacktrack import set_cover_greedy

class TestSetCover(unittest.TestCase):
    def __init__(self, methodName, set_cover_func):
        super().__init__(methodName)
        self.set_cover = set_cover_func

    # Caso de prueba básico donde existe una solución mínima
    def test_cobertura_minima(self):
        U = {1, 2, 3, 4, 5}
        S = [{1, 2}, {2, 3}, {4}, {1, 4, 5}]
        resultado = self.set_cover(U, S)
        self.assertEqual(resultado, ({2, 3},{1, 4, 5}))

    # Ejemplo adicional donde la solución mínima incluye subconjuntos superpuestos
    def test_cobertura_minima_superpuesta(self):
        U = {1, 2, 3, 4, 5, 6}
        S = [{1, 2, 3}, {4, 5}, {2, 4, 6}, {6}]
        resultado = self.set_cover(U, S)
        self.assertEqual(resultado, ({1, 2, 3}, {4, 5}, {2, 4, 6}))

    # Ejemplo con subconjuntos disjuntos
    def test_cobertura_minima_disjuntos(self):
        U = {1, 2, 3, 4, 5}
        S = [{1, 2}, {3}, {4, 5}]
        resultado = self.set_cover(U, S)
        self.assertEqual(resultado, ({1, 2}, {3}, {4, 5}))

    # Caso donde el conjunto universal tiene más elementos y la cobertura es óptima
    def test_cobertura_minima_grande(self):
        U = {1, 2, 3, 4, 5, 6, 7, 8}
        S = [{1, 2}, {2, 3, 4}, {4, 5}, {6, 7}, {5, 8}]
        resultado = self.set_cover(U, S)
        self.assertEqual(resultado, ({1, 2}, {2, 3, 4}, {6, 7}, {5, 8}))

    # Caso donde hay subconjuntos que cubren solo algunos elementos
    def test_cobertura_minima_elementos_individuales(self):
        U = {1, 2, 3, 4, 5}
        S = [{1}, {2}, {3}, {4}, {5}]
        resultado = self.set_cover(U, S)
        self.assertEqual(resultado, ({1}, {2}, {3}, {4}, {5}))

    # Caso con elementos redundantes
    def test_cobertura_minima_redundante(self):
        U = {1, 2, 3, 4, 5}
        S = [{1, 2}, {2, 3}, {1, 2, 3, 4, 5}, {4, 5}]
        resultado = self.set_cover(U, S)
        self.assertEqual(resultado, ({1, 2, 3, 4, 5},))

    # Caso donde solo un subconjunto cubre todo el conjunto U
    def test_cobertura_minima_unico_subconjunto(self):
        U = {1, 2, 3}
        S = [{1, 2, 3}, {1}, {2}, {3}]
        resultado = self.set_cover(U, S)
        self.assertEqual(resultado, ({1, 2, 3},))

    # Caso de prueba con subconjuntos que no cubren U completamente
    def test_cobertura_minima_incompleta(self):
        U = {1, 2, 3, 4}
        S = [{1, 2}, {3}]
        resultado = self.set_cover(U, S)
        self.assertIsNone(resultado)

# Función auxiliar para ejecutar tests con una función específica
def run_tests(set_cover_func):
    suite = unittest.TestSuite()
    suite.addTest(TestSetCover('test_cobertura_minima', set_cover_func))
    suite.addTest(TestSetCover('test_cobertura_minima_superpuesta', set_cover_func))
    suite.addTest(TestSetCover('test_cobertura_minima_disjuntos', set_cover_func))
    suite.addTest(TestSetCover('test_cobertura_minima_grande', set_cover_func))
    suite.addTest(TestSetCover('test_cobertura_minima_elementos_individuales', set_cover_func))
    suite.addTest(TestSetCover('test_cobertura_minima_redundante', set_cover_func))
    suite.addTest(TestSetCover('test_cobertura_minima_unico_subconjunto', set_cover_func))
    suite.addTest(TestSetCover('test_cobertura_minima_incompleta', set_cover_func))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':

    run_tests(set_cover)
