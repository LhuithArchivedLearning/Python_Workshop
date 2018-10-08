#---------------------------------------------------------------#
#
# Disarm That Bomb!
#
# We've all seen films and television shows where the hero needs
# to disarm a time bomb by cutting the wires leading to the
# trigger.  But which wire to cut first!?!  Tension mounts as
# our hero tries to choose between the red, green and blue
# wires...!!!
#
# Below is a Tkinter-based program that attempts to simulate
# this scenario.  It provides three buttons representing
# choices of wires to cut and randomly generates the correct
# sequence.  Pushing the buttons in the correct sequence
# ends the game with a congratulatory message.  However,
# pushing the buttons in the wrong sequence produces error
# messages in the shell window and prevents the game from
# reaching a final outcome.
#
# Your task is to modify this program so that it doesn't
# misbehave when the wrong button is pressed and always ends
# the game properly, either with the bomb being disarmed
# or exploding.  When an incorrect button is pressed it should:
#
# a) Display a message in the GUI indicating that the bomb
#    has exploded; and
# b) Disable all the buttons because the game is over.
#
# Importantly, however, you cannot change, delete or disable
# any of the existing lines of Python code.  Instead you must
# use your knowledge of exception handling to prevent the
# existing code misbehaving, but without changing it in any
# way.
#

# Import the Tkinter functions
from tkinter import Tk, Button, Frame, Label, DISABLED

# Import a random number function
from random import shuffle

# Create a window
bomb_display = Tk()

# Give the window a title
bomb_display.title('Disarm That Bomb!')

# Create a label to display the current state of the bomb
display = Label(bomb_display, font = ('Arial', 48),
                text = "It's ticking...!",
                width = 16, bg = 'gold')

# Global variable to define valid sequence of cuts
valid_sequence = ['Red', 'Green', 'Blue']
shuffle(valid_sequence)

# Function that's called when any button is pressed
def button_pushed(button, colour):
    global valid_sequence
    # Disable this button so that it can't be pressed again
    button['state'] = DISABLED
    # Confirm that the buttons have been pushed in the right order
    assert valid_sequence[0] == colour
    # Remove the first item from the sequence of pushes required
    valid_sequence.pop(0)
    # See if the bomb has been disarmed yet
    if valid_sequence == []:
        display['text'] = "You've done it!"
        display['bg'] = 'green'
    else:
        display['text'] = colour + ' wire cut!'
   
# The individual functions called when the buttons are pressed
def cut_red():
    button_pushed(red_button, 'Red')

def cut_blue():
    button_pushed(blue_button, 'Blue')

def cut_green():
     button_pushed(green_button, 'Green')

# Create a frame to hold the buttons
buttons = Frame()

# Create the push button widgets
red_button = Button(buttons, text = ' Cut red wire ',
                    activeforeground = 'red', font = ('Arial', 20),
                    command = cut_red)
blue_button = Button(buttons, text = ' Cut blue wire ',
                     activeforeground = 'red', font = ('Arial', 20),
                     command = cut_blue)
green_button = Button(buttons, text = ' Cut green wire ',
                      activeforeground = 'red', font = ('Arial', 20),
                      command = cut_green)

# Use the grid geometry manager to put the widgets into their locations
display.grid(row = 0, column = 0, padx = 5, pady = 10)
red_button.grid(row = 0, column = 0)
blue_button.grid(row = 0, column = 1)
green_button.grid(row = 0, column = 2)
buttons.grid(row = 1, column = 0)

# Start the event loop to react to user inputs
bomb_display.mainloop()
