#----------------------------------------------------------------
#
# SHOPPING LIST
#
# In this exercise you will develop a Graphical User
# Interface using tkinter.  The program must create a
# window containing a text box, a list box and
# a button. The options in the list box are typical
# grocery items.  Each time the user selects a grocery
# item in the list and presses the button it
# should be displayed in the text box, to create
# a personalised shopping list.
#

# Import the necessary tkinter functions needed to create
# the window and the three widgets
from tkinter import Tk, Text, Button, Listbox

# Import the tkinter constant END which is useful when
# we want to add text to the end of a Text area or an
# item to the end of a Listbox
from tkinter import END

# Our list of choices
groceries = ['Eggs', 'Milk', 'Bread', 'Coffee', 'Tea', 'Lettuce',
             'Tomatoes', 'Onions', 'Chicken', 'Cheese', 'Fish',
             'Sugar', 'Rice', 'Pasta', 'Soup', 'Cereal', 'Yogurt']

# Create a window
window = Tk()

# Give the window a title
window.title('Shopping list')


###### ADD YOUR CODE TO CREATE WIDGETS AND THEIR BEHAVIOUR HERE

# 1. Define a function which displays the user's current
#    list choice in the text area when the button is pushed

# 2. Create a text area widget which will display the
#    user's choices

# 3. Create a listbox widget and insert all the grocery choices
#    into it

# 4. Create a button widget which calls the function defined
#    above when the user pushes it


# Start the event loop to react to user inputs
window.mainloop()
