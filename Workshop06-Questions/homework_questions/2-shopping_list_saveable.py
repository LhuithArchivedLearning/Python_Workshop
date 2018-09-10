#----------------------------------------------------------------
#
# SAVEABLE SHOPPING LIST
#
# NB: To do this exercise you must have already completed one of
# the "shopping list" exercises.
#
# In the previous "shopping list" exercise you created a GUI
# which allowed the user to select grocery items and add them to
# a list of such items which was displayed in the user
# interface.  However, the list is lost when the GUI is closed
# down.  Extend your solution so that:
#
# a) It has a button labelled "Save" that can be pressed at
# any time; and
#
# b) When the "save" button is pressed the current contents of
# the list are written to a text file "shopping_list.txt".
#
# To do this you will need to use a list-valued variable to
# keep track of the current contents of the list.
#

# Import the necessary Tkinter functions
from tkinter import Tk, Text, Button, END
from tkinter.ttk import Combobox

# Create a window
window = Tk()

# Give the window a title
window.title('Shopping list')

# Create a list of choices
groceries = ['Eggs', 'Milk', 'Bread', 'Coffee', 'Tea', 'Lettuce',
             'Tomatoes', 'Onions', 'Chicken', 'Cheese', 'Fish',
             'Sugar', 'Rice', 'Pasta', 'Soup', 'Cereal', 'Yogurt']


##### DEVELOP YOUR SOLUTION HERE, BASED ON YOUR PREVIOUS SHOPPING LIST CODE

# 1. Introduce a list variable keeps track of the user's choices

# 2. Add a button for saving the list

# 3. Define a function which writes the contents of the variable to
#    a text file


# Start the event loop to react to user inputs
window.mainloop()
