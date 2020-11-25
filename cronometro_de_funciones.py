from time import time
# import sys
# sys.setrecursionlimit(10000)

def cronometra(funcion):

	def print_tiempo(*args, rep = 1_000_000):

		t0 = time()
		for i in range(rep):
			output = funcion(*args)
		t = time()
		tiempo_total = t - t0
		print(f"tiempo de {funcion.__name__}: {tiempo_total}")
		return output

	return print_tiempo

"""
Nota: si la función es recursiva necesitaremos una copia de ella en la propia
función puesto que si no cuando se llame así misma estaría llamándose con el decorador.
"""
# Ejemplo:
@cronometra
def multiply(y, z):

	def multiply_copy(y, z):
		if z == 0:
			return 0
		elif z%2 != 0:
			return multiply_copy(2*y, z//2) + y
		else:
			return multiply_copy(2*y, z//2)

	if z == 0:
		return 0
	elif z%2 != 0:
		return multiply_copy(2*y, z//2) + y
	else:
		return multiply_copy(2*y, z//2)

@cronometra
def multiply2(y, z): return y*z

# No se requiere de print()
multiply(5, 5)
multiply2(5, 5)

