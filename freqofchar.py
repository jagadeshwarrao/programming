def solve(words):
    # write your solution from here
    lst=[]
    for i in words:
        for j in i:
            lst.append(j)
    alpha=set(lst)
    alphalist=list(alpha)
    alphalist.sort()
    d={}
    for i in alphalist:
        s=lst.count(i)
        d[i]=s
    for j in d:
        print(j+":",d[j])