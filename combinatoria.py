

def factorial(n):
	resultado = 1
	for i in range(2, n+1):
		resultado *= i

	return resultado


def binary(m, A=None, C=None, M=None):
	"""
	Genera todas las cadenas posibles de m bits
	"""
	if M is None:
		M = m
	if A is None:
		A = []

	def process(C, A):
		A.append(C.copy())

	if C is None:
		C = [_ for _ in range(m)]

	if m == 0:
		process(C, A)
	else:
		C[m-1] = 0
		binary(m-1, A, C, M)
		C[m-1] = 1
		binary(m-1, A, C, M)

	return A


def permutaciones(lista):

	respuesta = []

	if not lista:
		return [[]]

	for a in lista:

		aux = lista.copy()  
		aux.remove(a) 

		permutaciones_a = permutaciones(aux) 
		
		for b in permutaciones_a: 
			b.append(a)

		respuesta.extend(permutaciones_a)

	return respuesta


def variaciones(lista, k, N=None):

	if N == None:
		N = len(lista)

	respuesta = []

	if N-len(lista) == k:
		return [[]]

	for a in lista:

		aux = lista.copy()  
		aux.remove(a) 

		variaciones_a = variaciones(aux, k, N) 
		
		for b in variaciones_a: 
			b.append(a)

		respuesta.extend(variaciones_a)

	return respuesta


from random import choice
def variaciones_metodo_aleatorio(lista, k):
	A = []
	n = len(lista)
	cardinal = factorial(n)/factorial(n-k)

	while len(A) != cardinal:
		C = []
		aux = lista.copy()
		for i in range(k):
			rand_item = choice(aux)
			C.append(rand_item)
			aux.remove(rand_item)
		if C not in A:
			A.append(C)

	return A


def combinaciones(conjunto):

	respuesta = [[]]

	for i in conjunto:  
		aux = respuesta.copy()
		for j in respuesta: 
			if not j:
				aux.append([i])
			else:
				aux_j = j.copy()
				aux_j.append(i)
				aux.append(aux_j)
		respuesta = aux 

	return respuesta


