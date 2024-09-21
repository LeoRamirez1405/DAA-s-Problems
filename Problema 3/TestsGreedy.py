import unittest
from setCoverGreedy import greedy_set_cover
class TestGreedySetCover(unittest.TestCase):
    
    # Caso básico con cobertura simple y costos diferentes
    def test_cobertura_minima_basica(self):
        U = {1, 2, 3, 4, 5}
        S = [{1, 2}, {2, 3}, {4}, {1, 4, 5}]
        costos = [4, 3, 2, 5]
        resultado = greedy_set_cover(U, S, costos)
        self.assertEqual(resultado, [{1, 2}, {1, 4, 5}])
        #AssertionError: Lists differ: [{2, 3}, {1, 4, 5}] != [{1, 2}, {1, 4, 5}]

    # Caso con subconjuntos superpuestos y costos diferentes
    def test_cobertura_minima_superpuesta(self):
        U = {1, 2, 3, 4, 5, 6}
        S = [{1, 2, 3}, {4, 5}, {2, 4, 6}, {6}]
        costos = [6, 5, 3, 2]
        resultado = greedy_set_cover(U, S, costos)
        self.assertEqual(resultado, [{1, 2, 3}, {2, 4, 6}])
        #AssertionError: Lists differ: [{2, 4, 6}, {1, 2, 3}, {4, 5}] != [{1, 2, 3}, {2, 4, 6}]
        
        
    # Caso con subconjuntos disjuntos y costos bajos
    def test_cobertura_minima_disjuntos(self):
        U = {1, 2, 3, 4, 5}
        S = [{1, 2}, {3}, {4, 5}]
        costos = [3, 2, 1]
        resultado = greedy_set_cover(U, S, costos)
        self.assertEqual(resultado, [{1, 2}, {3}, {4, 5}])
        #AssertionError: Lists differ: [{4, 5}, {1, 2}, {3}] != [{1, 2}, {3}, {4, 5}]

    # Caso donde la cobertura requiere subconjuntos con elementos redundantes
    def test_cobertura_minima_redundante(self):
        U = {1, 2, 3, 4, 5}
        S = [{1, 2}, {2, 3}, {1, 2, 3, 4, 5}, {4, 5}]
        costos = [4, 3, 6, 2]
        resultado = greedy_set_cover(U, S, costos)
        self.assertEqual(resultado, [{1, 2, 3, 4, 5}])
        #AssertionError: Lists differ: [{4, 5}, {2, 3}, {1, 2}] != [{1, 2, 3, 4, 5}]

    # Caso con todos los subconjuntos con un solo elemento
    def test_cobertura_minima_elementos_individuales(self):
        U = {1, 2, 3, 4, 5}
        S = [{1}, {2}, {3}, {4}, {5}]
        costos = [1, 1, 1, 1, 1]
        resultado = greedy_set_cover(U, S, costos)
        self.assertEqual(resultado, [{1}, {2}, {3}, {4}, {5}])

    # Caso donde no es posible cubrir todos los elementos
    def test_cobertura_minima_incompleta(self):
        U = {1, 2, 3, 4}
        S = [{1, 2}, {3}]
        costos = [4, 2]
        resultado = greedy_set_cover(U, S, costos)
        self.assertIsNone(resultado)

    # Caso con todos los elementos cubiertos por un solo subconjunto
    def test_cobertura_minima_un_solo_subconjunto(self):
        U = {1, 2, 3}
        S = [{1, 2, 3}, {1}, {2}, {3}]
        costos = [3, 2, 2, 2]
        resultado = greedy_set_cover(U, S, costos)
        self.assertEqual(resultado, [{1, 2, 3}])

    # Caso donde los subconjuntos tienen diferentes costos y se debe elegir el más económico
    def test_cobertura_minima_costo_vs_elementos(self):
        U = {1, 2, 3, 4, 5}
        S = [{1, 2}, {2, 3}, {3, 4, 5}]
        costos = [4, 5, 3]
        resultado = greedy_set_cover(U, S, costos)
        self.assertEqual(resultado, [{3, 4, 5}, {1, 2}])

# Ejecutar los tests
if __name__ == '__main__':
    unittest.main()
