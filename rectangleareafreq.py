def solve(list1):
    # complete the method solve
    area=[]
    for i in list1:
        a=i[0]*i[1]
        area.append(a)
    freq=[]
    setarea=sorted(list(set(area)))
    for i in setarea:
        temp=[i,area.count(i)]
        freq.append(temp)
    for i in freq:
        m=str(i[0])+": "+str(i[1])
        print(m)
    print()