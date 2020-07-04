class UF:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)
        
    def _parent(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a
    
    def _size(self, a):
        return self.size[self._parent(a)]
    
    def merge(self, a, b):
        a, b = self._parent(a), self._parent(b)
        if a != b:
            if self._size(a) < self._size(b):
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

    def __repr__(self):
        return self.parent.__str__() + "\n" + self.size.__str__()

T = int(input())
uf = UF(T * 2)
for _ in range(T):
    uf.merge(*map(int, input().split()))
print(min(sz for node, sz in zip(range(T * 2 + 1), uf.size) if sz != 1 and node == uf._parent(node)), end=" ")
print(max(uf.size))