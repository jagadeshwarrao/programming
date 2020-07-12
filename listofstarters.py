def solve(items):
    # write your code from here
    lst=[]
    d={}
    for i in items:
        lst.append(i[0])
    lst.sort()
    for i in lst:
        lst1=[]
        for j in items:
            if(i==j[0]):
                lst1.append(j)
        lst1.sort()
        st=" ".join(lst1)
        d[i]=st
    for i in d:
        print(i,":",d[i])
            