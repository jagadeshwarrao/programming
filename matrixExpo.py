
def multiply(a, b): 
	
	mul = [[0 for x in range(3)] 
			for y in range(3)]; 
	for i in range(3): 
		for j in range(3): 
			mul[i][j] = 0; 
			for k in range(3): 
				mul[i][j] += a[i][k] * b[k][j]; 

	for i in range(3): 
		for j in range(3): 
			a[i][j] = mul[i][j]; 
	return a; 

def power(F, n): 

	M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]; 

	if (n == 1): 
		return F[0][0] + F[0][1]; 

	power(F, int(n / 2)); 

	F = multiply(F, F); 

	if (n % 2 != 0): 
		F = multiply(F, M); 

	return F[0][0] + F[0][1] ; 

def findNthTerm(n): 
	F = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]; 

	return power(F, n - 2); 

n = 5; 

print("F(5) is", 
	findNthTerm(n)); 

