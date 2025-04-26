#1)
list1= (list(range(6)))
list2= (list(range(4,11,2)))  
list3= (list(range(10,5,-1))) 
list4= (list(range(10,-11,-5)))  
print(list1)
print(list2)
print(list3)
print(list4)

#2)
Output=[(1, 2, 0), (2, 4, -1), (3, 6, -2), (4, 8, -3), (5, 10, -4)]
zip() function returns an iterator of tuples, where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together and so on.


#3)
Output=[2, 3, 4]

def add1(num):
    return num+1
r = list(map(add1, [1, 2, 3]))  
print(r)


#4)
r = list(map(lambda num: num + 1, [1, 2, 3]))
print(r)


#5)
Output:
[10, 20, 30]
0


#6)
x = [1, 2, 10, 13, 1]
even = [True if y%2==0 else False for y in x]
print(even)


#7)
class Point2D:
    def __init__(self, x=0, y=0):  
        self.x = x  
        self.y = y  

    def __str__(self): 
        return f"({self.x}, {self.y})"

    def add(self, p): 
        self.x += p.x  
        self.y += p.y 

    def distance(self, p): 
        delta_x = self.x - p.x  
        delta_y = self.y - p.y  

        dist = (delta_x ** 2 + delta_y ** 2) ** 0.5  
        return dist


p1 = Point2D(1, 2)
p2 = Point2D(4, -2)

p2.add(p1)

print(p2)
print(p1.distance(p2))


print(p1.distance(p2))


#7)2
class Point2D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x  
        self.y = y  
        self.z = z

    def __str__(self): 
        return f"({self.x}, {self.y})"

    def add(self, p): 
        self.x += p.x  
        self.y += p.y  
        self.z += p.z

    def subtract(self, p):
        self.x -= p.x
        self.y -= p.y
        self.z -= p.z

    def distance(self, p): 
        delta_x = self.x - p.x  
        delta_y = self.y - p.y 
        delta_z = self.z - p.z

        dist = (delta_x ** 2 + delta_y ** 2 + delta_z **2) ** 0.5  
        return dist


p1 = Point2D(1, 2, 3)
p2 = Point2D(4, -2, -8)

p2.add(p1)

print(p2)
print(p1.distance(p2))


print(p1.distance(p2))