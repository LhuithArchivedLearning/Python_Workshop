#----------------------------------------------------------------
#
# TRAFFIC LIGHT
#
# In this exercise you must create a Graphical User
# Interface using tkinter.  The program should create
# a window containing a drawing canvas and three buttons.
# Each time one of the buttons is pressed a red, yellow
# or green circle should be drawn on the canvas, in
# imitation of a traffic light.
#
# As an additional feature, you could restrict the
# buttons so that the lights can only follow the usual
# green-yellow-red-green sequencing.  (There is no yellow
# between red and green in real traffic lights!)
#

# Import the necessary tkinter functions
from tkinter import Tk, Button, Canvas

# Create a window
traffic_window = Tk()

# Give the window a title
traffic_window.title('Traffic Light')


###### PUT YOUR CODE HERE

# 1. Define functions to be called when one of the buttons
#    is pressed which will create appropriately coloured
#    ovals on the drawing canvas, using the "create_oval"
#    "Canvas" method with an appropriate "fill" colour
#    parameter

def draw_light(color, event) :
    startpos = 25;
    size = 50;
    
    if color == 'red':
        draw_screen.create_oval(startpos, 10, startpos + size, 60, fill = 'red', outline = "");
    elif color == 'yellow':
        draw_screen.create_oval(startpos + size, 10, startpos + size + size, 60, fill = 'yellow', outline = "");
    elif color == 'green':
        draw_screen.create_oval(startpos + size + size, 10, startpos + size + size + size, 60, fill = 'green', outline = "");
    else :
        print('Bugger This');

    #draw_screen.delete("all");

# 2. Create the three Button widgets and pack them into
#    the main window

def on_relase(event) :
    draw_screen.delete("all");


red_button = Button(traffic_window, font = ('Ariel', 32), text = 'RED');
yellow_button = Button(traffic_window, font = ('Ariel', 32), text = 'YELLOW');
green_button = Button(traffic_window, font = ('Ariel', 32), text = 'GREEN');


red_button.grid(row = 1, column = 1);
yellow_button.grid(row = 1, column = 2);
green_button.grid(row = 1, column = 3);6

red_button.bind("<ButtonPress>", lambda event, col = 'red' : draw_light('red', event));
yellow_button.bind("<ButtonPress>", lambda event, col = 'red' : draw_light('yellow', event));
green_button.bind("<ButtonPress>", lambda event, col = 'red' : draw_light('green', event));

red_button.bind("<ButtonRelease>", on_relase);
yellow_button.bind("<ButtonRelease>", on_relase);
green_button.bind("<ButtonRelease>", on_relase);

#red_button.pack();
#green_button.pack();
#yellow_button.pack();

# 3. Create the drawing Canvas widget and pack it into the
#    main window

draw_screen = Canvas(traffic_window, width = 200, height = 100);
draw_screen.grid(row = 0, column = 2);
#draw_screen.pack();


# Start the event loop to react to user inputs
traffic_window.mainloop()
