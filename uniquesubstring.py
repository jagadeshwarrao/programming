s=input()
lst=list(s)
lst1=[]
for i in lst:
    if(i not in lst1):
        lst1.append(i)
    else:
        break
st=''.join(lst1)
if(len(st)>=3):
    print(st)
else:
    print(-1)




