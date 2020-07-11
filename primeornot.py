def solve(n):
    # write your code here
    if(n>=0):
        flag=0
        a=int(n/2)
        for i in range(2,a):
            if(n%i==0):
                flag=1
                break
            i=i+1
        if(not flag):
            print("Prime")
        else:
            print("Not Prime")
    else:
        print("Not Prime")