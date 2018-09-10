#----------------------------------------------------------------------
#  Luck of the Irish
#
#  As another example of code reuse, in this exercise you will develop
#  a Turtle graphics function to draw a shamrock (a three-leaf clover)
#  and use it to populate an Irish field.
#

# Import the turtle graphics functions
from turtle import *

# Set up the "grassy field"
field_size = 600 # pixels
setup(field_size, field_size)
bgcolor("dark green")
title("Luck of the Irish")

# Adjust the drawing speed, if necessary
speed('normal')
#----------
# Step 1
#
# Define a function that draws a single shamrock.  It should have
# two parameters, the x and y coordinates at which to draw the
# image.  The shamrock should consist of three circular leaves and
# a stem.  Choose an appropriate colour, distinct from the background.

leaf_size = 80;

def DrawShamRockLeaf(x, y, heading):
    main_leaf_circ = 45;

    direction = heading - 26;
    setheading(direction);
    begin_fill();
    circle(leaf_size, -main_leaf_circ);
    circle(leaf_size/4, -180);
    end_fill();
    setheading(270 + direction + 10);
    begin_fill();
    circle(leaf_size/4, -180);
    circle(leaf_size, -main_leaf_circ);
    end_fill(); 
    setheading(0);
    

    
def Shamrock(x, y) :
    pencolor('white');
    fillcolor('white');
    DrawShamRockLeaf(x, y, 0);
    #setheading(90);
    DrawShamRockLeaf(x + 1, y + 1, 90);
    DrawShamRockLeaf(x - 1, y - 1, 270);
    #DrawShamRockLeaf(x, y);

#----------
# Step 2
#
# Write a main program to display 50 (or so) shamrocks randomly
# positioned on the field.  Use the field size defined above
# to limit the placement of shamrocks.

### PUT YOUR MAIN PROGRAM HERE
Shamrock(0,0);


# Exit gracefully
hideturtle()
done()
