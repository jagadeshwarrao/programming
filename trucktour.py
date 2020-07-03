N = int(input())

s,c = 0,0
for i in range(N) :
    p,d = (int(_) for _ in input().split())
    if c+p < d :
        s = i+1
        c = 0
    else :
        c += p-d
        
print(s)     