n=int(input())
lst=list(map(int,input().split()))
count=0
for i in range(0,len(lst)):
    sum1=lst[i]
    if(lst[i]%2!=0):
        count=count+1
    for j in range(i+1,len(lst)):
        sum1=sum1+lst[j]
        if(sum1%2!=0):
            count=count+1
print(count)





