

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


def C(n, k):

	conjunto = [i for i in range(n)]

	comb = combinaciones(conjunto)
	return [i for i in comb if len(i) == k]




