import turtle
import math

p=turtle.Turtle()
p.color("pink","#994444")
p.speed(100)
p.begin_fill()
for i in range(100):
	p.forward(math.sqrt(i)*10)
	p.left(45)
p.end_fill()
	
	
turtle.done()
	