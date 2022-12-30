import turtle
s = turtle.Screen() 
# variable for the turtle screen
t = turtle.Turtle() 
# variable for the turtle
s.bgcolor("cadetblue3") # background colour
t.hideturtle() 
# to hide the turtle
t.speed(0) 
# to control the drawing speed
t.color("black")
t.penup()
t.begin_fill() 
# start the colour filling
t.fillcolor("white")
t.goto(-250,-150)
t.pendown()
t.forward(500)
t.setheading(90) 
#to rotate the turtle head
t.forward(300) 
# pixels in y axis
t.setheading(180)
t.forward(500) 
# pixels in x axis
t.setheading(270)
t.forward(300)
t.end_fill() 
# end of colour filling
t.penup()
t.goto(0,0)
t.pendown()
t.color("black")
t.penup()
t.goto(-80,-10)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.circle(80) 
# circle radius
t.end_fill()
s.exitonclick()