class Fixes:
    def __init__(self,equation):
        self.top = -1
        self.equation=equation
        self.capacity =len(equation)
        self.array=[]
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    def isEmpty(self):
        return True if self.top == -1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return ""
    def push(self, op):
        self.top += 1
        self.array.append(op)
    def isOperand(self, ch):
        return ch.isdigit()
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
    def convert(self):
        for i in self.equation:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while( (not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
       
        self.postfix="".join(self.output).replace("\r","")








## write Fixes class above this line ##

testcases = int(input())
for _ in range(testcases):
    equation = input()
    fix = Fixes(equation)
    print(f'Infix: {equation}')
    fix.convert()
    print(f'Postfix: {fix.postfix}')
    print('---')
