class Warrior:
    def __init__(self,name,attack,strength):
        self.name=name
        self.attack=attack
        self.strength=strength
    def damage(self):
        if(self.attack==True and(self.strength>=1 and self.strength<=10)):
            return 20
        elif(self.attack==True and(self.strength>=11 and self.strength<=20)):
            return 30
        elif(self.attack==True and(self.strength>20)):
            return 100
        else:
            return 0








## your code above this line ##

def bool_convert(line):
    if(line == "True"):
        line = True
    else:
        line = False
    return line


name = input()
attack = bool_convert(input())
strength = int(input())

warrior1 = Warrior(name, attack, strength)

name = input()
attack = bool_convert(input())
strength = int(input())

warrior2 = Warrior(name, attack, strength)

print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")
print(f"warrior1's damage is {warrior1.damage()}")
print("----")

print(f"warrior2's name is {warrior2.name}. Is attacking? {warrior2.attack}")
print(f"warrior2's damage is {warrior2.damage()}")
print("----")
