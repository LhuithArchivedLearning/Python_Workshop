#---------------------------------------------------------
#
# Linear Curve
#
# Define a function called "linear_curve" that uses Turtle
# graphics to draw a linear curve by drawing straight lines
# between increasing/decreasing points on the x-axis to
# decreasing/increasing points on the y-axis.  Part of the
# function has been given below, but not the crucial loop
# that draws each line.
#
# See the enclosed file "linear_curve.pdf" for an example
# of the expected output.
#
# Extra challenge:  Extend your function so that it
# draws a "full circle" linear curve.
#

# Import functions required
from turtle import *


#---------------------------------------------------------
#
# Suggested solution strategy to complete the linear_curve function:
#
# 1. For each line to be drawn:
#    a. Calculate the distance D the line must be offset from the corner
#    b. Draw a line from one axis to the next that is offset on
#       the y-axis by D and on the x-axis by the line length minus D
#

# A function to draw a linear curve
#
def linear_curve():
 
    # Set the length of each line
    line_length = 300

    # Set the separation between successive lines on the axes
    line_sep = 10

    # Calculate how many lines must be drawn
    num_lines = line_length // line_sep

    ##### COMPLETE THE linear_curve FUNCTION HERE

    
#---------------------------------------------------------
# Main program to call your linear_curve function
#
setup()
title("Linear curve")
speed('fastest')
linear_curve()
hideturtle()
done()
