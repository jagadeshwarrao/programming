def solve(num1,num2,special_mode):
    # write your code from here
    if(special_mode==True):
        if(num1==num2==6):
            print("7")
        else:
            if(num1==num2):
                print(num1+num2+1)
            else:
                print(num1+num2)
    else:
        print(num1+num2)