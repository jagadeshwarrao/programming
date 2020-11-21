
import random

def power(a, n, p):
	
	 
	res = 1
	
	a = a % p 
	
	while n > 0:
		
		if n % 2:
			res = (res * a) % p
			n = n - 1
		else:
			a = (a ** 2) % p
			

			n = n // 2
			
	return res % p

def isPrime(n, k):
	
	if n == 1 or n == 4:
		return False
	elif n == 2 or n == 3:
		return True
	
	
	else:
		for i in range(k):
			
			a = random.randint(2, n - 2)
			
			if power(a, n - 1, n) != 1:
				return False
				
	return True
	
k = 3
if isPrime(11, k):
print("true")
else:
print("false")

if isPrime(15, k):
print("true")
else:
print("false")


