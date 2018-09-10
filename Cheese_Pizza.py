#Cheese Pizza

#import fuctions
from turtle import *
from random import randint
from cheese_topping import add_pieces_of_cheese

#Constants
diameter = 600 #pixels
crust = 50 #pixels

#Create a Canvas
setup(900, 700);
title('This is a Cheese Pizza');
tablecloth = 'sea green';
bgcolor(tablecloth);

#Create the Base
pencolor('tan');
dot(diameter);


#add tomato paste
pencolor('dark red');
dot(diameter - crust);

#Add cheese to the pizza
penup();


#stop drawing each step
tracer(False);
#add lots of cheese

add_pieces_of_cheese(diameter//2.0 - 25, 500);

#Slice the Pizza
tracer(True);
speed('fastest');
penup();
home();
pendown();
width(6);
pencolor(tablecloth);

for cut in range(6):
    forward(diameter/2.0);
    goto(0,0);
    left(60);



#Close Down
hideturtle();
done();
