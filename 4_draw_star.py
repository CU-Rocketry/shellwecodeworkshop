#1. Import necessary library
import turtle

#2. Configure turtle
t=turtle.Turtle()
t.penup()
t.goto(-125,0)
t.pendown()
t.speed(3)
t.color("orange","yellow") #(pen color, fill color)
t.pensize(3) #width of pen

#3. Configure Window
window=turtle.Screen()
window.title("Star Drawing")
window.bgcolor("Black")

#3. Sketch Star (Make sure to include/specify angles)
for _ in range(5):
    t.forward(300)
    t.right(144) #turn turtle clockwise 144 degrees to create a star shape

turtle.done() #keep window open after turtle stops moving