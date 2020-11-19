

def devuelve_vecinos_in(grafo_out: dict): 

	l_ordenada = [None for i in range(len(grafo_out))] 
	n = 0
	grafo_aux = grafo_out.copy()

	grafo_in = {i: set() for i in grafo_out}
	
	for i in grafo_out:
		for j in grafo_out[i]:
			grafo_in[j].add(i)

	return grafo_in


def ordenacion_topologica_1(grafo_out: dict): 
	# Este algoritmo es O(n^2)
	# Funciona a fuerza bruta. 

	l_ordenada = [] 
	n = 0  # Para el análisis de complejidad
	grafo = devuelve_vecinos_in(grafo_out)
	len_grafo = len(grafo)
	grafo_aux = grafo.copy()

	while len(l_ordenada) != len_grafo:

		# Debido a que si borramos elementos de la misma lista que está
		# siendo iterada daría error, necesitamos un grafo auxiliar:
		grafo_aux = grafo.copy()

		for p in grafo_aux:
			n += 1
			print(n)
			if set(grafo_aux[p]) & set(l_ordenada) == set(grafo_aux[p]):
				l_ordenada.append(p)
				del grafo[p]

	
	return l_ordenada


def ordenacion_topologica_2(grafo_out: dict): 
	# Es el algoritmo visto en clase y es 
	# más eficiente que el anterior. O(n + m)

	grafo_in = devuelve_vecinos_in(grafo_out) # Esta funcion es O(n + m)

	S = []
	l_ordenada = [] 
	n = 0  # Para el análisis de complejidad

	# Añadimos los minimales a S:
	for i in grafo_in:
		if not grafo_in[i]:
			S.append(i)

	while S:  # Mientras S no esté vacía

		# Añadimos los nodos 
		for v in S:
			l_ordenada.append(v)

			for w in grafo_out[v]:
				n += 1
				print(n)
				# Borramos las aristas
				grafo_in[w] = grafo_in[w] - set(l_ordenada)

				if not grafo_in[w] and w not in l_ordenada:
					S.append(w)

			S.remove(v)
					
	return l_ordenada


# Ejemplo
grafo_out = {1: {7, 3, 9}, 2: {4, 8}, 3: {6, 4},  4: {}, 5: {1}, 6: {}, 7: {}, 8: {}, 9: {2}}

# devueleve_vecinos_in(grafo_out) = {1: {5}, 2: {9}, 3: {1}, 4: {2, 3}, 5: set(), 6: {3}, 7: {1}, 8: {2}, 9: {1}}

# Peor caso del primer algoritmo:
grafo_out2 = {1: {}, 2: {1}, 3: {2}, 4: {3}, 5: {4}}
# grafo_in2 = {6: {5}, 5: {4}, 4: {3}, 3: {2}, 2: {1}, 1: set()}

print(ordenacion_topologica_1(grafo_out2))
print("------")
print(ordenacion_topologica_2(grafo_out2))

