def solve(n):
    # write your code here
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<i:
                print(".",end="")
            else:
                print("*",end="")
        print()