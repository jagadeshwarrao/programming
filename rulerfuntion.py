def solve(n):
    # write your code here
    s=""
    for i in range(1,n+1):
        if i==1:
            s=s+str(i)
        else:
            s=s+" "+str(i)+" "+s
    print(s)