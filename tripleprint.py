n=int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))
for j in list1:
    for k in range(1,j+1):
        for l in range(3):
            print(k,end=' ')
        print()




