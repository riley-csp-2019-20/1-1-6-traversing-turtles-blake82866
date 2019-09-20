#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    color = turtle_colors.pop()
    t.fillcolor(color)
    t.begin_fill()
    t.pencolor(color)
    t.end_fill()
    my_turtles.append(t)

# were the turtle starts
startx = 0
starty = 0

# make the turtle move
direction = 360
for t in my_turtles:
    t.penup()
    t.setheading(direction)
    t.goto(startx, starty) 
    t.pendown()
    t.right(20)      
    t.forward(25)

# make the next turtle move from were the last did
    startx = t.xcor()
    starty = t.ycor()

# make the turtle face the same direction as the last
    direction = t.heading()

wn = trtl.Screen()
wn.mainloop()