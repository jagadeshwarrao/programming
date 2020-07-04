import sys
from collections import deque
def combine(a, b):
    return a + b * 2

n, k = [int(x) for x in input().split()]
queue = deque(sorted([int(x) for x in input().split()]))
#print(queue, file=sys.stderr)
combines = 0
n_queue = deque()
top_two = []
while queue:
    if queue and n_queue and len(queue) == 1:
        while n_queue:
            #print('adding new at the end:', n_queue[0], file=sys.stderr)
            queue.append(n_queue.popleft())
    if queue and n_queue and n_queue[0] <= queue[0]:
        #print('adding to queue:', n_queue[0], file=sys.stderr)
        queue.appendleft(n_queue.popleft())
    if queue and len(top_two) == 0 and k <= queue[0]:
        break
    cookie = queue.popleft()
    #print('cookie:', cookie, file=sys.stderr)
    top_two.append(cookie)
    if len(top_two) == 2:
        #print('combine:', top_two[0], top_two[1], file=sys.stderr)
        new_cookie = combine(top_two[0], top_two[1])
        #print('new cookie:', new_cookie, file=sys.stderr)
        top_two = []
        n_queue.append(new_cookie)
        combines += 1
while n_queue:
    queue.append(n_queue.popleft())
#print('final:', queue, file=sys.stderr)
if any(x < k for x in queue):
    print('-1')
else:
    print(combines)