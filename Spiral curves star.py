import turtle

c=turtle.Turtle()
c.getscreen(). bgcolor ("black")
c.color("light green","sky blue")
c.pensize(2)
c.speed(0)
c.begin_fill()

for j in range(80):
	for i in range(5):
		c.fd(250)
		c.left(216)
	
	c.left(5)

c.end_fill()
	
	
turtle.done()