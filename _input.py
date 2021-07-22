def getting_input():
	"""
	Gets input from user and implements it into an 2 dim array
	"""
	print('Enter a table:')
	return [list(map(int, list(input()))) for _ in range(9)]
