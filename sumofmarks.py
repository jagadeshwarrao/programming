def solve(marks):
    # write your code from here
    d={}
    lst=[]
    lst1=[]
    sumlist={}
    for i in marks:
        s=0
        d[i['English']]=i['name']
        lst.append(i['English'])
        for j in i:
            if(j!='name'):
                s=s+i[j]
        sumlist[s]=i['name']
        lst1.append(s)
    m=max(lst)
    m1=max(lst1)
    print("Max English:",d[m])
    print("Max Marks:",sumlist[m1])