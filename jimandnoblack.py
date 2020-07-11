def solve(num1,num2):
    # write your code from here
    if(num1<=21 and num2<=21):
        if((21-num1)<(21-num2)):
            print("Player1")
        elif((21-num1)>(21-num2)): 
            print("Player2") 
        else: 
            print("Rematch")
    else:
        print("Rematch")