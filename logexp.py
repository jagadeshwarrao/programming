
def power(x, y): 

	if (y == 0): return 1
	elif (int(y % 2) == 0): 
		return (power(x, int(y / 2)) *
			power(x, int(y / 2))) 
	else: 
		return (x * power(x, int(y / 2)) *
				power(x, int(y / 2))) 
b 
x = 2; y = 3
print(power(x, y)) 


