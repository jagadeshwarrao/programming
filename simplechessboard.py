n=int(input())
for i in range(1,n+1):
    for j in range(n):
        if((i+j)%2==0):
            print("B",end="")
        else:
            print("W",end="")
    print()




