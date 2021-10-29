import turtle
import os

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Projection of Points")

x_pen=turtle.Turtle()
x_pen.speed(0)
x_pen.color('white')
x_pen.penup()
x_pen.setposition(-360,-13)
x_pen.write('X',font='Arial')
x_pen.hideturtle()

y_pen=turtle.Turtle()
y_pen.speed(0)
y_pen.color('white')
y_pen.penup()
y_pen.setposition(350,-13)
y_pen.write('Y',font='Arial')
y_pen.hideturtle()

xy_line=turtle.Turtle()
xy_line.speed(0)
xy_line.color("white")
xy_line.penup()
xy_line.setposition(-350,0)
xy_line.pendown()
xy_line.fd(700)
xy_line.hideturtle()

#input
a=input("Enter whether point is 'in front' of VP or 'below' VP: ")
a2=int(input("Enter distance of point from VP: "))

b=input("Enter whether point is 'above' HP or 'below' HP: ")
b2=int(input("Enter distance of point from HP: "))

if a==('in front') and b==('above'):
    pen1=turtle.Turtle()
    pen1.color=('white')
    pen1.penup()
    pen1.setposition(0,0)
    pen1.pendown()
    pen1.lt(90)
    pen1.fd(b2)
    pen1.lt(180)
    pen1.fd(b2+a2)
    pen1.hideturtle()
else:
    print("Error")
    

delay=input("Press enter to end.")
