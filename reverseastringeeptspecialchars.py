def isAlphabet(x): 
    return x.isalpha() 
def toList(string): 
    List = [] 
    for i in string: 
        List.append(i) 
    return List
def toString(List): 
    return ''.join(List) 
def swap(a, b): 
    return b, a 

string=input()
LIST = toList(string) 
r = len(LIST) - 1
l = 0
while l < r:
    if not isAlphabet(LIST[l]):
        l += 1
    elif not isAlphabet(LIST[r]):
        r -= 1
    else:
        LIST[l], LIST[r] = swap(LIST[l],LIST[r]) 
        l += 1
        r -= 1
print(toString(LIST))






