l=list(map(str,input().split(",")))
for x in l:
    st,num=x.split(":")
    s=0
    num=int(num)
    while(num>0):
        r=num%10
        s+=r*r
        num=num//10
    if(s%2==0):
        st=st[-1]+st[0:len(st)-1]
        print(st)
    else:
        st=st[1:len(st)]+st[0]
        st=st[1:len(st)]+st[0]
        print(st)



