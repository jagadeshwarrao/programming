def solve(n):
    # write your code here
    count=0
    j=0
    k=0
    while count<n :
        k=fib(n)
        count=count+1
        j=j+1
    print(k)
def fib(p):
    a=0
    b=1
    c=1
    d=0
    f=0
    if p==1:
        return 0
    else:
        for i in range(2,p+1,+1):
            f=a+b+c
            a=b
            b=c
            c=f
        d=a
        return d