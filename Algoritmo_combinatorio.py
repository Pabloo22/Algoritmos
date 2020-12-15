

def combinaciones(conjunto):

	output=[[]]

	for i in conjunto:  
		aux = output.copy()
		for j in output: 
			if not j:
				aux.append([i])
			else:
				aux_j = j.copy()
				aux_j.append(i)
				aux.append(aux_j)
		output = aux 

	return output

def fact(n):
	x = 1
	for i in range(1, n):
		x += i*x
	return x

def C(n, k):


	# conjunto = [i for i in range(n)]

	# comb = combinaciones(conjunto)
	# return [i for i in comb if len(i) == k]

	d = fact(n)
	D = fact(n-k)*fact(k)

	return d / D

print(len(combinaciones([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))



