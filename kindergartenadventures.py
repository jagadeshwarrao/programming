import sys
n = int(sys.stdin.readline())
t = [int(x) for x in sys.stdin.readline().split()]

current_available = 0
become_unavailable = [0] * (3 * n)
best_index = 1
best_result = 0
for i in range(2*n):
    el = t[i % n]
    become_unavailable[i + (n - el)] += 1
    if current_available > best_result:
        best_result = current_available
        best_index = i % n + 1
    if current_available == best_result:
        best_index = min(i % n + 1, best_index)
    current_available += 1
    current_available -= become_unavailable[i]
       
print(best_index)
