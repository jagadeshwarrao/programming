def solve(A,B):
    # write your logic from here
    x1=A['x']
    y1=A['y']
    x2=B['x']
    y2=B['y']
    a=math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
    print(int(a))