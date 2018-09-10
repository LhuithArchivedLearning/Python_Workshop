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
from tkinter import Tk, Text, Button, END, Label
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

def display_current_choice(cBox):
    if len(Choice.get("1.0", END)) == 1:
        Choice.insert(END,  cBox.get());
        FinishButton['text'] = "CheckOut";        
    else:
        Choice.insert(END,  ", " + cBox.get());

def checkout():
    if len(Choice.get("1.0", END)) != 1:
        Choice.delete("1.0", END);
        FinishButton['text'] = "Items Added";
        
CartLabel = Label(window, height = 1, width = 30, font = ('Arial', 12), text = 'Cart');
CartLabel.pack();
# 2. Create a Text area to display the user's choice and
#    pack it into the main window
Choice = Text(window, height = 20, width = 30, font = ('Arial', 12));
Choice.pack();

# 3. Create a Combobox widget whose parent container is the
#    main window and pack it
grossCombo = Combobox(window, width = 20, value = groceries);
grossCombo.set("Please Select Yo Shizz");
grossCombo.state(['readonly']);
grossCombo.bind("<<ComboboxSelected>>", lambda event:display_current_choice(grossCombo));
grossCombo.pack();
# 4. Create a Button to push when the user is happy with
#    their choice and pack it
FinishButton = Button(window, height = 1, width = 30, font = ('Arial', 12), text = 'CheckOut', command = checkout);
FinishButton.pack();

# Start the event loop to react to user inputs
window.mainloop()
