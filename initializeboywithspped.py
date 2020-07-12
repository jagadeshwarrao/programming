class Boy:
    def __init__(self,clothes,mood,speed):
        self.clothes=clothes
        self.mood=mood
        self.speed=speed
    def accelerate(self):
        self.speed=speed+10









clothes = input()
mood = input()
speed = int(input())

boy1 = Boy(clothes,mood,speed)

print(f"boy1's cloths are {boy1.clothes} and mood is {boy1.mood}")
print(f"boy1's current speed is {boy1.speed}")

boy1.accelerate()
print(f"After acceleration, boy1's speed is {boy1.speed}")