import turtle
import random

window=turtle.Screen()
window.bgcolor("black")
window.title("Galaxy of Stars")

t=turtle.Turtle()
t.color("orange","yellow")
t.speed(0) #fastest speed
t.hideturtle()

#Function to sketch a star:
def sketch_star(scale):
    for _ in range(5): 
        t.forward(scale)
        t.right(144)

for _ in range(20): #Sketch multiple random stars!
    x=random.randint(-300,300)
    y=random.randint(-200,200)
    scale=random.randint(10,40)

    #make sure the following is indented inside the loop:
    t.penup()
    t.goto(x,y)
    t.pendown()

    sketch_star(scale) #call function
    
turtle.done()

