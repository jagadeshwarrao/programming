import bisect

class IntervalNode:
    def __init__(self, a, b):
        self.midpoint = (a + b) / 2
        self.left = self.right = None
        self.center_left  = [ a ]
        self.center_right = [ b ]

    def putInterval(self, a, b):
        bisect.insort( self.center_left, a )
        bisect.insort( self.center_right, b )

    def getCrossCount(self, a, b):
        result = 0
        if a <= self.midpoint <= b: return len(self.center_left)
        if b < self.midpoint:
            return bisect.bisect_right(self.center_left, b)
        else:
            return len(self.center_right) - bisect.bisect_left(self.center_right, a)

class IntervalTree:
    def __init__(self):
        self.root = None

    def put(self, a, b):
        self.root = self.put_(self.root, a, b)
    def put_(self, node, a, b):
        if node is None: return IntervalNode(a, b)
        if b < node.midpoint:
            node.left = self.put_(node.left, a, b)
        elif a > node.midpoint:
            node.right = self.put_(node.right, a, b)
        else:
            node.putInterval(a, b)
        return node

    def getCrossCount(self, a, b):
        return self.getCrossCount_(self.root, a, b)
    def getCrossCount_(self, node, a, b):
        if node is None: return 0
        result = node.getCrossCount( a, b )
        if a < node.midpoint:
            result += self.getCrossCount_(node.left, a, min(b, node.midpoint))
        if b > node.midpoint: 
            result += self.getCrossCount_(node.right, max(a, node.midpoint), b)
        return result


tree = IntervalTree()

N, M = map(int, input().split())
for _ in range(N):
    a,b = map(int, input().split())
    tree.put(a, b)

res = 0
for _ in range(M):
    c,d = map(int, input().split())
    res += tree.getCrossCount(c,d)

print(res)
