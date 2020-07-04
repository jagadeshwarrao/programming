class ParentPointerTree(object):
    def __init__(self, x):
        self.value = x
        self.parent = self
        self.size = 1
        self.rank = 1

    def find(self):
        p = self
        while p != p.parent:
            p = p.parent
        self.parent = p
        return p

    def union(self, other):
        self_root, other_root = self.find(), other.find()
        if self_root != other_root:
            if self_root.rank < other_root.rank:
                self_root.parent = other_root
                other_root.size += self_root.size
            elif other_root.rank < self_root.rank:
                other_root.parent = self_root
                self_root.size += other_root.size
            else:
                self_root.parent = other_root
                other_root.rank += 1
                other_root.size += self_root.size

people, queries = [ int(x) for x in input().split() ]

elements = { p : ParentPointerTree(p) for p in range(1, people + 1) }

def query(x):
    print(elements[x].find().size)

def merge(x, y):
    elements[x].union(elements[y])
        
commands = { "Q" : query, "M" : merge }

for _ in range(queries):
    command, *params = input().split()
    params = [ int(p) for p in params ]
    commands[command](*params)