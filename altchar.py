def alt(s):
    return sum(1 for c, c1 in zip(s, s[1:]) if c == c1)

j = int(input())
for _ in range(j):
    print(alt(input()))
