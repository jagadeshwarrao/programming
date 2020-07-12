class Solution:
    def evaluateRPN(self, A):
        # write your method here
        stack = []
        tokens=A
        for c in tokens:
            try:
                stack.append(int(c))
            except:
                a = stack.pop()
                b = stack.pop()
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(b - a)
                elif c == '*':
                    stack.append(a * b)
                else:
                    if a * b < 0 and b % a:
                        stack.append(b // a + 1)
                    else:
                        stack.append(b // a)
        return stack[0]