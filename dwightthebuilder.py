def solve(target,big_bricks,small_bricks):
    i=1
    while(i<=big_bricks):
        if 5*i<=target:
            pass
        else:
            break;
        i=i+1
        
        
    if 5*i==target:
        print("Possible")
    else:
        i=i-1
        temp=target-5*i
        if temp<=small_bricks:
            print("Possible")
        else:
            print("Impossible")
    # write your code from here