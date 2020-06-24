# Complete the 'dynamicArray in hackerrank' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

n, q = map(int, input().split())
l = [[] for _ in range(n)]

latsans = 0
for _ in range(q):
    a, x, y = map(int, input().split())
    if a == 1:
        l[(x^latsans)%n].append(y)
    else:
        t = (x^latsans)%n
        latsans = l[t][y%len(l[t])]
        print(latsans)
