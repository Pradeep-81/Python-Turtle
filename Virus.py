import turtle
import random
c=turtle.Turtle()
c.getscreen(). bgcolor ("black")
c.color("light green")
c.speed(0)
a=0
b=0

while True:
	c.fd(a)
	c.right(b)
	a+=3
	b+=1
	
	if b==200:
		break
	
	
	
turtle.done()