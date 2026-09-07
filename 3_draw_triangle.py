#1. Import necessary library
import turtle


#2. Configure turtle
t=turtle.Turtle()
t.penup() #lift pen so it doesn't draw while moving
t.goto(-125,-200) #specify the coordinates the turtle goes to
t.pendown() #turtle will now start drawing

t.speed(3)
t.color("yellow")
t.begin_fill() #start filling shape

#3. Configure Window
window=turtle.Screen()
window.title("Triangle Drawing")
window.bgcolor("blue")

#4. Sketch Triangle
for _ in range(3):
    t.forward(400)
    t.left(120) #Turn turtle counter-clockwise (left) 120 degrees (because equilateral triangles have exterior angles of 120 degrees)

t.end_fill() #stop filling shape
turtle.done() #keep window open even after turtle stops drawing