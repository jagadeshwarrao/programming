from bisect import bisect_left

class Shell:
    def __init__(self, distances):
        self.size = sum(distances)
        self.list = distances
        self.elements = len(self.list)
    def __str__(self):
        return '({}, {})'.format(self.size, self.list)
    def FindValue(self, value):
        i = bisect_left(self.list, value)
        return i if (self.elements != i and self.list[i] == value) else None
    def DestroyElement(self, element):
        v = self.list.pop(element)
        self.size -= v
        self.elements -= 1
        return (self.size == 0)
    def Sum(self, element):
        leftSum = (self.list[element] * element) - sum(self.list[0:element])
        rightSum = sum(self.list[element+1:]) - ((self.elements - element - 1) * self.list[element])
        return leftSum + rightSum
    def GetSize(self, element):
        return self.list[element]
    def CalculateBeforeSize(self, size):
        return (size * self.elements) - self.size
    def CalculateAfterSize(self, size):
        return self.size - (size * self.elements)
    def __lt__(self, other):
        return self.list[self.elements - 1] < other

class DistanceList:
    def __init__(self, distances):
        numShells = min(int(len(distances) / 3000) + 1, 16)
        perShell = int(len(distances)/numShells)
        additional = len(distances) % numShells
        self.shells = list()
        curShell = 0
        for i in range(numShells):
            plus1 = 1 if additional > 0 else 0
            nextShell = curShell + perShell + plus1
            self.shells.append(Shell(distances[curShell:nextShell]))
            curShell = nextShell
            additional -= 1
    def FindValue(self, value):
        s = bisect_left(self.shells, value)
        return (s, self.shells[s].FindValue(value))
    def DestroyElement(self, element):
        if(self.shells[element[0]].DestroyElement(element[1])):
            self.shells.pop(element[0])
    def CalculateDistance(self, element):
        citySize = self.shells[element[0]].GetSize(element[1])
        distanceBefore = 0
        for s in self.shells[:element[0]]:
            distanceBefore += s.CalculateBeforeSize(citySize)
        distanceAfter = 0
        for s in self.shells[element[0] + 1:]:
            distanceAfter += s.CalculateAfterSize(citySize)
        return distanceBefore + distanceAfter + self.shells[element[0]].Sum(element[1])
    def __str__(self):
        return '\n'.join([str(s) for s in self.shells])

class DistanceFinder:
    def __init__(self, distances):
        self.distanceList = DistanceList(sorted(distances))
    def CalculateDistance(self, value):
        element = self.distanceList.FindValue(value)
        distance = self.distanceList.CalculateDistance(element)
        self.distanceList.DestroyElement(element)
        return distance
    def Print(self):
        print(str(self.distanceList))

def CalculateCable(distances, populations):
    totalDistance = 0
    sortedPop = sorted(zip(distances, populations), key=lambda x : x[1], reverse=True)
    df = DistanceFinder(distances)
    for (distance, population) in sortedPop:
        totalDistance += df.CalculateDistance(distance) * population
    print(totalDistance % 1000000007)

tests = int(input())
for t in range(tests):
    cities = int(input())
    distances = list(map(int, input().split()))
    populations = list(map(int, input().split()))
    CalculateCable(distances, populations)