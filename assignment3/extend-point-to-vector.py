import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y =y

    def __eq__(self, other):
       if (self.x==other.x) and (self.y==other.y):
            return True
       else:
           return False
       
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
    def eucl_dist(self, other):
        d = math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return d
           

class Vector(Point):
    def __init__(self, x, y):
        pass
    def __str__(self):
        return f"[{self.x}:{self.y}]"
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
print(Point(1,2))
p1 = Point(1,2)
p2 = Point(4,5)
print("The points are equal: ", p1==p2)
print("Point is: ", p1)
print("Euclidian distance: ", p1.eucl_dist(p2))

v1 = Vector(7,9)
v2 = Vector(3,1)
print("Vector is: ", v1)
print("Sum of vectors: ", v1+v2)
print("The vectors are equal: ", v1==v2)
print("Euclidian distance: ", v1.eucl_dist(v2))