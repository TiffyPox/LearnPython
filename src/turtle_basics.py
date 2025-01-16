import turtle

timmy = turtle.Turtle()

turtle.bgcolor('pink') # turn background black 

# get ready to draw 36 circles 
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

# mouth
timmy.goto(0, -20)
timmy.begin_fill()
timmy.color('black')
timmy.circle(10)
timmy.end_fill()

# nose
timmy.penup() 
timmy.goto(-10, 70) # move to window position 
timmy.pendown() 
timmy.begin_fill() # start filling window color 
timmy.color('black') 
for i in range(4): 
    timmy.forward(20) 
    timmy.left(120) 
timmy.end_fill() # end filling window color 

# hide turtle to finish the drawing 
timmy.hideturtle()

turtle.done()