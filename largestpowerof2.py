def solve(n):
    # write your code here
    i=1
    while(1):
        if i==n:
            break
        elif(i<=n):
            i=i*2
        else:
            i=i/2
            break
    print(int(i))