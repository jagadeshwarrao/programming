n_elements = int(input())
data = list(map(int, input().split()))
assert len(data) == n_elements

res = 0
minima = [data[0]]
for i in range(1, n_elements):
    d = data[i]
    while len(minima):
        x = minima.pop()
        res = max(d ^ x, res)
        if x < d:
            minima.append(x)
            break
    minima.append(d)
print(res)