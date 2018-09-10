
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task I agree that it represents my own work.
#  I am aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  Student no: n10318313
#  Student name: Eugene Martens
#
#--------------------------------------------------------------------#


from turtle import *

square_size = 250;
rotation = 45;

#centres the turtle
#based on rotation and size
#moves on x axis first
#then on y axis
def Centre_Pointer(size, rot):
    setheading(0 + rot);
    forward(size/2);
    setheading(270 + rot);
    forward(size/2);
    setheading(0);

#creates a square, sets the filling collor
#centres and sets the heading
#then iterates throug 4 times to draw the 4
#lines of the square
def Square(fill_col, size, rotation) :

    #start method by making sure pen is up
    #and turtle is home with fill color set
    penup();
    home();
    fillcolor(fill_col);

    #set centre based on size and rotation
    Centre_Pointer(size, rotation);
    setheading(rotation);
    
    begin_fill();
    
    #draw the square after heading was set
    for point in range(4):
        pendown();
        left(90);
        forward(size);

    end_fill();
        
    penup();

#set the startup functions
speed('fastest');
home();
width(7);

#draw the 3 squares
Square("#FF0000", square_size, rotation);
Square("#0000FF", square_size / 1.4, rotation);
Square("#00FF00", square_size / 2.5, rotation);

#end gracefully
hideturtle()
done()


