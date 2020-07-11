def solve(num1,num2):
    # write your code from here
    if(num1==7 or num2==7):
        print("Lucky!")
    elif(num1+num2==7):
        print("Lucky!")
    elif(num1-num2==7 or num2-num1==7):
        print("Lucky!")
    else:
        print("Not Lucky!")