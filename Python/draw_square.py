# I am going to write a program that can draw a square. I will define a function 
# as "draw_square" and import "turtle" from the Python Standard Library. Now the
# syntax "shelly = turtle.Turtle()" may a look a little weird if you are new to
# "classes", but it's how we grab a turtle from the library.

# Let's look at it this way:
# In the Python Standard Library, there is a file called "turtle" (lowercase).
# Inside that file is "Class" called "Turtle" (uppercase).
# So now we write the code "turtle.Turtle()", which calls the "turtle" file we 
# imported, which calls a "class" inside the file, which calls a function named 
# "def __init__". This creates new space in memory for a new instance or new
# object of the class "Turtle", which we called "shelly". That's what the line of 
# code below represents: "shelly = turtle.Turtle()".

# Now that I have called upon the class "Turtle" inside the file "turtle", I can 
# use any functions that are available in that class that have already been made. 
# Like, "def forward" or "def right". This is a lot of information to digest, so 
# let's go ahead and write some code to see it in action.

# Here is my drawing turtle and a green window she can draw on
import turtle

def draw_square(some_turtle):
	for i in range(1, 5):
		some_turtle.forward(200)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("green")
	shelly = turtle.Turtle()
	shelly.shape("turtle")
	shelly.speed(1)
	draw_square(shelly)
	
	window.exitonclick()

draw_art()
