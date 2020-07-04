import heapq

L,H=[],[]

for _ in range(int(input())) :
    a = int(input())
    if not H :
        heapq.heappush(H,a)
    else :
        if len(H) > len(L) :
            if H[0] < a :
                b = heapq.heappushpop(H,a)
                heapq.heappush(L,-b)
            else :
                heapq.heappush(L,-a)
        else :
            if -L[0] > a :
                b = -heapq.heappushpop(L,-a)
                heapq.heappush(H,b)
            else :
                heapq.heappush(H,a)
    
    if len(H) > len(L) :
        print("%.1f" % H[0])
    else :
        print("%.1f" % ((H[0]-L[0])/2))
        
  
    

