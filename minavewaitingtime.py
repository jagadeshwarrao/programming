import heapq

N = int(input())
Tasks = [tuple(int(_) for _ in input().split()) for _ in range(N)]
Tasks.sort()

TotalWaiting = 0
currentTime = 0
currentWaiting = []

i = 0
while i < len(Tasks) :

    # No clients, go to next client
    if not currentWaiting and Tasks[i][0] > currentTime :
        currentTime = Tasks[i][0]

    # Get all client waiting
    while i < len(Tasks) and Tasks[i][0] <= currentTime :
        heapq.heappush(currentWaiting, tuple([Tasks[i][1], Tasks[i][0]]))
        i += 1
    
    # Serve the quickest pizza
    task = heapq.heappop(currentWaiting)
    currentTime += task[0]
    TotalWaiting += currentTime-task[1]
    
    # If no more clients, serve all remaining client and close
    if i >= len(Tasks) :
        while currentWaiting :
            # Serve the quickest pizza
            task = heapq.heappop(currentWaiting)
            currentTime += task[0]
            TotalWaiting += currentTime-task[1]

print(TotalWaiting // N)
            
    
