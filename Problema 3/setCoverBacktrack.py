from itertools import combinations

# Funciones del problema (cubre_U y set_cover)

def cubre_U(U, subconjuntos_seleccionados):
    union_subconjuntos = set()
    for subconjunto in subconjuntos_seleccionados:
        union_subconjuntos.update(subconjunto)
    return union_subconjuntos == U

def set_cover(U, S):
    n = len(S)
    mejor_cobertura = None
    
    for r in range(1, n + 1):
        for combinacion in combinations(S, r):
            if cubre_U(U, combinacion):
                if mejor_cobertura is None or len(combinacion) < len(mejor_cobertura):
                    mejor_cobertura = combinacion
        if mejor_cobertura is not None:
            break

    return mejor_cobertura

