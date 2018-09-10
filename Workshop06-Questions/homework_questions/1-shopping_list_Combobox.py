#----------------------------------------------------------------
#
# ALTERNATIVE SHOPPING LIST
#
# In this exercise you will develop a Graphical User
# Interface using Tkinter.  In another workshop exercise
# you created a "shopping list" application using Tkinter's
# Listbox and Text widgets.  Apart from selecting pre-defined
# grocery items from the Listvox, it was also possible to
# manually type items into the Text area.  In this exercise
# you will provide a different user interface for doing this
# job, this time using the ttk module's Combobox widget.
#
# WARNING: This exercise relies on the "ttk" package
# which offers some extra widgets beyond those provided
# by Tkinter, including the Combobox widget needed
# here.  It's possible that the ttk module may not be
# installed in some older Python installations.  If you
# get an error when trying to import from ttk you will
# not be able to complete this exercise.
#
# In this version of the "shopping list" application you
# must create a window containing a Text box, a Combobox and
# a Button widget. The options in the Combobox are typical
# grocery items.  Each time the user selects a grocery
# item in the Combobox and presses the Button the item
# should be displayed in the Text box, to create
# a shopping list.  Users can also enter items not in
# the default shopping list into the Combobox manually.
#

# Import the necessary Tkinter functions
from tkinter import Tk, Text, Button, END
from tkinter.ttk import Combobox

# Create a window
window = Tk()

# Give the window a title
window.title('Shopping list')

# Our list of grocery choices
groceries = ['Eggs', 'Milk', 'Bread', 'Coffee', 'Tea', 'Lettuce',
             'Tomatoes', 'Onions', 'Chicken', 'Cheese', 'Fish',
             'Sugar', 'Rice', 'Pasta', 'Soup', 'Cereal', 'Yogurt']


##### DEVELOP YOUR CODE HERE

# 1. Define a function to display the current choice
#    in the Text area when the button is pushed

def display_current_choice(event, text):
    Choice.delete(1.0, END);
    Choice.insert(END, text);
    
# 2. Create a Text area to display the user's choice and
#    pack it into the main window
Choice = Text(window, height = 2, width = 10, font = ('Arial', 32));
Choice.pack();

# 3. Create a Combobox widget whose parent container is the
#    main window and pack it
grossCombo = Combobox(window, width = 10, value = groceries);
grossCombo.current(0);
grossCombo.state(['readonly']);
grossCombo.bind("<<ComboboxSelected>>", lambda event:display_current_choice(event, grossCombo.get()));
grossCombo.pack();
# 4. Create a Button to push when the user is happy with
#    their choice and pack it


# Start the event loop to react to user inputs
window.mainloop()
