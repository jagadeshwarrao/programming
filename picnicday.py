def solve(num1,num2):
    # write your code from here
    if (num1>=13 and num1<=19) or (num2<=19 and num2>=13):
        print("40")
    elif(num1==4 and num2==7) or (num1==7 or num2==4):
        print ("11")
    else:
        print(num1+num2)
    