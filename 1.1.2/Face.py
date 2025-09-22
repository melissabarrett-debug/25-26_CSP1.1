# import the turtle module
import turtle as trtl

painter= trtl.Turtle()


painter.circle(50)
painter.penup()
painter.forward(200)
painter.pendown()
painter.circle(50)
painter.pendown()
painter.right(260)
painter.penup()
painter.forward(45)
painter.pendown()
painter.circle(20)
# left eye
painter.penup()
painter.left(175)
painter.forward(50)
painter.right(90)
painter.forward(200)
painter.right(90)
painter.forward(65)
painter.pendown()
painter.circle(20)
#nose
painter.penup()
painter.right(90)
painter.forward(100)
painter.right(90)
painter.pendown()
painter.forward(70)


wn = trtl.Screen()
wn.mainloop()