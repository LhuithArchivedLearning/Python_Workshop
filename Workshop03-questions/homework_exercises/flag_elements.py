#---------------------------------------------------------------------
#
# Flag elements - A module containing two reusable functions
#
# This module defines a function to draw a stripe and
# another function to draw a star.  You can import these
# functions into another program and call them to create
# flags containing these two elements.
#
# Note that the functions are "parameterised" so that the
# items they draw can appear in different sizes and colours,
# without the need to rewrite the code.


# Import the graphics functions required
from turtle import *


#---------------------------------------------------------------------
# Function to draw a five-pointed star of the given size
# and colour starting at the top point of the star.  The "height"
# is the vertical size of the star, in pixels.
#
def star(height, colour):

    left_angle = 72 # degrees, for left turns
    right_angle = 144  # degrees, for right turns
    line_size = height * 0.409 # length of each of the ten lines

    # Draw a five-pointed, filled star as five concave segments
    setheading(-left_angle) # pointing down from top point
    color(colour) # use the given fill colour
    pendown()
    begin_fill()
    segment_numbers = range(5)
    for seg_no in segment_numbers: # draw each of the segments
      forward(line_size)
      left(left_angle)
      forward(line_size)
      right(right_angle)
    end_fill()
    penup()


#---------------------------------------------------------------------
# Function to draw a stripe (rectangle) of the given width,
# height and colour starting at the top left-hand corner.
#
def stripe(width, height, colour):

    # Draw a filled rectangle
    setheading(0) # face east
    color(colour) # use the given colour
    pendown()
    begin_fill()
    forward(width) # top edge
    right(90)
    forward(height) # right-hand edge
    right(90)
    forward(width) # bottom edge
    right(90)
    forward(height) # left-hand edge
    end_fill()
    penup()
