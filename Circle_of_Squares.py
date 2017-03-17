# Drawing a circle out of squares 0_0
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
	shelly.speed(3)
	draw_square(shelly)

	for i in range(1, 37):
		draw_square(shelly)
		shelly.right(10)
	
	window.exitonclick()

draw_art()