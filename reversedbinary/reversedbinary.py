def reverseBinary(x):
	x = bin(x)
	return int(x[:2]+x[2:][::-1], 2)
	
a = raw_input()
a = int(a)

print reverseBinary(a)
