
def counting_sort(A, rango):
	print("A =", A)
	C = []
	B = [None for i in range(len(A))]

	for i in range(rango):
		C.append(0)
	# print("C =", C)

	for j in range(len(A)):
		C[A[j]] += 1 
	# print("C =", C) 

	for i in range(1, rango):
		C[i] += C[i - 1] 
	print("C =", C)

	for j in range(len(A)):
		B[C[A[j]] - 1] = A[j]
		C[A[j]] -= 1
		print("B =", B)
		# print("C =", C)

	return B

lista = [2, 5, 3, 0, 2, 3, 0, 3]
rango = 6
mayor = 5
counting_sort(lista, rango)