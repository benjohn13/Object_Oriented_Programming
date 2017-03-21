# Event Handling
import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling Keypresses")      # Change the window title
wn.bgcolor("green")                  # Set the background color
shelly = turtle.Turtle()             

def h1():
   shelly.forward(30)

def h2():
   shelly.left(45)

def h3():
   shelly.right(45)

def h4():
    wn.bye()                     

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

# Now we need to tell the window to start listening for events,
# if any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
