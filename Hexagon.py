import turtle

hexagon=turtle.Turtle ()
hexagon.getscreen(). bgcolor ("pink")
hexagon.color("red","light yellow")
hexagon.begin_fill()

for i in range(6):
	hexagon.fd(100)
	hexagon.left(60)
	
hexagon.end_fill()

turtle.done()