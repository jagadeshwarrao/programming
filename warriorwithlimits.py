class Warrior:
    LEVEL=1
    def __init__(self,name,strength):
        self.name=name
        if(Warrior.LEVEL==1):
            self.strength=min(strength,20)
        elif(Warrior.LEVEL==2):
            self.strength=min(strength,30)
        elif(Warrior.LEVEL==3):
            self.strength=min(strength,50)
        else:
            self.strength=strength







## your code above this line ##


Warrior.LEVEL = int(input())
name = input()
strength = int(input())

warrior1 = Warrior(name, strength)

print(f"Current level is {Warrior.LEVEL}")
print(f"warrior1's name is {warrior1.name}. Strength is {warrior1.strength}")
print("----")