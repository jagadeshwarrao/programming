class Warrior:
    def say_hello(self):
        print("Argh! I am a Warrior!")
    def roar(self,n):
        for i in range(0,n):
            print("Roar",end="")










warrior1 = Warrior()

warrior1.say_hello()

times = int(input())

warrior1.roar(times)