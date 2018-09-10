###################################################################
#
# Hungry Ant
#
# As a graphics program that involves making decisions, this
# program aims to simulate the behaviour of a foraging ant.  The
# ant meanders about the screen at random until either it is
# exhausted or until it finds a tasty meal.  A different message is
# displayed depending upon the outcome.
#
# The program below is a minor variant of the "step to the right"
# turtle graphics demonstration from Lecture 4.  The
# main differences are:
#
# 1) The pen is kept up, so that no line is drawn as our "ant"
#    moves around.
#
# 2) A function and some related constants have been added to draw
#    a coloured dot on the screen representing delicious ant
#    food.
#
# Your tasks are as follows.
#
# a) Foraging ants rarely walk in perfectly straight lines.  Modify
#    the code to introduce a random "wobble" in the ant's direction
#    at each step.  Hint: Add code to do a small left or right turn
#    before the ant would normally walk straight forward.  (It's best
#    to leave the ant's behaviour alone when it's turning to avoid
#    the edge of the screen, otherwise you may create a situation
#    where the ant gets stuck randomly moving along an edge.)
#
# b) Define a Boolean-valued function that returns True if and only
#    if the ant is currently within the square representing food.
#    Hint: You will need to use the built-in xcor() and ycor()
#    functions to determine the ant's location, and the global
#    constants that fix the position and size of the food.
#
# c) Change the program so that it recognises when the ant has
#    wandered onto the food.  In this case the ant should stop and
#    the message "Yum, yum!" should be displayed on the screen.
#    Hint: You will need to use the built-in write() function to
#    print text in the drawing window.  Also, note that Python's
#    "break" command causes the program to exit the current loop
#    immediately, so can be used to terminate the "for" loop.
#
# d) As a further refinement, you should get the ant to say "I give
#    up!" if all of the "steps" have been completed and the food
#    has not been found.  Hint: You will need a way of remembering
#    whether the loop ended because the food was found or because
#    the ant has completed the specified number of steps.
#


########################################
# Import the necessary pre-defined functions
from turtle import *
from random import randint


########################################
# Define some fixed values to control the simulation - change
# these to alter the simulation's behaviour
#
step_size = 10 # how far the ant moves in each step, in pixels
turn_angle = 20 # how far to turn to avoid the edge, in degrees
food_x_pos, food_y_pos = -230, 250 # coordinates where the food is placed
food_radius = 50 # how big to make the food dot


########################################
# This Boolean-valued function returns True if the ant is near
# any of the drawing window's four edges 
#
border = 60 # how close we must get to be considered "near" the edge
max_x_coord = (window_width() // 2) - border # how far we can go left or right
max_y_coord = (window_height() // 2) - border # how far we can go up or down

def near_edge():
    x_distance_from_home = abs(xcor())
    y_distance_from_home = abs(ycor())
    return x_distance_from_home > max_x_coord or \
           y_distance_from_home > max_y_coord

def on_food():
    x_distance_from_food = abs(xcor() - food_x_pos)
    y_distance_from_food = abs(ycor() - food_y_pos)
    return x_distance_from_food < food_radius and \
             y_distance_from_food < food_radius

    
########################################
# Function to draw a dot representing ant food (the
# given coords are the centre of the dot)
#
def draw_food(x_pos, y_pos, radius):
    penup()
    goto(x_pos, y_pos) # bottom left
    color("orange")
    dot(radius * 2)


########################################
# Main program starts here:
# Set up the drawing window and other overall parameters.
#
title("Hungry Ant")
bgcolor("green")
penup()
speed("fastest")

########################################
# Create the "food".
#
draw_food(food_x_pos, food_y_pos, food_radius)

########################################
# Start with the ant at the origin pointing in a random direction.
#
color("black")
home()
setheading(randint(0, 359))

########################################
# In each step check to see if we're near an edge and,
# if so, turn to the right
#
for step in range(1000): # how many steps the ant should take
    
    
    if near_edge():
        right(turn_angle)
    elif on_food() :
        break;
    #### Add code here to give the ant a random wobble
    #### if it is NOT near an edge
    roll = randint(0,1);
    if roll == 0 :
        left(randint(0,3));
    else :
        left(-randint(0, 2));

    if step % 2 == 0:
        pendown();
    else:
        penup();
        
    forward(step_size)
    #### Add code here to see if the food has been found
    #### and take appropriate action

print('Ant is Munchin');
########################################
# Release the drawing window when finished.
#
done()
