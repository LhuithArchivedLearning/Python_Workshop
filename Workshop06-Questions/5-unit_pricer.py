#--------------------------------------------------------------------#
#
# Unit Pricer
#
# Studies have shown that shoppers are very bad at mental arithmetic.
# For instance, most people don't realise that a 50% increase in
# quantity is the same as a 33% discount in price.  Instead they
# assume the former is better value.  Similarly, if offered 33%
# extra for free or 33% off the price most people think these deals
# are the same, whereas the discount is much better value.
#
# For this reason "unit pricing" is a big advantage for consumers,
# allowing them to easily compare the value of different products.
# In this exercise you will create a simple interactive tool for
# calculating unit prices as a shopping aid.  This can be done with
# just three widgets, two spinboxes and a label, but as time
# permits you should aim to make your user interface as "friendly"
# as possible.
#
# Below is an incomplete Tkinter program.  Follow the instructions
# in the order shown to complete your unit pricing "app".
#

# Import the standard Tkinter functions
from tkinter import *

# Create the main window
pricing_window = Tk()
pricing_window.title('Unit Price Calculator')

# Step 3: Define a function to calculate and display
# the unit price.  This function should get the price
# and quantity from the respective spinboxes, convert
# the values to integers, and use them to calculate
# the unit price as the price divided by the quantity.
# It should then replace the text in the label with the
# unit price.  As time permits, try to format the
# displayed result nicely.
#
# Step 4: Once your function is complete, add it as the
# "command" used by the spinboxes when they are updated.
# In this way your function will be called to update
# the label whenever one of the spinboxes is changed by
# the user.
pass

# Step 2: Create two "spinbox" widgets and put them in
# the main window.  Both widgets should allow the user
# to select an integer value from 1 to 99, inclusive.
# One of these widgets will be used to enter a price in
# dollars and the other a quantity in kilograms.
# Check online for documentation on how to create a
# spinbox.  In particular, note that the range of values
# is defined by "from_" and "to" parameters, with the
# odd spelling of "from_" being used to avoid conflicting
# with Python's "from" keyword.  If time permits, add
# labels to the GUI to tell the user what the widgets are
# for.
pass

# Step 1: Create a label in which to display results and
# put it in the main window. The text in this label will
# show unit prices in dollars per kilogram.  Initialise it
# with some default text to show when the program starts.
pass

# Start the event loop
pricing_window.mainloop()
