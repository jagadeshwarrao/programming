from collections import Counter
n,k=map(int,input().split())
l1=list(map(int,input().split()))
d=Counter(l1)
c=0 
if k!=0:
    l=list(set(l1))
else:
    l=list(l)
l.sort()
t=len(l)
if t>2:
  for i in range(1,t-1):
    if l[i]+k>=l[i+1] or l[i]-k <=l[i-1]:
      if k!=0:
          c=c+d[l[i]]
      else:
          c=c+1
  if l[0]+k>=l[1]:
    if k!=0:
          c=c+d[l[i]]
    else:
          c=c+1
  if l[-1]-k<=l[-2]:
    if k!=0:
          c=c+d[l[i]]
    else:
          c=c+1
elif t==2:
  if l[0]+k>=l[1]:
    if k!=0:
          c=c+d[l[i]]
    else:
          c=c+1
  if l[-1]-k<=l[-2]:
    if k!=0:
          c=c+d[l[i]]
    else:
          c=c+1
else:
  c=0  
print(c)
