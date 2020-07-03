stack = []
max_stack = []

for _ in range(int(input())):
    try:
        cmd = input()
    except:
        cmd = '3'
    if cmd[0] == '1':
        n = int(cmd.split()[1])
        stack.append(n)
        if len(max_stack) == 0 or max_stack[-1] < n:
            max_stack.append(n)
        else: 
            max_stack.append(max_stack[-1])
    elif cmd == '2':
        stack.pop()
        max_stack.pop()
    else: 
        print(max_stack[-1])
    