def main():
    N, K = (int(x) for x in sys.stdin.readline().split())
    A = [int(x) for x in sys.stdin.readline().split()]
    setA = set(A)
    c = 0
    for x in A:
        if (x-K) in setA:
            c += 1
    print (c)

if __name__ == '__main__':
    import sys
    main()