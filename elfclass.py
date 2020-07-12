class Elf:
    def say_hello(self):
        print("Howdy, elf here!")
    def magic(self,n):
        f=1
        for i in range(1,n+1):
            f=f*i
        return f









elf1 = Elf()

elf1.say_hello()

n = int(input())

magical_number  = elf1.magic(n)
print("Magical number is", magical_number)