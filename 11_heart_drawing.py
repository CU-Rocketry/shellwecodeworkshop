import turtle

#Configure Window
window=turtle.Screen()
window.title("Heart Drawing")
window.bgcolor("black")

#Configure turtle:
t=turtle.Turtle()
t.penup()
t.goto(0,-150)
t.pendown()
t.color("magenta")
t.fillcolor("pink")
t.pensize(2)
t.speed(2)

t.begin_fill() #start filling the heart with color

#Sketch the left curve of the heart
t.left(140) #angle turtle is positioned in, in degrees counter-clockwise
t.forward(224) #turtle steps forward __ number of steps

#Sketch left semi-circle
for _ in range(200):
    t.right(1)
    t.forward(2)

#Turn around for the right side of the heart:
t.left(120)

#Sketch the right semi-circle
for _ in range(200):
    t.right(1)
    t.forward(2)

#Wrap up the drawing
t.forward(224)
t.end_fill()

#Hide turtle but keep window
t.hideturtle()
turtle.done()
