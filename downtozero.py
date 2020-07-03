import math

import time
start = time.time()

def Sol( N ):
    if N == 0: return 0
    Q = [ (N,0) ]
    setQ = [ 0 ] * N
    while Q:
        N, steps = Q.pop(0)
        if N == 1: return steps+1
        div = int(math.sqrt( N ))
        while div > 1:
            if N % div == 0 and not setQ[N // div]:
                Q.append( (N // div, steps+1) )
                setQ[ N // div ] = 1
            div -= 1
        if not setQ[N-1]:
            Q.append( (N-1, steps+1) )
            setQ[ N-1 ] = 1
            
    
Q = int(input())
for _ in range(Q):
    N = int(input())
    print(Sol(N))