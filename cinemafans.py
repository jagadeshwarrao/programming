def solve(acting_power,rating):
    # write your code from here
    if(acting_power>8 or rating>8)and(acting_power>2 and rating>2):
        print("Yes")
    elif(acting_power<2 or rating<2):
        print("No")
    else:
        print("Maybe")