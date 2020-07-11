def solve(n):
    # write your code here
    for i in range(2*n+1):
        if i<=n:
            for j in range(2*n+1):
                if j<=i  or j>=2*n-i:
                    print("*",end="")
                else:
                    print(".",end="")
            print()
        else:
            for j in range(2*n+1):
                if j<=2*n-i or j>i-1:
                    print("*",end="")
                else:
                    print(".",end="")
            print()