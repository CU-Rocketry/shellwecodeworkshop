#Parametric Equations:
# x=16sin^3(t)
#y=13cos(t)-5cos(2t)-2cos(3t)-cos(4t)
import math
import turtle

#Configure Window
window=turtle.Screen()
window.title("Drawing a Heart with Parametric Equations")
window.bgcolor("black")

#Configure turtle
t=turtle.Turtle()
t.color("pink")
t.speed(1)
t.pensize(2)
t.begin_fill()


#Loop through parameter, t, from 0 to 2*pi
steps=600
for i in range(steps): #indexing
    angle=i*(2*math.pi/steps) #convert step index to radians (somewhere within the range of 0 to 2*pi)
    x=16*math.sin(angle)**3 # The double asterisk (**) indicates an exponent
    y=(13*math.cos(angle)-5*math.cos(2*angle)-2*math.cos(3*angle)-math.cos(4*angle))

    #scale coordinates so heart is bigger
    scale=15
    t.goto(x*scale,y*scale)

t.end_fill()
t.hideturtle()
turtle.done()