# Object Inheritance

# Inheritance allows us to communicate structure about our data and our code, both 
# up to the programmer ourselves, as well as down to the actual program. There exists 
# a hierarchy relationship between classes. It's similar to relationships or 
# categorizations that we know from real life. When you see code in a program being
# written over and over again, you'll want to see if there is opportunity to take
# advantage of simplfying it with object inhertiance.

# Think about vehicles for example. Bikes, cars and trucks are vehicles. Trucks,
# vans, and sports cars are vehicles. We could implement a vehicle class in Python, 
# which might have methods like accelerate and brake. Cars, Buses and Trucks and 
# Bikes can be implemented as subclasses which will inherit these methods from 
# vehicle.

# Another way to look at object inheritance is to think of creating a parent class 
# called shape, with child classes such as squares, triangles and cirlces. We 
# create a class with methods that will be passed down to the child classes and 
# make our code. Let's look at some code on how this can work.

# Here are a few classes defined for different shapes:
import math

class Square:
	def __init__(self):
		self.color = ""
		self.sides = 4
		self.size = 0

class Rectangle:
	def __init__(self):
		self.color = ""
		self.sides = 4
		self.length = 0
		self.width = 0

class Triangle:
	def __init__(self):
		self.color = ""
		self.sides = 3
		self.length = 0
		self.length = 0
		self.length = 0


# While this code will work, it's very repdative and lacks the use of object 
# inhertiance. If I needed to make an update to any of the colors or lengths, I
# I would have to go through line by line and possibly make a mistake along the 
# way. You may also notice that some of the methods called are used in the different
# classes. So let's simplify this and demonstrate object inhertiance.
import math

class Shape():
	def __init__(self):
		self.color = ""
		self.sides = 0

class Quadrilateral(Shape):
	def __init__(self, w, l, c):
		self.sides = 4
		self.width = w
		self.length = l
		self.color = c

class Triangle(Shape):
	def __init__(self, s1, s2, s3, c):
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.color = c

class Circle(Shape):
	def __init__(self, r, c):
		Shape.__init__(self)
		self.radius = r
		self.color = c

class Square(Quadrilateral):
	def __init__(self, w, c):
		Quadrilateral.__init__(self, w, w, c)

class Rectangle(Quadrilateral):
	def __init__(self, w, l, c):
		Quadrilateral.__init__(self, w, l, c)

class Equilateral(Triangle):
	def __init__(self, s1, s2, s3, c):
		Triangle.__init__(self, s1, s2, s3, c)

class Isosceles(Triangle):
	def __init__(self, s1, s2, s3, c):
		Triangle.__init__(self, s1, s2, s3, c)

sq1 = Square(5, "Green")
e1 = Equilateral(3, 3, 3, "Orange")
circle1 = Circle(10, "Blue")

print("Square Size =", sq1.width, "x", sq1.sides, sq1.color)
print("Equilateral Size =", e1.s1, "x", e1.s2, "x", e1.s3, e1.color)
print("Circle Radius =", circle1.radius, circle1.color)

# Here I have created a parent class "Shape", given birth to three children named
# "Quadrilateral", "Triangle" and "Circle". Now I can create many different shapes 
# (child classes) within those child classes and use exisitng methods from higher 
# up the chain without having to write a bunch of duplicate code. There are many 
# ways you could write this and simplify it. But I hope this helps you understand
# the concept of inheritance better and use it in you future programs! 
