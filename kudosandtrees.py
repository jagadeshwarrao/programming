n = int(input())

p = list(range(n))
rank = [0] * n
size = [1] * n

def get(v):
	stack = []
	while p[v] != v:
		stack.append(v)
		v = p[v]
	for u in stack:
		p[u] = v
	return v

def union(v1, v2):
	v1 = get(v1)
	v2 = get(v2)
	if v1 == v2:
		return
	if rank[v1] < rank[v2]:
		v1, v2 = v2, v1
	size[v1] += size[v2]
	p[v2] = v1
	rank[v1] += 1

for _ in range(n - 1):
	x, y, col = input().split()
	if col == 'b':
		union(int(x) - 1, int(y) - 1)

a = [size[i] for i in range(n) if p[i] == i]

MOD = 10**9 + 7
def solve(a):
	s1 = [0]
	for x in a:
		s1.append((s1[-1] + x) % MOD)
	s2 = [0]
	for i, x in enumerate(a):
		s2.append((s2[-1] + x * s1[i]) % MOD)
	s3 = [0]
	for i, x in enumerate(a):
		s3.append((s3[-1] + x * s2[i]) % MOD)
	return s3[-1]

print(solve(a))