#---------------------------------------------------------
#
#  Concentric Circles
#
#  In an earlier workshop exercise you developed a program
#  which drew three concentric circles.  Here we will
#  illustrate the power of repetitive code by developing
#  functions that draw as many circles as we want.
#
#  In this exercise you will define three Turtle graphics
#  functions, "draw_circles_for", "draw_circles_while"
#  and "draw_circles_recursive", each of which draws a set of
#  concentric circles centred on the screen's origin.  Each
#  function must accept the number of circles to be drawn as
#  its parameter.  So that the circles are all of different
#  sizes, global variable "separation" below should be used
#  to differentiate the radius of each successive circle.
#  The first circle should be of radius "separation" pixels,
#  the second of radius "2 * separation" pixels and so on.
#
#  This behaviour can be implemented easily using a FOR loop,
#  and with only a little more thought using a WHILE loop or
#  recursively.  Try doing it in all three ways.  The code
#  for drawing one circle can be common to all three
#  versions.
#

from turtle import *

# How much separation there should be between each successive
# circle's radius
separation = 10 # pixels

#---------------------------------------------------------

## DEVELOP YOUR THREE FUNCTIONS HERE
def draw_circles_for(steps):
    
    for step in range(steps):
        penup();
        setheading(270);
        forward(step * separation);
        setheading(0);
        pendown();
        circle(step * separation);
        penup();
        home();

def draw_circles_while(steps):

    count = 0;
    while(count <= steps):
        count += 1;
        penup();
        setheading(270);
        forward(count * separation);
        setheading(0);
        pendown();
        circle(count * separation);
        penup();
        home();

def draw_circles_recursive(steps):
    steps -= 1;
    print(steps);
    if(steps > 0):
        penup();
        setheading(270);
        forward(steps * separation);
        setheading(0);
        pendown();
        circle(steps * separation);
        penup();
        home();
        draw_circles_recursive(steps);
#---------------------------------------------------------
#
# This main program calls one of your functions.  Uncomment
# the appropriate call for the function you are developing.
#

# Set up
setup()
title("Concentric circles")
speed("fastest")

# Test the functions by drawing 30 circles.
# Uncomment these calls one at a time to test your functions.
#
#draw_circles_for(30)
#draw_circles_while(30)
draw_circles_recursive(30)

# Clean up
hideturtle()
done()


