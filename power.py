def add(x,y):
	z = x + y
	return z



def multiply(a,b):
	total = 0
	for x in range(a):
		total = add(total,b)
	return total

def power(p,o):
	pow = 1
	for x in range(o):
		pow = multiply(pow,p)
	return pow

print(power(10,2))

