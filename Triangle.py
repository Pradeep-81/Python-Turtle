import turtle

tri=turtle.Turtle ()
tri.getscreen(). bgcolor ("pink")
tri.color("red","light yellow")
tri.begin_fill()

for i in range(3):
	tri.fd(100)
	tri.left(120)
	
tri.end_fill()

turtle.done()