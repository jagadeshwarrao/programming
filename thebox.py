class Box:
    def __init__(self,height,width,breadth):
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