def solve(n1):
    # write your code here
    
    l=[]
    a=0
    b=1
    c=0
    if n1==0:
        l.append(n)
    elif n1==1:
        l.append(0)
        l.append(1)
    else:
        l.append(0)
        l.append(1)
        while n1-1>0:
            c=a+b
            l.append(c)
            a=b
            b=c
            n1=n1-1
       
    return l
        
    