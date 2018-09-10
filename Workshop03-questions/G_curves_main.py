# "Curves" main program
#
# As a simple exercise in creating your own Python module, here
# you will develop a single program in two separate files.  In
# this file you will develop a "main" program, and in the
# other "curves" file you will develop a function which is
# "imported" into this one.
#
# Begin by completing the instructions in the "curves_module"
# file to create the function to be imported.  Then follow
# the instructions below to write the main program that calls
# this function.
#
# Having done this, your program should draw a complex shape
# on the screen.  Experiment to get different patterns by
# changing the constant integer values in both the main program
# below and the function definition in the other file.
#

# Import the standard Turtle graphics functions
from turtle import *

# Import the function you define in your own module
from G_curves_module import *

# Set up the drawing canvas
setup(800, 700)
title('Curves')
penup()
speed('fast')

# Set some values for the drawing pen.  (You
# can change these to get different effects.)
width(4)
pencolor('red')
pendown()

# Develop code here as follows:
#
# 1. Initialise an "angle" variable to zero
# 2. For each of 18 steps:
#    a. Call the function in your module to draw a
#       single arc, giving it the "angle" variable
#       and a fixed radius of 250 as arguments
#    b. Add 20 degrees to the "angle" variable
pass

# Tidy up           
hideturtle()
done()
