import sys

for t in range(int(sys.stdin.readline().strip())):
    n,m = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    nonzero = {}
    for i in range(m):
        parts = sys.stdin.readline().strip().split(" ")
        t = parts[0]
        vals = [int(x) for x in parts[1:]]
        if t=="UPDATE":
            coords = tuple(vals[:3])
            nonzero[coords] = vals[-1]
        elif t=="QUERY":
            total = 0
            lower = vals[:3]
            upper = vals[3:]
            for (coords, val) in nonzero.items():
               in_bounds = True
               for j in range(3):
                    if not (lower[j] <= coords[j] <= upper[j]):
                        in_bounds = False
               if in_bounds:
                    total += val
            print(total)
        else:
            raise Exception("Input Fubar")
            
    
