class plant:
    def __init__(self, pest):
        self.pest = pest
        self.prevkiller = self.nextkiller = None
    __slots__ = 'pest,next,prevkiller,nextkiller'.split(',')
    
nplants = int(input())
plants = [int(pest) for pest in input().split()]
start = current = plant(plants[0])
curkiller = firstkiller = plant(None)
for pest in plants[1:]:
    current.next = newplant = plant(pest)
    if current.pest < newplant.pest:
            curkiller.nextkiller = current
            current.prevkiller = curkiller
            curkiller = current
    current = newplant
last = current.next = plant(-1)
last.prevkiller = curkiller
curkiller.nextkiller = last
day = 0
while last.prevkiller is not firstkiller:
    day += 1
    curkiller = last.prevkiller
    while curkiller is not firstkiller:
        victim = curkiller.next
        if not(hasattr(victim, "next")):
            print(victim.pest, day)
        curkiller.next = victim.next
        if victim.prevkiller == curkiller:
            curkiller.nextkiller = victim.nextkiller
            victim.nextkiller.prevkiller = curkiller
            victim.prevkiller = victim.nextkiller = None
        curkiller = curkiller.prevkiller

    curkiller = last.prevkiller
    while curkiller is not firstkiller:
        prevkiller = curkiller.prevkiller
        if curkiller.pest >= curkiller.next.pest:
            curkiller.nextkiller.prevkiller = prevkiller
            prevkiller.nextkiller = curkiller.nextkiller
            curkiller.prevkiller = curkiller.nextkiller = None
        curkiller = prevkiller
print(day)
    
    