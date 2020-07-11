def solve(A):
    # write your code here
    c=A[0]-A[1]
    f=0
    for i in range(len(A)-1):
        if A[i]-A[i+1]!=c:
            f=1
    if f==0:
        print("True")
    else:
        print("Normal Series")