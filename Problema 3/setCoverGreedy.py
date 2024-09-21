def greedy_set_cover(U, S, costos):
    # Inicialmente, todos los elementos de U están descubiertos
    descubiertos = set(U)
    cobertura = []
    
    while descubiertos:
        mejor_subconjunto = None
        mejor_costo_por_elemento = float('inf')
        
        # Iterar sobre los subconjuntos que aún no han sido seleccionados
        for i, subconjunto in enumerate(S):
            # Calcular los elementos descubiertos cubiertos por el subconjunto actual
            elementos_cubiertos = descubiertos.intersection(subconjunto)
            
            if elementos_cubiertos:
                # Calcular el costo por elemento cubierto
                costo_por_elemento = costos[i] / len(elementos_cubiertos)
                
                # Elegir el subconjunto que minimiza el costo por elemento cubierto
                if costo_por_elemento < mejor_costo_por_elemento:
                    mejor_costo_por_elemento = costo_por_elemento
                    mejor_subconjunto = i
        
        # Añadir el subconjunto elegido a la cobertura
        if mejor_subconjunto is not None:
            cobertura.append(S[mejor_subconjunto])
            # Actualizar los elementos descubiertos
            descubiertos -= S[mejor_subconjunto]
        else:
            break
    
    # Devolver la cobertura si todos los elementos fueron cubiertos
    if not descubiertos:
        return cobertura
    else:
        return None
