import turtle
from random import randint

#небо
screen = turtle.Screen()
screen.bgcolor("lightblue") 

turtle.speed(0)

#пляж
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.forward(600)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.end_fill()

#вода
turtle.penup()
turtle.goto(-300 , 100)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.forward(600)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.end_fill()

#волны
turtle.penup()
turtle.goto(-270 , -15)
turtle.color('blue')
for i in range(11):
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('blue')
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-270 + 60*i, -15)

turtle.color('black')


#ствол пальмы
turtle.penup()
turtle.goto(100, -50)  
turtle.pendown()
for i in range(5):
    turtle.penup()
    turtle.goto(100, -50 + i * 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("brown")
    turtle.circle(10)
    turtle.end_fill()


#кокосы(желтые)
turtle.penup()
turtle.goto(110, 25)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(8)
turtle.end_fill()

turtle.penup()
turtle.goto(90, 25) 
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(8)
turtle.end_fill()

turtle.penup()
turtle.goto(100, 15) 
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(8)
turtle.end_fill()

#листья у пальмы
turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("green")
turtle.setheading(15)
turtle.forward(55)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("green")
turtle.setheading(-15) 
turtle.forward(55)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(100, 40)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("green")
turtle.setheading(-165) 
turtle.forward(55)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(95, 35)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("green")
turtle.setheading(-195)  
turtle.forward(55)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.end_fill()





#шезлонг
t = turtle.Turtle()
t.speed(3)
t.pensize(2)
xx = -130
yy = -55
t.penup()
t.goto(xx, yy)
t.pendown()


t.color("red")
t.begin_fill()
t.goto(xx + 50, yy)  
t.goto(xx + 45, yy + 15)  
t.goto(xx + 5, yy + 15)  
t.goto(xx, yy)  
t.end_fill()


t.penup()
t.goto(xx + 5, yy + 15)
t.pendown()
t.color("darkorange")
t.begin_fill()
t.goto(xx + 10, yy + 35)  
t.goto(xx - 5, yy + 35)  
t.goto(xx, yy + 15)  
t.goto(xx + 5, yy + 15)  
t.end_fill()


t.color("brown")
t.pensize(3)


t.penup()
t.goto(xx, yy)
t.pendown()
t.goto(xx - 5, yy - 10)


t.penup()
t.goto(xx + 50, yy)
t.pendown()
t.goto(xx + 55, yy - 10)

t.penup()
t.goto(xx, yy + 15)
t.pendown()
t.goto(xx - 5, yy + 5)


t.penup()
t.goto(xx + 45, yy + 15)
t.pendown()
t.goto(xx + 40, yy + 5)


t.color("black")
t.pensize(1)


for i in range(3):
    y_pos = yy + 5 + i * 3
    t.penup()
    t.goto(xx + 2, y_pos)
    t.pendown()
    t.goto(xx + 43, y_pos)


for i in range(4):
    y_pos = yy + 18 + i * 4
    t.penup()
    t.goto(xx + 1, y_pos)
    t.pendown()
    t.goto(xx + 8, y_pos)



#зонт

umbrella_x = xx - 25
umbrella_y = yy 


t.pensize(4)
t.color("brown")
t.penup()
t.goto(umbrella_x + 2, umbrella_y)
t.pendown()
t.goto(umbrella_x + 2, umbrella_y + 60)

t.pensize(2)
t.color("red")
t.penup()
t.goto(umbrella_x - 25, umbrella_y + 60)  
t.pendown()


t.begin_fill()
t.setheading(90)  
for i in range(180):  
    t.forward(0.5) 
    t.right(1)      
t.end_fill()

t.color("white")
t.pensize(2)
stripes_angles = [-30, -60, -90, -120, -150]  

for angle in stripes_angles:
    t.penup()
    t.goto(umbrella_x + 3, umbrella_y + 89) 
    t.pendown()
    t.setheading(angle)  
    t.forward(31)        



#черепаха
turtle.shape('turtle')
turtle.penup()
turtle.goto(xx + 18 ,yy + 10)
turtle.setheading(0)
turtle.pendown()
turtle.color('green')







turtle.done() 
