#---------------------------------------------------------------
#
# Caged Turtle
#
# As a trivial graphical example of the use of exception
# handling, consider the following drawing tool that allows
# users to move the "turtle" cursor around the screen by
# clicking on the drawing canvas.  The initial version allows
# you to move the turtle anywhere.
#
# Your job is to modify this program so that an attempt to move
# the turtle outside of a prescribed square area is not allowed,
# effectively confining the turtle to stay within the square.
#
# To do this you need to (1) modify the move_turtle function to
# raise an exception if the user's selected coordinate is
# outside the square, and (2) modify the new_position function
# to print an error message if an attempt is made to move the
# turtle outside the square.
#


# Import the turtle graphics and random number functions
from turtle import *
from random import choice

# Define the size of the square caging the turtle
square_side = 300 # pixels

# Define the colours the turtle can have
colours = ['red', 'green', 'blue', 'orange', 'brown', 'purple', 'yellow']


#-----
# Version 1: Moves the turtle to the given coordinates.
#
# Version 2: Modify this function so that it raises an
# exception if the chosen coordinate is outside the square.
# The turtle should not be moved in this case.  Python statement
# "raise Exception" will raise a generic exception.
#
def move_turtle(x_coord, y_coord):
    goto(x_coord, y_coord)

    
#-----
# Version 1: When the user clicks the mouse in the drawing window
# it changes the turtle's colour randomly and then calls move_turtle.
#
# Version 2: Modify this function so that if an exception is raised by
# the move_turtle function an error message is printed to the shell
# window telling the user that they have clicked on an illegal
# coordinate.
#
def new_position(x_coord, y_coord):
    color(choice(colours))
    move_turtle(x_coord, y_coord)


#-----
# The main program which binds mouse clicks to the new_position
# function above.
#

# Name the window and setup the "turtle"
title('Caged Turtle')
shape('turtle')

# Draw a square intended to confine the turtle
penup()
goto(square_side // 2, square_side // 2) # top-right corner
setheading(180) # west
pendown()
for side in ['top', 'left', 'bottom', 'right']:
    forward(square_side)
    left(90)
penup()
home()

# Get ready for user inputs
pendown()
onscreenclick(new_position)

# Allow the drawing window to be closed gracefully
done() 

