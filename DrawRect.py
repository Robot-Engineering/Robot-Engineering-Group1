class DrawRect:
    def rect(x_start,y_start,length,width,degree):
        import turtle
        turtle.reset()
        turtle.penup()
        turtle.goto(x_start,y_start)
        turtle.pendown()
        turtle.left(degree)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.done()
