def solve(A,B):
    # write your code from here
    s=set(A).union(set(B))
    u=list(s)
    u.sort()
    for i in u:
        print(i,end=" ")