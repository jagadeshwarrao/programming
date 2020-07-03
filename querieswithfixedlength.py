from collections import deque
import heapq
n,q = map(int,input().split())
l = list(map(int,input().split()))

for _ in range(q):
    d = int(input())
    q = deque([],d)
    h = []
    for i in range(d):
  
        while len(q) and l[i] >= l[q[-1]]:
            q.pop()
        q.append(i)
        
    for i in range(i+1,len(l)):

        heapq.heappush(h,l[q[0]])     
        while len(q) and q[0] <= i - d:
            q.popleft()
            
        while len(q) and l[i] >= l[q[-1]]:
            q.pop()
        q.append(i)
    heapq.heappush(h,l[q[0]])     
    print(h[0])