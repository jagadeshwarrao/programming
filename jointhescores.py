def solve(football,cricket,basketball,chess,volleyball):
    # write your solution from here
    lst=[football,cricket,basketball,chess,volleyball]
    lst1=[]
    d={}
    for i in range(0,5):
        d[i]=lst[i]
        for j in lst[i]:
            if(j not in lst1):
                lst1.append(j)
    lst1.sort()
    final={}
    for i in lst1:
        res=0
        for j in lst:
            for k in j:
                if(k==i):
                    res=res+j[k]
        final[i]=res
    for i in final:
        print(i+":",final[i])
    
    

