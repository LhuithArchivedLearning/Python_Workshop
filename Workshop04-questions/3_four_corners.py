###################################################################
#
# Four corners
#
# As a graphics program that involves making decisions, this
# exercise extends the demonstration program from the lecture
# with colour.
#
# The program below is a minor variant of the "jump to the left"
# Turtle graphics demonstration from Lecture 4.  The
# main difference is that a thick line is drawn as the cursor
# moves around the screen.
#
# Your task is to modify the program so that the line changes
# colour depending on what quadrant of the screen the cursor is in.
# We assume the drawing surface is divided into four segments as
# follows, with coordinate (0, 0) at the centre.
#
#                   |
#    Quadrant 1     |    Quadrant 2
#                   |
#                   |
#    ---------------+---------------
#                   |
#    Quadrant 3     |    Quadrant 4
#                   |
#                   |
#
# Select a colour for each quadrant and extend the code below
# so that the line being drawn changes colour depending on the
# quadrant.  The result will be an abstract painting with
# four differently coloured squares.
#
# Hint: The cursor's current coordinates are returned by
# Turtle's "xcor" and "ycor" methods.
#


# Import the necessary pre-defined functions
from turtle import *
from random import randint
Q1 = 'red';
Q2 = 'purple';
Q3 = 'yellow';
Q4 = 'blue';

########################################
# This Boolean-valued function returns True if the turtle is near
# any of the drawing window's four edges 
#
border = 75 # how close we must get to be considered "near" the edge
max_x_coord = (window_width() // 2) - border # how far we can go left or right
max_y_coord = (window_height() // 2) - border # how far we can go up or down

def near_edge():
    x_distance_from_home = abs(xcor())
    y_distance_from_home = abs(ycor())
    return x_distance_from_home > max_x_coord or \
           y_distance_from_home > max_y_coord

########################################
# Define some fixed values to control the simulation
#
step_size = 10 # how far the turtle moves in each step, in pixels
turn_angle = 20 # how far to turn to avoid the edge, in degrees

########################################
# Set up the drawing window and other overall parameters
#
title("Four Corners")
hideturtle()
bgcolor("white")
width(10)
speed("fastest")

########################################
# Start by pointing the turtle in a random direction
#
setheading(randint(0,359))

########################################
# In each step check to see if we're near an edge and,
# if so, turn to the right.  Also change colour depending
# on the current segment.
#
for step in range(3000): # how many steps to take in the simulation
    if near_edge():
        right(turn_angle)
    forward(step_size)
    if(xcor() < 0 and ycor() > 0):
        color(Q1);
    elif(xcor() > 0 and ycor() > 0):
        color(Q2);
    elif(xcor() < 0 and ycor() < 0):
        color(Q3);
    elif(xcor() > 0 and ycor() < 0):
        color(Q4);
    else:
        color('black');

########################################
# Release the drawing window when finished
#
done()
