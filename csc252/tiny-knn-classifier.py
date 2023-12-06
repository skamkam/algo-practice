import math
from random import randint
from random import choice

class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.numPoint = 2
        
    def sum_squares (self, otherPoint):
        return (self.x - otherPoint.getX())**2 + (self.y - otherPoint.getY())**2
    
    def distance_to (self, otherPoint):
        # using distance formula: sqrt((x2-x1)^2 + (y2-y1)^2)
        return math.sqrt( self.sum_squares(otherPoint) )

    # Python calls this method if you try to print a Point
    def __str__ (self):
        return "({},{})".format(self.x, self.y)

    def getNumPoint(self):
        return self.numPoint

    def getX (self):
        return self.x
    
    def getY (self):
        return self.y

class Item (Point):
    def __init__ (self, x, y, item):
        super().__init__(x,y)
        self.item = item
    
    def __str__ (self):
        return "({},{}): {}".format(self.x, self.y, self.item)
    
    def getItem(self):
        return self.item
        
class Point3D (Point):
    def __init__ (self, x, y, z):
        super().__init__(x,y)
        self.z = z
        self.numPoint = 3

    def sum_squares (self, otherPoint3D):
        return super().sum_squares(otherPoint3D) + (self.z - otherPoint3D.getZ())**2

    def __str__ (self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def getZ (self):
        return self.z
                
def get_list_of_Items_for_testing(numPt, maxX, maxY, labels):
    lst = []
    for i in range(numPt):
        x = randint(0,maxX)
        y = randint(0,maxY)
        item = choice(labels)
        pt = Item(x,y, item)
        lst.append(pt)
    return lst

def k_nearest(dataset:list, newPoint:Point, k:int) -> list:
    distList = []
    for i in range(len(dataset)):
        distList.append(newPoint.distance_to(dataset[i]))
    copyDistList = distList.copy()
    copyDistList.sort()
    maxDist = copyDistList[k-1]
    neighbors = []
    for i in range(len(dataset)):
        if distList[i] <= maxDist:
            neighbors.append(dataset[i])
    return neighbors

def classifier(neighbors:list) -> str:
    countDict = {}
    for i in range(len(neighbors)):
        val = neighbors[i].getItem()
        if val in countDict.keys():
            countDict[val] += 1
        else:
            countDict[val] = 1 
    maxVal = ""
    maxNum = 0
    for val, count in countDict.items():
        if count > maxNum:
            maxNum = count
            maxVal = val
        elif count == maxNum:
            maxVal = maxVal + " ties " + val
    return maxVal
    
    
def main():
    dataset = get_list_of_Items_for_testing(20, 50, 50, ["Orange", "Grapefruit"])
    newPoint = Point(25, 25)
    print("Dataset:")
    for i in range(len(dataset)):
        print(dataset[i])
    neighbors = k_nearest(dataset, newPoint, 3)
    print("Neighbors:")
    for i in range(len(neighbors)):
        print(neighbors[i])
    print("Winner:", classifier(neighbors))
main()



    
