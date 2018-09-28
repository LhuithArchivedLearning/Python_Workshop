#-------------------------------------------------------------------------
#
#  Olympic Rings
#
#  In this folder you will find a file "olympic_rings.pdf" which shows
#  the flag used for the Olympics since 1920.  Notice that this flag
#  consists of five rings that differ only in their position and colour.
#  If we want to draw it using Turtle graphics it would therefore be
#  a good idea to define a function that draws one ring and reuse it
#  five times.
#
#  Complete the code below to produce a program that draws a reasonable
#  facsimile of the Olympic flag.  (NB: In the real flag the rings are
#  interlocked.  Don't try to reproduce this tricky feature, just draw
#  rings that overlap.)
#


#-------------------------------------------------------------------------
#  Step 1: Function definition
#
#  Define a function called "ring" that takes three parameters, an
#  x-coordinate, a y-coordinate and a colour.  When called this function
#  should draw an "olympic ring" of the given colour centred on the
#  given coordinates.  (Note that Turtle graphic's "circle" function
#  draws a circle starting from the cursor's current position, not
#  centred on the cursor's position.)  Since all the circles are the
#  same size you can define the radius and thickness of the circle
#  within the function.

outter_ring_size = 100
w = 15;
inner_ring_size = outter_ring_size - w;

def ring(x, y, col) :
    fillcolor(col);
    color(col);
    penup();

    #outer ring
    goto(x, y - outter_ring_size/2.0);
    pendown();
    begin_fill()
    circle(outter_ring_size);
    penup();

    #inner ring
    goto(x, y - (outter_ring_size/2.0 - w));
    pendown();
    setheading(180);
    circle(-inner_ring_size);
    end_fill();
    penup();
    setheading(0);
#-------------------------------------------------------------------------
#  Step 2: Calling the function
#
#  Now write code to call the function five times, each time with
#  different coordinates and colours, to create the flag.  To get
#  you started we have provided some of the Turtle framework.

#  Import the Turtle functions
from turtle import *


#  Create the drawing window
setup(1000, 650)
title('"... and it\'s gold, Gold, GOLD for Australia!"')

speed('fastest');

# Draw the five rings
ring(-(outter_ring_size * 2) - w/2.0, 0, 'blue');

ring(0,0, 'black');
ring((outter_ring_size * 2) + w/2.0, 0, 'red');

ring((outter_ring_size + w/2.0), -outter_ring_size, 'green');
ring(-(outter_ring_size + w/2), -outter_ring_size, 'yellow');

###  PUT YOUR FUNCTION CALLS HERE


#  Shut down the drawing window
hideturtle()
done()
