
#1. import necessary libraries 
import turtle as t
import math
import time

#2. Configure window & turtle
window=t.Screen()
window.bgcolor("light blue") #set background color
window.title("A Turtle's Stroll")

#3. Make Turtle
t.Turtle() #make turtle
t.shape("turtle") #change shape of turtle (default shape is an arrow)
t.color("green") #set turtle color
t.speed(1) #set drawing speed: 1=slow,10=fast,0=fastest (speed range: 0-10)
t.shapesize(1.5,1.5,1) #change size; turtle.shapesize(width, length, outline)

#4. Move Turtle
#move turtle: forward or backward
t.forward(100) #move turtle forward 100 steps
#time.sleep(3) #pauses entire program
t.backward(30) 

#rotate turtle: left or right in degrees
#time.sleep(4)
t.left(40) #turn turtle 40 degrees counterclockwise
time.sleep(3)
t.right(25) #turn turtle 25 degrees clockwise

#5. Keep window open so you can see your animation/drawing!
t.done()  