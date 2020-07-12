class Calculator:
    def sum(self,l):
        self.l=l
        s=0
        for i in self.l:
            s+=i
        return s
    def minus(self,a,b):
        self.a,self.b=a,b
        return self.a-self.b
    def multiply(self,l):
        self.l=l
        p=1
        for i in self.l:
            p*=i
        return p
    def divide(self,a,b):
        self.a,self.b=a,b
        if self.b==0:
            return 'Div by 0 not allowed!'
        else:
            return self.a//self.b









calc = Calculator()

first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
fifth = int(input())

sum_list = [first,second,third,fourth,fifth]
answer_1 = calc.sum(sum_list)
print(f"Sum of {sum_list} is {answer_1}")

answer_2 = calc.minus(first,second)
print(f"{first} - {second} = {answer_2}")

answer_3 = calc.multiply(sum_list[:-1]) # selecting only first 4 values
print(f"Multiplying {sum_list[:-1]} = {answer_3}")

answer_4 = calc.divide(fourth,fifth)
print(f"Dividing {fourth}/{fifth} = {answer_4}")