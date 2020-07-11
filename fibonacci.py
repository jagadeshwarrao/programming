def solve(n):
    # write your code here
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
         print(" ")
    elif n== 1:
        print("0")
    else:
        while count < n:
            print(n1, end=" ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1 