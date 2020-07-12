import sys
n=input()
l=[]
for i in n:
    if(i.isdigit() and int(i) not in l):
        l.append(int(i))
l.sort(reverse=True)
if(l[-1]%2!=0):
    mini=0
    for i in range(1,len(l)):
        if(l[i]%2==0 and l[i]<l[mini]):
            mini=i
    if(mini!=0):
        k=l.pop(mini)
        l.append(k)
    elif(mini==0 and l[mini]%2==0):
        k=l.pop(mini)
        l.append(k)
    else:
        print("-1")
        sys.exit(0)
for i in l:
    print(i,end="")




