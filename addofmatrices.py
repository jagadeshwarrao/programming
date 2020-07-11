def solve(A,B):
    # write your code here
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j]+B[i][j],end=" ")
        print()