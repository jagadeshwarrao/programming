def solve(num):
    # write your program from here
     
    s=num%10
    num=num/10
    d=s*10+num
    return int(d)