
from queue import PriorityQueue

def solve(a):
	

	pq = PriorityQueue()
	
	num1 = ""
	num2 = ""

	for x in a:
		pq.put(x)

	while not pq.empty():
		num1 += str(pq.get())
		if not pq.empty():
			num2 += str(pq.get()) 

	sum = int(num1) + int(num2)
	
	return sum
	
if __name__=="__main__":
	
	arr = [ 6, 8, 4, 5, 2, 3 ]
	print("The required sum is ", solve(arr))

