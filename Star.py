import turtle

star=turtle.Turtle()

star.getscreen().bgcolor("light green")
star.speed(10)
star.color("black","yellow")

star. begin_fill()
for i in range(5):
	star.forward (100)
	star.left(216)
star.end_fill()
	
turtle.done()