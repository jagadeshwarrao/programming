h = int(input())
for _ in range(h):
    _ = (input())
    j = (input())
    x = set([h for h in _])
    y = set([y for y in j])
    if x.intersection(y) == set():
        print("NO")
    else:
        print("YES")