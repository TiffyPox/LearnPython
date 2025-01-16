import turtle

# Week 11 of University
# Task: Draw a frog using turtle

timmy = turtle.Turtle()

turtle.bgcolor('pink') # Turn background pink 

timmy.penup() 
timmy.color('white')

# Face
timmy.goto(0, -100)
timmy.begin_fill()
timmy.color('green')
timmy.circle(200)
timmy.end_fill()

# One eye
timmy.goto(-30,100) 
timmy.begin_fill() 
timmy.color('white') 
timmy.circle(30) 
timmy.end_fill() 
timmy.begin_fill() 
timmy.color('black') 
timmy.circle(20)
timmy.end_fill()

# Second eye
timmy.goto(30,100) 
timmy.begin_fill() 
timmy.color('white') 
timmy.circle(30) 
timmy.end_fill() 
timmy.begin_fill() 
timmy.color('black') 
timmy.circle(20)
timmy.end_fill()

# Mouth
timmy.goto(0, -20)
timmy.begin_fill()
timmy.color('black')
timmy.circle(10)
timmy.end_fill()

# Nose
timmy.penup() 
timmy.goto(-10, 70) 
timmy.pendown() 
timmy.begin_fill() 
timmy.color('black') 
for i in range(4): 
    timmy.forward(20) 
    timmy.left(120) 
timmy.end_fill() 

# Hide turtle to finish the drawing 
timmy.hideturtle()

turtle.done()