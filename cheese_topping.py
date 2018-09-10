#Module for Drawing Cheese Toppings

from turtle import *
from random import randint

#define a function to draw a peice of cheese
def add_pieces_of_cheese (how_far, how_many = 150) :
    for piece in range(how_many):
        #Choose cheesy colors
        pencolor('orange');
        fillcolor('yellow');
        #choose a cheese shape
        shape('square');
        #Move to a random position on the pizza
        home();
        setheading(randint(0,359));
        forward(randint(0, how_far));
        #Stamp a shape onto the screen
        stamp();    
