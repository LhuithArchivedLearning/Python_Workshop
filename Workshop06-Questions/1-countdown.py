#----------------------------------------------------------------
#
# COUNTDOWN
#
# In this exercise you must create a Graphical User
# Interface using tkinter.  The program should create
# a window containing a label and a button.  The label
# displays a number and each time the button is pressed
# the number in the label should decrease by 1 until
# it reaches zero, at which some other value can be
# displayed.  This will give you practice at both
# creating widgets and getting them to interact.
#

# Import the necessary tkinter functions
from tkinter import Tk, Button, Label

# Create a window
countdown_window = Tk()

# Give the window a title
countdown_window.title('Countdown')


##### PUT YOUR CODE HERE

# 1. Define a function to be called when the button is
#    pressed which will change the label's value
def label_change() :

    try :
        current = int(result['text']);6
        
        if(current > 1) :
            result['text'] = current - 1;
        else :
            result['text'] = 'NOPE';
        
    except :
        print("NOPE");


# 2. Define the Button widget and pack it into the
#    main window
count_button = Button(countdown_window, font = ('Arial', 32), text = 'Do Stuff', command = label_change);
count_button.pack();


# 3. Define the Label widget and pack it into the main
#    window
result = Label(countdown_window, font = ('Arial', 32), text ='10');
result.pack();

# Start the event loop to react to user inputs
countdown_window.mainloop()
