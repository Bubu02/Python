import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor ("black")
turtle.speed(0)
t.hideturtle()
color = ["blue","red","yellow","green","blue"]

for i in range(120):
    for c in color :
        turtle.color(c)
        turtle.circle(200-i, 100)
        turtle.lt(90)
        turtle.circle(200-i, 100)
        turtle.rt(60)
        turtle.end_fill()

turtle.mainloop()
s.exitonclick()
