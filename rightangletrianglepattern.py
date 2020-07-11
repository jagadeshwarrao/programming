def solve(n):
    # write your code here
    k=0
    for i in range(1,n+1):
      
        for j in range(1,n-i+1+1):
            k=k+1
            if k==10:
                k=1
            print(k,end="")
        print()