#---------------------------------------------------------
#
# For-each practice
#
# The most commonly used kind of repetition for our purposes
# is the FOR-EACH loop which does some action for every
# value in a list.  The actions can be made distinct by
# referring to the particular value.
#
# As practice in creating such loops, this exercise simply
# asks you to draw some patterns using Turtle graphics and
# the values in some lists by following simple instructions.
#

# Set up a drawing canvas
from turtle import *
setup()
title("Practice with for-each loops")
bgcolor('black')

# Set up some drawing characteristics
speed('fastest')
color('white')
width(2)

# The three lists to use are as follows
colours = ['red', 'green', 'blue', 'yellow', 'white', 'orange',
           'aqua', 'olive', 'misty rose', 'salmon', 'spring green',
           'fuchsia', 'deep sky blue', 'silver', 'aquamarine',
           'orange red', 'seashell', 'chocolate', 'light steel blue',
           'tomato', 'chartreuse', 'bisque', 'dark orchid',
           'powder blue', 'gainsboro']
radii = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71,
         76, 81, 86, 91, 96, 101, 106, 111, 116, 121, 126, 131,
         136, 141, 146]
coordinates = [[85, 140], [0, 280], [-85, 140], [0, 0],
               [-165, 0], [-254, -150], [-80, -150], [0, 0],
               [165, 0], [254, -150], [80, -150], [0, 0]]

# Develop your code below by following the instructions.  Each step
# is independent of its predecessors so when you finish one step
# comment it out and start on the next.

# Step 1: For each of the colours above, set the pen colour accordingly
# add draw a dot of size 50.  So that the dots don't all appear on
# top of one another, move forward 15 pixels after drawing each one.

for col in colours :
    color(col);
    dot(50);
    forward(15);

penup();
home();

# Step 2: Comment out your Step 1 code. Now, with the pen down,
# walk in a circle for each of the radii (plural of radius) in the
# list above to produce a tunnel-like pattern.  To make your
# pattern more interesting, turn the turtle left by 12 degrees
# after drawing each circle.  This will create a pattern like
# a snail's shell.

for rad in radii:
    pendown();
    left(12);
    circle(rad);
    penup();

# Step 3: Comment out your code for Steps 1 and 2 above.  Again
# with the pen down, tell the turtle to go to each of the
# coordinates in the list above.  This should produce a pattern
# reminiscent of a well-known car logo.  Make it appear even
# more realistic by making the pen colour red and filling in
# the image.

for coord in coordinates :
    pendown();
    goto(coord);

# Release the drawing canvas
hideturtle()
done()
