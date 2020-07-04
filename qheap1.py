import bisect
class sortedlist(list):
    def __init__(self,seq,*args,**kwargs):
        list.__init__(self,seq)
        self.key = kwargs.get("key",lambda a:a)
        self.sort(key=self.key)
        self.keylist = [self.key(a) for a in self]
    def __setitem__(self,k,v):
        return NotImplemented
    def __delitem__(self,k):
        list.__delitem__(self,k)
    def __contains__(self,v):
        i = bisect.bisect_left(self.keylist,self.key(v))
        return len(self)!=0 and i < len(self) and self[i] == v
    def __reversed__(self):
        return NotImplemented
    def insert(self,k,v):
        return NotImplemented
    def append(self,v):
        i = bisect.bisect(self.keylist, self.key(v))
        self.keylist.insert(i, self.key(v))
        list.insert(self,i, v)
    def extend(self, seq):
        for a in seq:
            self.append(a)
    def reverse(self):
        return NotImplemented
    def pop(self,index=-1):
        self.keylist.pop(index)
        return list.pop(self,index)
    def remove(self,v):
        i = bisect.bisect_left(self.keylist, self.key(v))
        del self.keylist[i]
        del self[i]
    def __add__(self,v):
        return sortedlist(list.__add__(self,v))
    def __iadd__(self,v):
        s = sortedlist(self,key=self.key)
        s.extend(v)
        return s
    def __repr__(self):
        return list.__repr__(self)
    def __str__(self):
        return list.__str__(self)
    def pairs(self):
        return zip(self,self.keylist)
h= sortedlist([])
for _ in range(int(input())):
    inp = list(map(int,input().split()))
    if inp[0] == 1:
        h.append(inp[1])
    elif inp[0] == 2:
        h.remove(inp[1])
    elif inp[0] == 3:
        print(h[0])