from collections import defaultdict

N, Q = map(int, input().split())

weights = []

for _ in range(N-1):
    U, V, W = map(int, input().split())
    weights.append([W, U, V])
    
weights.sort()

class Node():
    def __init__(self, size, parent=None):    
        self.size = size
        self.parent = parent

clusters = {n:Node(1) for n in range(1,N+1)}
counts = defaultdict(int)

for W, U, V in weights:
    u = clusters[U]
    v = clusters[V]
    
    while u.parent:
        u = u.parent
        
    while v.parent:
        v = v.parent
    
    counts[W] += u.size * v.size
    
    n = Node(u.size + v.size)
    u.parent = n
    v.parent = n
    
    clusters[U] = n
    clusters[V] = n

K = sorted(counts)
V = [counts[k] for k in K]

Z = [0]
t = 0

for v in V:
    t += v
    Z.append(t)

import bisect

for _ in range(Q):
    L, R = map(int, input().split())
    
    x = bisect.bisect_left(K, L)
    y = bisect.bisect_right(K, R)    
    print(Z[y] - Z[x])