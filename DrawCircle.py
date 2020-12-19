import turtle
class DrawCircle:
    def Circle(x,y,r,c_1,c_2):
        turtle.reset()
        turtle.penup()
        turtle.goto(x,y+r)
        turtle.pendown()
        turtle.circle(-r)
        turtle.pencolor(c_1)
        turtle.fillcolor(c_2)
        turtle.done()
