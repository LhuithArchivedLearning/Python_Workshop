# Concentric circles
#
# As an exercise in using the Turtle package and lists you are
# required to draw three concentric circles on the screen.
# These circles must be centred in the drawing window.  The
# radii of the circles are given to you as a list of numbers.
# You must develop your program so that it is easy to change
# the sizes of the three circles by changing the numbers in
# the list.
#
# NB: We need unfilled circles, so you can't use Turtle's
# "dot" function for this purpose.  Also, you must ensure that
# lines are not drawn between or connecting the circles.
#
# Recall that Turtle's "circle" function does not draw a
# circle at the current location.  Instead it causes the turtle
# to walk in a circle, which means that the circle is actually
# drawn in a position such that the turtle (cursor) is on its
# perimeter.
#
# The basic strategy to use for drawing each circle is:
#
# 1) Lift up the pen
# 2) Go to the centre of the screen ("home")
# 3) Move to a position on the intended circle's perimeter
# 4) Set the turtle's heading so that when it walks
#    in a circle it will create a circle centred on
#    the screen
# 5) Put the pen down
# 6) Walk in a circle
# 
# Importantly, the radius of each circle is given in
# a list, so your code must refer to the appropriate
# list element to control the size of each circle.
# If the numbers in the list are changed, your code
# should draw circles of a different size.


# Import the turtle library
from turtle import *

# Create the drawing canvas and give it a name
setup()
title('Concentric Circles')

# Define the radii of the three circles, in pixels
#radii = [30, 60, 90]

# Here are some other values you can try
# by uncommenting one of these lines:
# radii = [5, 30, 60]
# radii = [15, 25, 35]
radii = [70, 80, 90]

for index in range(len(radii)):
    penup();
    home();
    
    setheading(270);
    forward(radii[index]);
    setheading(0);
    
    pendown();
    circle(radii[index]);




# Exit gracefully
hideturtle()
done()
