class Box:
    def __init__(self,height=20,width=30,breadth=3):
        self.height=height
        self.width=width
        self.breadth=breadth
    def volume(self):
        return self.height*self.width*self.breadth







## your code above this line ##

height = int(input())
width = int(input())
breadth = int(input())

box1 = Box(height,width,breadth)

print(f"box1 of height: {box1.height}, width: {box1.width} and breadth: {box1.breadth}")
print(f"box1 has volume: {box1.volume()}")

box2 = Box()

print(f"box2 of height: {box2.height}, width: {box2.width} and breadth: {box2.breadth}")
print(f"box2 has volume: {box2.volume()}")