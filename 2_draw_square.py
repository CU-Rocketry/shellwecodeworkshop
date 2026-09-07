#1. Import necessary library
import turtle

#2. Configure turtle
t=turtle.Turtle()
t.speed(2)
t.color("orange")
t.pensize(1.5)

#3. Configure Window
window=turtle.Screen()
window.title("Square Drawing")
window.bgcolor("green")

#4. Sketch 4 (equal) sides
for _ in range(4): #the argument for range is the number or sides of the shape
    t.forward(200) #move turtle forwar d 200 steps
    t.right(90) #turn turtle clockwise (right) 90 degrees (since squares have 90 degree angles)
turtle.done()