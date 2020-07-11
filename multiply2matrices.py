def solve(A,B):
    # write your code here
    if len(A[0])==len(B):
        for i in range(len(A)):
            for j in range(len(B[0])):
                x=0
                for k in range(len(B)):
                    x=x+A[i][k]*B[k][j]
                print(x,end=" ")
            print()
    else:
        print("Impossible")