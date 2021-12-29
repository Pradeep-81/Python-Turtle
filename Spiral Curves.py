import turtle
design=turtle.Turtle()
design.getscreen(). bgcolor ("black")

design.pensize(2)
design.speed(100)

for i in range(11):
	for  colour in ["red","blue","yellow","green","orange","pink","violet"]:
		design.color(colour)
		design.circle(100)
		design.left(5)
		

design.hideturtle()
turtle.done()