class Warrior:
    def __init__(self,name,attack):
        self.name=name
        self.attack=attack
    def updateName(self):
        self.name=self.name.swapcase()








def bool_convert(line):
    if(line == "True"):
        line = True
    else:
        line = False
    return line

name = input()
attack = bool_convert(input())

warrior1 = Warrior(name, attack)

print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

warrior1.updateName()

print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

warrior1.updateName()

print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")