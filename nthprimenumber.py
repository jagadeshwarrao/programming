def solve(n):
    # write your code here
    c,i=0,0
    num=0
    while c<n:
        num=num+1
        for i in range(2,num+1):
            if num % i == 0:
                break
        
        if i==num:
            c=c+1
    print(num)