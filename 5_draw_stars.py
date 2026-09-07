#1. Import necessary libraries
import turtle
import random

#2. Configure multiple turtles
t=turtle.Turtle()
t.penup()
t.goto(0,0)
t.pendown()
t.speed(3)
t.color("orange","yellow") #(pen color, fill color)
t.pensize(3) #width of pen

t.penup() #stop turtle from drawing before it gets to specified position
#randomly iterate through a specified interval for both the x and y coordinates
x=random.randint(-200,200)
y=random.randint(-200,200) 
t.goto(x,y) #send the turtle to these coordinates
t.pendown() #start drawing again 

#repeat previous steps for second turtle
t2=turtle.Turtle()
t.penup()
t.goto(-100,-125)
t.pendown()
t2.speed(1)
t2.color("blue","purple")
t2.pensize(1.5)
t2.penup()

x2=random.randint(-400,400)
y2=random.randint(-400,400)
t2.goto(x2,y2)
t2.pendown()

#3. Configure Window
window=turtle.Screen()
window.title("Star Drawing")
window.bgcolor("Black")

#3. Sketch First Star 
for _ in range(5):
    t.forward(300)
    t.right(144) #turn turtle clockwise 144 degrees to create a star shape

#4. Sketch Second Star
for _ in range(5):
    t2.forward(100)
    t2.right(144) #turn turtle clockwise 144 degrees to create a star shape

turtle.done() #keep window open after turtle stops moving