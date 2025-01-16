# Make a house using Turtle
import turtle 

# Create a screen object
screen = turtle.Screen()

# Set the screen size to 800x600 pixels
screen.setup(width = 800, height = 600)

turtle.bgcolor('sky blue') 
timmy = turtle.Turtle() 

# Make the first big square for house 
timmy.begin_fill() # start fill of color 
timmy.color('magenta') 
for i in range(4): 
    timmy.forward(100) 
    timmy.left(90) 
timmy.end_fill() # end fill of color 
timmy.penup() 
timmy.goto(-20,100) # move turtle to next area 
timmy.pendown() 

# Make a red triangle roof 
timmy.begin_fill() # start fill for roof 
timmy.color('cyan') 
timmy.left(60) 
timmy.forward(140)
timmy.right(120) 
timmy.forward(140) 
timmy.right(120) 
timmy.forward(140) 
timmy.end_fill() # end fill of color for roof 

# Make a window 
timmy.penup() 
timmy.goto(35,80) # move to window position 
timmy.pendown() 
timmy.begin_fill() # start filling window color 
timmy.color('yellow') 
for i in range(4): 
    timmy.forward(20) 
    timmy.left(90) 
timmy.end_fill() # end filling window color 

# Second window
timmy.penup() 
timmy.goto(85,80) # move to window position 
timmy.pendown() 
timmy.begin_fill() # start filling window color 
timmy.color('yellow') 
for i in range(4): 
    timmy.forward(20) 
    timmy.left(90) 
timmy.end_fill() # end filling window color 

# Door
timmy.penup() 
timmy.goto(60, 20) # move to window position 
timmy.pendown() 
timmy.begin_fill() # start filling window color 
timmy.color('brown') 
for i in range(4): 
    timmy.forward(20) 
    timmy.left(90) 
timmy.end_fill() # end filling window color 

# Door
timmy.penup() 
timmy.goto(60, 40) # move to window position 
timmy.pendown() 
timmy.begin_fill() # start filling window color 
timmy.color('brown') 
for i in range(4): 
    timmy.forward(20) 
    timmy.left(90) 
timmy.end_fill() # end filling window color 

# Bush
timmy.penup()
timmy.goto(100, 30) # move to window position 
timmy.begin_fill() 
timmy.color('green') 
timmy.circle(20)
timmy.end_fill()

# Sun
timmy.penup()
timmy.goto(-80, 280) # move to window position 
timmy.begin_fill() 
timmy.color('yellow') 
timmy.circle(20)
timmy.end_fill()

# Grass
timmy.penup() 
timmy.goto(-400, 0) # move to window position 
timmy.pendown() 
timmy.begin_fill() # start filling window color 
timmy.color('green') 
for i in range(4):
    timmy.forward(-800) 
    timmy.left(-90) 
timmy.end_fill() # end filling window color 

# Person head
timmy.penup()
timmy.goto(-60, 50)
timmy.begin_fill()
timmy.color('black')
timmy.circle(10)
timmy.end_fill()

# Person arm
timmy.penup()
timmy.goto(-40, 30)
timmy.begin_fill()
timmy.color('black')
for i in range(4):
    timmy.forward(10)
    timmy.left(90)
timmy.end_fill()

# Person second arm
timmy.penup()
timmy.goto(-70, 30)
timmy.begin_fill()
timmy.color('black')
for i in range(4):
    timmy.forward(10)
    timmy.left(90)
timmy.end_fill()

# Person body
timmy.penup()
timmy.goto(-50, 30)
timmy.begin_fill()
timmy.color('black')
for i in range(4):
    timmy.forward(20)
    timmy.left(90)
timmy.end_fill()

# Person body
timmy.penup()
timmy.goto(-50, 10)
timmy.begin_fill()
timmy.color('black')
for i in range(4):
    timmy.forward(20)
    timmy.left(90)
timmy.end_fill()

# Hide the turtle when done 
timmy.hideturtle()

# Keep program open when finished drawing
turtle.done()
