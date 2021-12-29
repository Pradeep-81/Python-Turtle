import turtle
design=turtle.Turtle()
design.getscreen(). bgcolor ("black")

design.pensize(2)
design.speed(100)

for i in range(11):
	for  colour in ["red","blue","yellow","green","orange","pink","violet"]:
		design.color(colour)
		for j in range(4):
			design.fd(100)
			design.left(90)
			
			
		design.left(5)
		

design.hideturtle()
turtle.done()