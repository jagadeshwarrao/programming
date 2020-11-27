


def modInverse(a, m): 
	a = a % m 
	for x in range(1, m): 
		if ((a * x) % m == 1): 
			return x 
	return 1



a = 3
m = 11

print(modInverse(a, m)) 


