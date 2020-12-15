
import sys; 
from math import ceil,log2; 

INT_MAX = sys.maxsize; 

def minVal(x, y) : 
	return x if (x < y) else y; 

def getMid(s, e) : 
	return s + (e - s) // 2; 

def RMQUtil( st, ss, se, qs, qe, index) : 
 
	if (qs <= ss and qe >= se) : 
		return st[index]; 

	if (se < qs or ss > qe) : 
		return INT_MAX; 

	mid = getMid(ss, se); 
	return minVal(RMQUtil(st, ss, mid, qs, 
						qe, 2 * index + 1), 
				RMQUtil(st, mid + 1, se, 
						qs, qe, 2 * index + 2)); 

def RMQ( st, n, qs, qe) : 
 
	if (qs < 0 or qe > n - 1 or qs > qe) : 
	
		print("Invalid Input"); 
		return -1; 
	
	return RMQUtil(st, 0, n - 1, qs, qe, 0); 

def constructSTUtil(arr, ss, se, st, si) : 

	if (ss == se) : 

		st[si] = arr[ss]; 
		return arr[ss]; 

	mid = getMid(ss, se); 
	st[si] = minVal(constructSTUtil(arr, ss, mid, 
									st, si * 2 + 1), 
					constructSTUtil(arr, mid + 1, se, 
									st, si * 2 + 2)); 
	
	return st[si]; 

def constructST( arr, n) : 

	x = (int)(ceil(log2(n))); 

	max_size = 2 * (int)(2**x) - 1; 

	st = [0] * (max_size); 
 
	constructSTUtil(arr, 0, n - 1, st, 0); 

	return st; 

 
if __name__ == "__main__" : 

	arr = [1, 3, 2, 7, 9, 11]; 
	n = len(arr); 

	st = constructST(arr, n); 

	qs = 1; 
	qe = 5;

	print("Minimum of values in range [", qs, 
		",", qe, "]", "is =", RMQ(st, n, qs, qe)); 

import sys; 
from math import ceil,log2; 

INT_MAX = sys.maxsize; 

def minVal(x, y) : 
	return x if (x < y) else y; 

def getMid(s, e) : 
	return s + (e - s) // 2; 

def RMQUtil( st, ss, se, qs, qe, index) : 
 
	if (qs <= ss and qe >= se) : 
		return st[index]; 

	if (se < qs or ss > qe) : 
		return INT_MAX; 

	mid = getMid(ss, se); 
	return minVal(RMQUtil(st, ss, mid, qs, 
						qe, 2 * index + 1), 
				RMQUtil(st, mid + 1, se, 
						qs, qe, 2 * index + 2)); 

def RMQ( st, n, qs, qe) : 
 
	if (qs < 0 or qe > n - 1 or qs > qe) : 
	
		print("Invalid Input"); 
		return -1; 
	
	return RMQUtil(st, 0, n - 1, qs, qe, 0); 

def constructSTUtil(arr, ss, se, st, si) : 

	if (ss == se) : 

		st[si] = arr[ss]; 
		return arr[ss]; 

	mid = getMid(ss, se); 
	st[si] = minVal(constructSTUtil(arr, ss, mid, 
									st, si * 2 + 1), 
					constructSTUtil(arr, mid + 1, se, 
									st, si * 2 + 2)); 
	
	return st[si]; 

def constructST( arr, n) : 

	x = (int)(ceil(log2(n))); 

	max_size = 2 * (int)(2**x) - 1; 

	st = [0] * (max_size); 
 
	constructSTUtil(arr, 0, n - 1, st, 0); 

	return st; 

 
if __name__ == "__main__" : 

	arr = [1, 3, 2, 7, 9, 11]; 
	n = len(arr); 

	st = constructST(arr, n); 

	qs = 1; 
	qe = 5;

	print("Minimum of values in range [", qs, 
		",", qe, "]", "is =", RMQ(st, n, qs, qe)); 
