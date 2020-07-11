n=int(input())
for i in range(n):   
    d,v=[d for d in input().split()]
    
    if v=="true":       
        if d=="1" or d=="7":
            print("9:00")
        else:
            print("7:00")
    else:
        if d=="1" or d=="7":
            print("6:00")
        else:
            print("5:00")




