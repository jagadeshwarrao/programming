

def findLongestPalindromicString(text): 
	N = len(text) 
	if N == 0: 
		return
	N = 2*N+1 
	L = [0] * N 
	L[0] = 0
	L[1] = 1
	C = 1	 
	R = 2	
	i = 0 
	iMirror = 0	 
	maxLPSLength = 0
	maxLPSCenterPosition = 0
	start = -1
	end = -1
	diff = -1

	for i in xrange(2,N): 
	 
		iMirror = 2*C-i 
		L[i] = 0
		diff = R - i 
		
		if diff > 0: 
			L[i] = min(L[iMirror], diff) 

		
		try: 
			while ((i+L[i]) < N and (i-L[i]) > 0) and \ 
					(((i+L[i]+1) % 2 == 0) or \ 
					(text[(i+L[i]+1)/2] == text[(i-L[i]-1)/2])): 
				L[i]+=1
		except Exception as e: 
			pass

		if L[i] > maxLPSLength:	 
			maxLPSLength = L[i] 
			maxLPSCenterPosition = i 

		if i + L[i] > R: 
			C = i 
			R = i + L[i] 

	start = (maxLPSCenterPosition - maxLPSLength) / 2
	end = start + maxLPSLength - 1
	print "LPS of string is " + text + " : ", 
	print text[start:end+1], 
	print "\n", 

 
text1 = "babcbabcbaccba"
findLongestPalindromicString(text1) 

text2 = "abaaba"
findLongestPalindromicString(text2) 

text3 = "abababa"
findLongestPalindromicString(text3) 

text4 = "abcbabcbabcba"
findLongestPalindromicString(text4) 

text5 = "forgeeksskeegfor"
findLongestPalindromicString(text5) 

text6 = "caba"
findLongestPalindromicString(text6) 

text7 = "abacdfgdcaba"
findLongestPalindromicString(text7) 

text8 = "abacdfgdcabba"
findLongestPalindromicString(text8) 

text9 = "abacdedcaba"
findLongestPalindromicString(text9) 


