#--------------------------------------------------------------------
#
# Fun With Flags
#
# In the lecture demonstration program "stars and stripes" we saw
# how function definitions allowed us to reuse code that drew a
# star and a rectangle (stripe) multiple times to create a copy of
# the United States flag.
#
# As a further example of the way functions allow us to reuse code,
# in this exercise we will import the flag_elements module into
# this program and create a different flag.  In the PDF document
# accompanying this file you will find several flags which can be
# constructed easily using the "star" and "stripe" functions already
# defined.  Choose one of these and try to draw it.
#

# First we import the two functions we need (make sure a copy of file
# flag_elements.py is in the same folder as this one)
from flag_elements import star, stripe

# Import the turtle graphics functions
from turtle import *

# Set up the drawing environment
setup(600, 400)
speed('fastest');

penup();
goto(-300, 200);
pendown();
stripe(600, 80, 'green');
penup();
setheading(270);
forward(80);
pendown()
stripe(600, 80, 'orange');
penup();
setheading(270);
forward(80);
pendown()
stripe(600, 80, 'green');
penup();
setheading(270);
forward(80);
pendown()
stripe(600, 80, 'orange');
penup();
setheading(270);
forward(80);
pendown()
stripe(600, 80, 'green');
penup();
goto(-300, 200);
pendown();
stripe(225, 240, 'red');

penup();
goto((-300 + (225/2)), (200 - (100/2)));
pendown();
star(125,'white')

# Exit gracefully
hideturtle();
done()
