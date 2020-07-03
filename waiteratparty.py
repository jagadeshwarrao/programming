def Primes(q):
    i = 2
    result = []
    n = 1
    while len(result) < q:
        n += 1
        while i < n:
            flag = True
            for item in range(2, int(i**0.5)+1):
                if i % item == 0 and i != item: 
                    flag = False
                    break
            if flag:
                result.append(i)
            i += 1
    return result

temp = [int(i) for i in input().split()]
N = temp[0]
Q = int(temp[1])
primes = Primes(Q)
pile = [int(i) for i in input().split()]

prime_pile = []

for prime in primes:
    notP = []
    yes = []
    for plate in pile:
        if plate % prime == 0:
            yes.append(plate)
        else:
            notP.append(plate)
    pile = notP[::-1]
    prime_pile.append(yes[::-1])
    
big=[]
for platelist in prime_pile:
    r = platelist[::-1]
    for plate in r:
        big.append(plate)

for plate in big: print(plate)
for i in range(len(pile)):
    print(pile[-(i+1)])


