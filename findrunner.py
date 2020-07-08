n=int(input())
a=map(int,input().strip().split(" "))
a=list(a)
mx1=a[0]
mn=a[0]
for i in a:
    if(i>mx1):
        mx1=i
    if(i<mn):
        mn=i
mx2=mn
for i in a :
    if(i>mx2 and i<mx1):
        mx2=i
print(mx2)