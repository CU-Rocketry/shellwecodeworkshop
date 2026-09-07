import turtle
import math
import random

#1. Configure window
window=turtle.Screen()
window.bgcolor("black")
window.title("Mathematical Spirographs")

#2. Configure turtle
t=turtle.Turtle()
t.speed(0) #fastest speed
t.width(1.5)

#3. Hypotrochoid Function
def sketch_hypotrochoid(R,r,d):
    color=(random.random(),random.random(),random.random())
    t.color(color)
    t.width(1.5)

    gcd=math.gcd(int(R),int(r))
    max_angle=2*math.pi*(r//gcd)

    step=0.02
    angle=0.0

    t.penup()#stop drawing
    x=(R-r)*math.cos(angle)+d*math.cos((R-r)*angle/r)
    y=(R-r)*math.sin(angle)-d*math.sin((R-r)*angle/r)
    t.goto(x,y) #go to position
    t.pendown()#start drawing

    while angle <=max_angle:
        x=(R-r)*math.cos(angle)+d*math.cos((R-r)*angle/r)
        y=(R-r)*math.sin(angle)+d*math.sin((R-r)*angle/r)
        t.goto(x,y)
        angle+=step
def sketch_epitrochoid(R2,r2,d2):
    color=(random.random(),random.random(),random.random())
    t.color(color)
    t.width(2)
    gcd2=math.gcd(int(R2),int(r2))
    max_angle2=2*math.pi*(r2//gcd2)
    step=0.02
    angle=0.0
    t.penup()
    x=(R2+r2)*math.cos(angle)-d2*math.cos((R2+r2)*angle/r2)
    y=(R2+r2)*math.sin(angle)-d2*math.sin((R2+r2)*angle/r2)
    t.goto(x,y)
    t.pendown()
    while angle <= max_angle2:
        x=(R2+r2)*math.cos(angle)-d2*math.cos((R2+r2)*angle/r2)
        y=(R2+r2)*math.sin(angle)-d2*math.sin((R2+r2)*angle/r2)
        t.goto(x,y)
        angle+=step
        
#Draw hypotrochoid (inside rolling)
sketch_hypotrochoid(R=random.randint(150,300),r=random.randint(90,170),d=random.randint(70,115))

#Draw epitrochoid (outside rolling)
sketch_epitrochoid(R2=random.randint(80,120),r2=random.randint(50,80),d2=random.randint(60,65))

window.mainloop()
