#-----------------------------------------------------------
#
# Target shooting
#
# As a graphical exercise involving conditional statements,
# here you will complete a simple game-like program which
# lets the user shoot at a target by clicking the mouse in
# the drawing canvas.
#
# When you run this question file it will display a target,
# but otherwise do nothing.  You need to study the given
# code below and then develop a function called "fire" which
# responds to mouse clicks by drawing a bullet hole and
# displaying a score.  Importantly, the score is different
# depending on where the mouse click occurred.  To allow
# for this you will need to use a conditional statement.
#


# Import the Turtle graphics functions
from turtle import *
from random import *
from math import *
#-----------------------------------------------------------
# Define some fixed values
#
screen_size = 800 # pixels
bullseye_diameter = 300 # pixels
target_diameter = 600 # pixels


#-----------------------------------------------------------
# Here is where you define your function which is called
# when someone clicks on the screen.  The function should
# be called "fire" and take two parameters, the x and y
# coordinates at which the mouse was clicked.  This function
# must:
#
# (a) draw a bullet hole in the appropriate location;
# (b) decide how much the "shot" is worth, either 10, 5
#     or 1 points, depending on whether the shot hit the
#     bullseye, the outer circle or missed altogether;
# (c) write the score next to the bullet hole; and
# (d) display the player's total score so fari n the
#     window's title.
#
# Hints:
# * You will find Turtle's "distance" function very helpful
#   for deciding how close the shot was to the origin.
# * Turtle's "write" function can be used to print text on
#   the screen.  To avoid writing over the bullet hole you
#   can either move the cursor first, or precede the number
#   by a few blank spaces.
# * To display the total score in the window's title you
#   can call Turtle's "title" function.  (Although normally
#   just used at the beginning of a program, this function
#   can be called as often as you like.)
# * You will need a way of remembering what the player's
#   total score is between calls to the "fire" function.  A
#   global variable may be helpful!
#

##### Put your "fire" function, and any other code needed
##### to support it, here

#screen_size = 800 # pixels
#bullseye_diameter = 300 # pixels
#target_diameter = 600 # pixels

def fire(x,y):
    penup()
    goto(x,y);
    dot(randint(10,30));
    
    dx = (x - screen_size//2) + screen_size//2;
    dy = (y - screen_size//2) + screen_size//2;

    length = sqrt((dx * dx) + (dy * dy));
    
    if length < (target_diameter//2.0) :
        print('Hit The Target!');
        
        if length < (bullseye_diameter//2) :
            print('and it was a Bullseye!!! ',int(length),'pixels from centre');
    else :
        print('Damn you missed');
#-----------------------------------------------------------
# The following code is the main program which sets
# up the target.  You will need to uncomment the
# call below to the "onscreenclick" function when
# you have created your "fire" function.

# Set up the drawing window
setup(screen_size, screen_size)
title('Your total: 0 points')
bgcolor('dark green')

# Draw the target as a big yellow dot
color('yellow')
dot(target_diameter)

# Draw the bullseye as a smaller red dot
color('red')
dot(bullseye_diameter)

# Hide the cursor and set the "bullet hole" colour
penup()
hideturtle()
color('black')

# Define which function to call when the mouse is clicked
##### Uncomment the following line when you've defined
##### your "fire" function
onscreenclick(fire)


# Allow the drawing window to be closed
done()
