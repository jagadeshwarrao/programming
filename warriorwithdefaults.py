class Warrior:
    def __init__(self,name,attack):
        self.name=name
        self.attack=attack
    def updateName(self,change=""):
        if(change==""):
            self.name=self.name+"updated"
            return self.name
        elif(change=="upper"):
            self.name=self.name.upper()
            return self.name
        else:
            self.name=self.name.lower()
            return self.name








## your code above this line ##

def bool_convert(line):
    if(line == "True"):
        line = True
    else:
        line = False
    return line

name = input()
attack = bool_convert(input())
change_to_1 = input()
change_to_2 = input()


warrior1 = Warrior(name, attack)

print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

warrior1.updateName()
print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

warrior1.updateName(change_to_1)
print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

warrior1.updateName(change_to_2)
print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")
