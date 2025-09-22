# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
color= input("Please enter a color: ")
painter.color(color)

# ask user for the radius of a circle
radius= int(input("Please enter a radius: "))

# draw a circle with the radius and line color entered by the user
painter.color(color,)
painter.circle(radius, 620, 4)

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()

painter.penup()
painter.forward(100)
painter.pendown()
painter.circle(radius, 190, 4)