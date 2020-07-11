def solve(A):
    # write your code here
    f=1
    
    for i in range(0,len(A)):
        s=0
        s1=0
        for j in range(0,i+1):
            s=s+A[j]           
        for k in range(i+1,len(A)):
                s1=s1+A[k]               
        if s==s1:
            f=0
            break
    if f==0:
        print("True")
    else:
        print("False")
            