class Warrior:
    def __init__(self,name,attack):
        self.name=name
        self.attack=attack
    def myEnemy(self,obj):
        print(f"My name is [{self.name}] and my enemy is [{obj.name}]")







## your code above this line ##

class Boy:
    def __init__(self,name):
        self.name = name

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

boy_name = input()
boy1 = Boy(boy_name)

warrior1.myEnemy(boy1)