#  devuelve una terna (d, x, y) de manera que d = mcd(a, b) y que d = a · x + b · y 
def Euclides_ext (a, b):

	if b == 0:
		return (a, 1, 0)
	else:
		salida = Euclides_ext(b, a%b)
		d = salida[0]
		x = salida[1]
		y = x*(a/b)*salida[2]
	return (d, x, y)

print(Euclides_ext(18, 10))

def eucExt(a,b):
	r = [a,b]
	s = [1,0] 
	t = [0,1]
	i = 1 
	q = [[]]
	while (r[i] != 0): 
		q = q + [r[i-1] // r[i]]  # parte entera de b/a
		r = r + [r[i-1] % r[i]]  # resto de b/a
		s = s + [s[i-1] - q[i]*s[i]]  # 1, 0 - b//a
		t = t + [t[i-1] - q[i]*t[i]]
		i = i+1
	return (r[i-1], s[i-1], t[i-1])


print("Sean a1, a2 enteros\n")
a1 = int(input("Teclea el valor de a1: "))
print ("\ta1 =",a1)
a2 = int(input("Teclea el valor de a2: "))
print("\ta2 =",a2)
print("\t\tMCD(", a1, ",", a2, ") =", eucExt(int(a1),int(a2))[0])
print("\t\t", eucExt(int(a1),int(a2))[0], "=", a1, "(", eucExt(int(a1),int(a2))[1], ") +", a2, "(", eucExt(int(a1),int(a2))[2], ")" )
