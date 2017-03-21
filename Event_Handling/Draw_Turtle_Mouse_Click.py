# Event Handling
import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Handling Mouse Clicks")
wn.bgcolor("Green")

shelly = turtle.Turtle()
shelly.pensize(3)
shelly.shape("circle")

def h1(x, y):
   shelly.goto(x, y)

wn.onclick(h1)
wn.mainloop()