def countSort(arr, n, exp): 
	output = [0] * n 
	count = [0] * n 
	for i in range(n): 
		count[i] = 0
        
	for i in range(n): 
		count[ (arr[i] // exp) % n ] += 1

	for i in range(1, n): 
		count[i] += count[i - 1] 

	for i in range(n - 1, -1, -1): 

		output[count[ (arr[i] // exp) % n] - 1] = arr[i] 
		count[(arr[i] // exp) % n] -= 1

	for i in range(n): 
		arr[i] = output[i] 

def sort(arr, n) : 
	
	countSort(arr, n, 1) 

	countSort(arr, n, n) 

 
if __name__ =="__main__": 
	 
	arr = [40, 12, 45, 32, 33, 1, 22] 
	n = len(arr) 
	print(*arr) 
	
	sort(arr, n) 
	print(*arr) 