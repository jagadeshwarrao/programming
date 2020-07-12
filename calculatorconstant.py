class Calculator:
    g=9.8
    e=2.71
    pi=3.14
    def add(self,num1,num2):
        return num1+num2
    def absolute(self,num1,num2):
        return num1-num2







a = int(input())
b = int(input())

calc = Calculator()

if(a > b):
    print(f"{a} added to g = {calc.add(a,Calculator.g)}")
else:
    print(f"absolute of {b} and e = {calc.absolute(b,Calculator.e)}")

Calculator.pi = 2.14

print(f"Now pi is {Calculator.pi}")