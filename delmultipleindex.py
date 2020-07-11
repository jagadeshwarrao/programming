def solve(A):
    # write your code here
    b=len(A)
    for i in range(0,b):
        if(i==1):
            A.pop(1)
        if(i==3):
            A.pop(3)
        if(i==6):
            A.pop(6)
    return A