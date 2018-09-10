#----------------------------------------------------------------
#
# PASSCODE
#
# In this challenging exercise you will develop a non-trivial
# GUI program using Tkinter that comprises:
#
# 1) a ten digit keypad;
# 2) an 'OK' button; and
# 3) a text field.
#
# The program should allow numerical passcodes to be entered
# after which the OK button can be pressed.  If the passcode
# entered is a valid one then appropriate feedback should
# be provided, and similarly for invalid passcodes.
#
# The valid passcodes in this case should be your
# eight digit student numbers (with a leading zero).
#
# It is suggested that you develop this program in several
# steps:
#
# a) Write the 'back-end' function that recognises valid
#    passcodes.
# b) Develop a simple GUI 'front-end' for communicating
#    between the user and the back end, without worrying
#    about how the GUI widgets are laid out.
# c) Make the GUI look nice by laying out the widgets in
#    a natural format.
#
# Observation: To recognise the ten different digits we need
# ten separate functions attached to the buttons, meaning
# that some code will be duplicated 10 times.  Cleverer
# solutions which avoid this duplication are possible, but
# are too sophisticated for our current needs.  Brute
# force is acceptable here!
#

# Import the tkinter functions
from tkinter import *

# Create a window
passcode_window = Tk()

# Give the window a title
passcode_window.title('Passcode')


#### PUT YOUR SOLUTION HERE

# You will need to implement the following features:
#
# * A Text widget for providing feedback to the user
# * An 'OK' Button widget which, when pressed, calls a
#   function to see if a valid passcode has been entered
# * Ten Button widgets which, when pressed, call a
#   corresponding function to record the fact that the
#   button has been pushed
# * A global Python variable to keep track of the button
#   presses (digits entered) so far
# * Ten functions, one for each digit, which are called
#   when the corresponding button is pushed and add the
#   corresponding digit to the global variable
# * The function which is called when the 'OK' button
#   is presssed to check the global variable to see if a valid
#   passcode has been entered, to update the Text field
#   accordingly, and the reset the global variable ready
#   for the next passcode
#

# Start the event loop
passcode_window.mainloop()
