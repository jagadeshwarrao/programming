def solve(string):
    # write your code from here
    if(string[0]=='f' and string[-1]=='b'):
        print("FizzBuzz")
    elif(string[0]=='f'):
        print("Fizz")
    elif(string[-1]=='b'):
        print("Buzz")
    else:
        print(string)