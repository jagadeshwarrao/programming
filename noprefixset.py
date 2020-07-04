class solution:
    def checkSET(self, strs):
        trie = dict()
        for cstr in strs:
            curr = trie
            for ch in cstr:
                if ch not in curr:
                    curr[ch] = dict()
                curr = curr[ch]
                if '_end' in curr:
                    return cstr
            if len(curr) > 0:
                return cstr
            curr['_end'] = ''
        return ''
    
n = int(input())
strs = []
for i in range(n):
    strs.append(input())
sol = solution()
ret = sol.checkSET(strs)
if ret == '':
    print('GOOD SET')
else:
    print('BAD SET')
    print(ret)