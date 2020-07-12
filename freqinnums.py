def solve(items):
    # write a code from here
    items.sort()
    d={}
    for i in items:
        s=items.count(i)
        if i not in d:
            d[i]=s
    for i in d:
        print(str(i)+":",d[i])