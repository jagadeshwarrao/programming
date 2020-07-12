n=int(input());temp=n*2-1
for i in range(n):
    print("*",end=" ")
print()
cnt=1
for i in range(n-2):
    t=temp-(cnt*2)-2
    s=' '*cnt+'*'+' '*t+'*'
    cnt+=1
    print(s)
print(' '*(n-1)+'*'+' '*(n-1))





