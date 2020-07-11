def solve(start,end):
    # write your code here
    l=[]
    for i in range(start,end+1):
        if i%15==0:
            l.append("FizzBuzz")
        elif i%3==0:
            l.append("Fizz")
        elif i%5==0:
            l.append("Buzz")
        else:
            l.append(i)
    return l