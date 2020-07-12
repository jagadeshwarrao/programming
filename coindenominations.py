N = int(input())
    
M = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

X=0
    
for i in M:
    if(N >= i):
        #print(N//i, '*', i)
        if(i==1):
            X += N
        else:
            X += N//i
        N = N % i
    if(N == 0):
        break
        
print(X)




