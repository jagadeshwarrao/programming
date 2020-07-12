arr=list(input())
l=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        s=""
        for k in range(i,j+1):
            s=s+arr[k]
        l.append(int(s))
#print(l)

def isPronic(n):
    for i in range(n+1) or [0]:
        if i*(i+1)==n:
            return i
    return -1

l2=[]
for i in set(l):
    if i*(i+1) in l:
        l2.append(i*(i+1))
    #elif i*(i-1) in l:
        #l2.append(i*(i-1))
    #print(i)
    '''a=isPronic(i)
    if(a!=-1):
        #print(i)
        if(a in l and a+1 in l):
            l2.append(i)'''

l2=list(set(l2))
l2.sort()

if(len(l2)==0):
    print(-1)
else:
    for i in l2:
        print(i,end=" ")









