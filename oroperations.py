# method to cerate a set of the set bits
def getSet(num):
    setBits = set()
    mask = 1
    for pos in range(0, 32):
        if (((mask << pos) & num ) > 0):
            setBits.add(pos)
    return setBits

T = int(input())

for  _ in range(T):
    arr = list(map(int, input().split()))
    assert (len(arr[1:]) == arr[0])
    arr = arr[1:]
    count = 1

    maxOR = 0
    all_sets = []

	# get OR of entire array
    # also create sets for each number
    for num in arr:
        maxOR = num |  maxOR
        all_sets.append(getSet(num))

    # this is our target
    maxSet = getSet(maxOR)


    
    minSubset = [] # stores our final answer
    covered = set([]) # how many bits set so far
    while len(covered) != len(maxSet):
    	# get the set with max difference
        maxDifferenceSet = max(all_sets, key = lambda x: len(x - covered))
        covered = covered | maxDifferenceSet # union of 2 sets
        minSubset.append(maxDifferenceSet)

    print(len(minSubset))




