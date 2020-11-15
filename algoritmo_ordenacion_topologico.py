def AOT(grafo: dict, l_ordenada = []): # Algoritmo de ordenacion topológico
	
	if len(l_ordenada) == len(grafo):
		return l_ordenada

	for p in grafo:
		if p not in l_ordenada:
			if set(grafo[p]) & set(l_ordenada) == set(grafo[p]):
				l_ordenada.append(p)

	
	return AOT(grafo, l_ordenada)

# Ejemplo
grafo = {"P1": [], "P2": [], 
		"P3": ["P2"], "P4": ["P1", "P2"], "P5": ["P1"], 
		"P6": ["P7", "P4", "P3"], "P7": ["P5", "P4"], 
		"P8": ["P7"], "P9": ["P8", "P6"]}


print(AOT(grafo))