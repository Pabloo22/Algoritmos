"""
From Wikipedia:
In computability theory, the Ackermann function, named after Wilhelm Ackermann, 
is one of the simplest and earliest-discovered examples of a total computable 
function that is not primitive recursive. All primitive recursive functions are 
total and computable, but the Ackermann function illustrates that not all total 
computable functions are primitive recursive. After Ackermann's publication 
of his function (which had three nonnegative integer arguments), many authors 
modified it to suit various purposes, so that today "the Ackermann function" 
may refer to any of numerous variants of the original function. One common 
version, the two-argument Ackermann–Péter function, is defined as follows 
for nonnegative integers m and n:

A(0, n) = n + 1
A(m, 0) = A(m - 1, 1)
A(m, n) = A(m - 1, A(m, n - 1))
"""

def ackermann_function_v1(m, n):

	if m == 0:
		return n + 1
	elif n == 0:
		return ackermann_function_v1(m - 1, 1)
	else:
		return ackermann_function_v1(m -1, 
									ackermann_function_v1(m, n -1))


def ackermann_function_v2(m, n):

	stack = [m]

	while stack:
		if stack[-1] == 0:
			stack.pop()
			n += 1
		elif n == 0:
			stack[-1] -= 1
			n = 1
		else:
			stack.append(stack[-1])
			stack[-2] -= 1
			n -= 1

	return n
