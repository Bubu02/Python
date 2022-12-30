import turtle
s = turtle.Screen()
# variable for the turtle screen
t = turtle.Turtle()
# varible for the turtle pointer
t.hideturtle()
# to hide thrturtle pointer
t.speed(10)
# to control the speed of the pen
s.bgcolor("deepskyblue")
# background colour
t.color("black")
# pen colour
t.penup()
# to remove the unwanted line from the initial coordinate to the goto point
t.goto(-250,150)
# to go to a certain coordinate
t.pendown()
# to remove the unwanted line from the initial coordinate to the goto point
t.begin_fill()
# filling of colour
t.fillcolor("orange")
# colour for the filling
t.forward(500)
# to draw a line in pixels
t.setheading(270)
# to rotate the head of the pointer
t.forward(100)
t.setheading(180)
t.forward(500)
t.setheading(90)
t.forward(100)
t.end_fill()
t.goto(-250,50)
t.begin_fill()
t.fillcolor("white")
t.setheading(270)
t.forward(100)
t.setheading(360)
t.forward(500)
t.setheading(90)
t.forward(100)
t.setheading(180)
t.forward(500)
t.end_fill()
t.goto(-250,-50)
t.begin_fill()
t.fillcolor("green")
t.setheading(270)
t.forward(100)
t.setheading(360)
t.forward(500)
t.setheading(90)
t.forward(100)
t.setheading(180)
t.forward(500)
t.end_fill()
t.penup()
t.goto(0,0)
t.pendown()
t.pendown()
t.color("black")
t.penup()
t.goto(0,50)
t.pendown()
t.pensize(3)
t.pencolor("blue4")
t.circle(50)
# radius of the circle
t.goto(0,0)
for i in range (24):
    # applying for loop to dwar 24 lines in The Ashoka Chakra
    t.right(360/24)
    t.forward(50)
    t.goto(0,0) 
s.exitonclick()