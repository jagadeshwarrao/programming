def read_stack():
    stack = [int(x) for x in input().split(' ')]
    stack = list(reversed(stack))
    sum_stack = set()
    psum = 0
    for i in range(len(stack)):
        psum += stack[i]
        sum_stack.add(psum)
    return sum_stack

input()

ans = read_stack()
ans &= read_stack()
ans &= read_stack()
if len(ans) > 0:
    print(max(ans))
else:
    print(0)