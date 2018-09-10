#----------------------------------------------------------------
#
# Join the dots
#
# This exercise gives you practice at both Turtle graphics and
# using lists.  It would be helpful to review your solution to 
# the "Starry, starry night" exercise from Workshop 2 before
# attempting this one.
#
# THE PROBLEM
#
# You are required to firstly draw 25 (or more)
# randomly-positioned dots on the screen and then
# draw a line connecting them together in the same
# order that they were drawn.  Draw the dots and the
# connecting line in different colours.
#
# NB: You cannot start drawing the line until AFTER
# you've finished drawing all the dots.  This means
# you'll need to find a way of remembering where all
# the dots are and the order in which they appeared.
#
# Hint: A list is a good way of remembering a sequence of
# numbers!
#
# Extra challenge: Use Turtle's "write" function to write
# consecutive numbers next to each dot as you draw them.
# This makes your solution look more like a real join-the-dots
# puzzle.
#


# Import the necessary functions
from turtle import *
from random import randint

# Adjust the drawing speed, if necessary
speed("fastest")

# A suggested problem-solving strategy:
#
# 1. Create the drawing canvas
# 2. Create list(s) to record the coordinates of the dots
# 3. Draw the dots.  For each one:
#    a. Choose a random position on the screen
#    b. Move to the chosen position and draw a dot
#    c. Record the position of the dot in your list(s)
# 4. Draw the connecting line
#    a. Change to an appropriate pen color and size
#    b. Go to the position of the first dot, without drawing
#    c. For each position recorded in the list(s), go to that
#       position, drawing as you go
# 5. Exit gracefully by unlocking the screen
done()
