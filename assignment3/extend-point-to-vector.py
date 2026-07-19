import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y =y

    def equality(self, other):
       if (self.x==other.x) and (self.y==other.y):
            return True
       else:
           return False
       
    def string_representation(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
    def eucl_dist(self, other):
        d = math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return d
           

class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x,y)
    def string_representation(self):
        return f"[{self.x}:{self.y}]"
    def add(self, other):
        x_sum = self.x + other.x
        y_sum = self.y + other.y
        return f"[{x_sum}:{y_sum}]"
    
print(Point(1,2))
p1 = Point(1,2)
p2 = Point(4,5)
print("The points are equal: ", p1.equality(p2))
print("Point is: ", p1.string_representation())
print("Euclidian distance: ", p1.eucl_dist(p2))

v1 = Vector(7,9)
v2 = Vector(3,1)
print("Vector is: ", v1.string_representation())
print("Sum of vectors: ", v1.add(v2))
print("The vectors are equal: ", v1.equality(v2))
print("Euclidian distance: ", v1.eucl_dist(v2))