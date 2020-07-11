def solve(num1,num2):
    # write your code from here
    if(num1==num2):
        a=0
        print(a)
    elif(num1%6==num2%6):
        a=min(num1,num2)
        print(a)
    else:
        a=max(num1,num2)
        print(a)
        