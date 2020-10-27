from random import sample

lista = range(0, 100)
lista = sample(lista, 4)

def insertion_sort(lista):
	for j in range(1, len(lista)):
		key = lista[j]
		i = j - 1
		while i >= 0 and lista[i] > key:
			lista[i+1] = lista[i]
			i -= 1
		lista[i+1] = key
	return lista

print(insertion_sort(lista))
