#------------------------------------------------------------
#
# Whack-a-Mole
#
# Motivation: As a demonstration of a program that involves
# both definite and indefinite iteration here we develop a
# simple version of a children's game often found in arcades.
#
# Scenario: A nasty mole is digging holes in your prize front
# lawn!  It suddenly pops up its head from underground and
# spins around in circles as it creates a large hole.  Armed
# with a mallet your job is to discourage this behaviour by
# whacking the mole on the head before it finishes the hole.
# If you succeed in hitting the mole in time it gives up and
# moves elsewhere.  If you miss the mole, or it finishes
# digging, a big hole appears in your nice lawn.
#
# Your task: This is a fairly complicated program to complete
# in one workshop, so below we've provided most of the code.
# You need to fill in the missing code at the points
# marked "***".  Before doing so, study the parts of the
# code that have been supplied to ensure that you understand
# the overall program structure.
#
# Technical note: This program relies on Turtle function
# onscreenclick.  Given the name of another function
# onscreenclick "binds" that function to the "event"
# of the player clicking the mouse in the drawing
# window.  This is an example of an ASYNCHRONOUS
# function call.  We don't call the bound function explicitly
# as we normally do, it is called by the Turtle run-time
# system whenever the mouse is clicked.  Such asynchronous
# function calls are common in interactive programs, but are
# not normally used in programs that just perform some fixed
# calculation.
#
# Disclaimer: This program relies on the precise timing of
# certain events and the ability of the function bound by
# onscreenclick to INTERRUPT some other program code that
# is running (in function move_mole below).  The precision
# with which these events are synchronised is very much
# dependent on the particular operating system you're using.
# Although we've tested this program in a few different
# Python implementations we can't guarantee good timing
# behaviour in every such system.  (Turtle graphics isn't
# intended for creating interactive games!)
#
# Extension: There are many improvements that could be made
# to this "game".  The most obvious is to add a counter to
# keep track of the player's score, so that it can be
# displayed at the end.
#


#-----------------------------------------------------------
# Import various functions needed for the game
#
from turtle import *
from random import randint
from time import sleep


#-----------------------------------------------------------
# Introduce global variables needed to keep track
# of the game's state here
#
# *** INTRODUCE GLOBAL VARIABLES NEEDED TO CONTROL THE GAME HERE


#-----------------------------------------------------------
# Introduce global constants needed to control the game's
# layout and other characteristics
#
max_screen_x, max_screen_y = 400, 300 # max positive or negative screen coords
border = 50 # how close the mole can get to the edge of the screen
max_x, max_y = max_screen_x - border, max_screen_y - border # mole's max coords
num_holes = 10 # how many holes the mole will attempt to dig
num_spins = 3 # how many times the mole spins before a hole is finished


#-----------------------------------------------------------
# Call this function to get the mole to run around in a small
# circle, as if digging a hole
#
def spin_around():
    sleep(0.25) # pause for a quarter second
    circle(10) # run around in a small circle


#-----------------------------------------------------------
# Call this function to make the mole say "Ouch!" when
# whacked
#
def say_ouch():
    write("Ouch!", align="center", font=("Arial", 20, "normal"))


#-----------------------------------------------------------
# Call this function to create a hole when the player has
# failed to whack the mole in time
#
def dig_hole():
    dot(50) # pixels

    
#-----------------------------------------------------------
# This Boolean function returns True iff the given coordinates
# are near the mole's (turtle's) current position, as defined
# by a square area around the given coords
#
def near_mole(x_coord, y_coord):
    leeway = 20 # how close we need to get, in pixels
    return (x_coord - leeway <= xcor() <= x_coord + leeway) and \
           (y_coord - leeway <= ycor() <= y_coord + leeway)


    
#-----------------------------------------------------------
# This function defines the behaviour of the mole
#
def move_mole():
    pass # does nothing (delete after inserting your code)
    
    # *** DECLARE ANY GLOBAL VARIABLES YOU NEED HERE
    # global 

    # Move to a random location
    new_x, new_y = randint(-max_x, max_x), randint(-max_y, max_y)
    goto(new_x, new_y)

    # Spin a certain number of times or until the player clicks
    # the mouse in the window

    # *** ADD A WHILE LOOP HERE THAT CAUSES THE MOLE TO SPIN
    # *** UP TO A FIXED NUMBER OF TIMES OR UNTIL THE MOUSE
    # *** HAS BEEN CLICKED
    
    # Decide what action to take at the end of an attempt to
    # dig a hole

    # *** ADD CODE HERE TO EITHER SAY "OUCH" OR COMPLETE THE
    # *** HOLE AS APPROPRIATE

    # Reset global variables for next hole

    # *** RESET ANY GLOBAL VARIABLES YOU USED, READY FOR THE
    # *** MOLE'S NEXT ATTEMPT TO DIG A HOLE
    
    
#-----------------------------------------------------------
# This function is called automatically by the Turtle system
# whenever the player clicks the mouse in the window
#
# It sets some global variables to record how successful the
# player's attempt to whack the mole was
#
def whack(x_coord, y_coord):
    pass # does nothing (delete after inserting your code)
    
    # *** DECLARE ANY GLOBAL VARIABLES YOU NEED HERE
    # global
    
    # *** UPDATE GLOBAL VARIABLES HERE TO RECORD THE "WHACK"
    # *** AND WHETHER IT SUCCEEDED OR NOT


#-----------------------------------------------------------
# This is the "main program"
#

# Set up the drawing screen
setup(max_screen_x * 2, max_screen_y * 2)
title("Whack-A-Mole")
bgcolor("light green")

# Create a "realistic" looking mole
register_shape("mole.gif")
shape("mole.gif")

# Lift up the pen so that the mole doesn't leave tracks
penup()

# Define which function to call when the player clicks the
# mouse button in the drawing window
onscreenclick(whack)

# Start playing the game by calling the move_mole function a
# fixed number of times

# *** ADD A FIXED LOOP HERE TO MOVE THE MOLE SEVERAL TIMES

# Terminate the game elegantly
hideturtle()
done()
