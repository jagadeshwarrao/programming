def solve(chocolates,is_weekend):
    # write your code from here
    if(is_weekend==True):
        if(chocolates>20 ):
            print("true")
        else:
            print("false")
    else:
        if(chocolates>=20 and chocolates<=40):
            print("true")
        else:
            print("false")