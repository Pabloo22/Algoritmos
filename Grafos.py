

def check_sequence(sequence):
	""" This algorithm is based on the Havel Hakimi theorem.
	Returns True if the sequence is a graphic one and returns False
	if it isn't.
	"""

	while True:

		sequence.sort(reverse=True)  # O(n log n)
		first = sequence.pop(0)

		for i in range(len(sequence[:first])):
			sequence[i] -= 1

		if -1 in sequence:
			return False
		elif max(sequence) == 0:
			return True



