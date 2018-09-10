#----------------------------------------------------------------
#
# Cheating at Join-the-Dots
#
# We have seen how functions are typically "called" from within
# the main program (or even from within other functions).  In
# embedded or interactive software, however, functions may be
# called by certain "events" occurring.  In this game we will
# create a function which is called when you click the mouse
# in a Turtle drawing window.
#
# Objective: Recall that in children's join-the-dots puzzles the
# aim is to connect numbered dots by a line.  Here we will create
# a join-the-dots puzzle that we can't lose because the dots are
# placed wherever we move the cursor!
#
# Approach: You are to define a function that will be called
# when a mouse click occurs. This function should move the
# turtle to the location of the click, drawing a line as it
# goes, and draw a dot in the new position.  To do this
# you will need to call Turtle's "onscreenclick" function in
# the main program to "bind" mouse clicks to your dot drawing
# function.  NB: The parameter to "onscreenclick" is the
# name of the function to be called.  The function itself must
# have two parameters, denoting the x and y coordinates at
# which the click occurred.
#
# Extra challenge: As an extension you can also get the
# function to put a number beside each dot, just like a real
# join-the-dots puzzle.  Hint: To make the number advance
# in each step you will need to use a global variable to keep
# track of how many dots have been drawn.  NB: To assign to a
# global variable from within a function you need to declare
# it as "global" inside the function, otherwise
# the Python interpreter will think it's a new local variable.
# See the global_variable demonstration from the lecture for
# an example.
#
# You will need the following turtle graphics functions.
# Look them up in the Python Library Reference manual to see
# what they do and what arguments they need.
#
# * color, goto, dot, etc - for moving and drawing, as usual
# * write - for adding text in the "extra challenge" step
# * onscreenclick - for defining the function to call
#   when the mouse is clicked
#

# Import the turtle graphics functions
from turtle import *


#-----
# Introduce a global variable here to keep track of the dot
# number between function calls for the "extra challenge".

########## PUT YOUR CODE HERE ##########
pass


#-----
# Define a function that will be called whenever the mouse
# is clicked in the drawing window to move to the new
# location and draw the next dot.  Note that this function
# must have two parameters, whose values will be the x and y
# coordinates where the mouse click occurred.

########## PUT YOUR CODE HERE ##########
pass


#-----
# The main program which binds mouse events to the two functions
# above.
#
title("World's Easiest Join-the-Dots Puzzle")

########## ADD CODE AS NEEDED TO THIS MAIN PROGRAM ##########

# onscreenclick(...) # Bind your function to mouse clicks

done() # Allow the drawing window to be closed gracefully

