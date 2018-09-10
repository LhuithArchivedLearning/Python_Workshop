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
from tkinter import Tk, Text, Button, END, Label
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
def display_current_choice(cBox):
    if len(Choice.get("1.0", END)) == 1:
        Choice.insert(END,  cBox.get());
        FinishButton['text'] = "CheckOut";        
    else:
        Choice.insert(END,  ", " + cBox.get());

def checkout():
    if len(Choice.get("1.0", END)) != 1:
        text_file = open("Groceries.txt", "w");
        text_file.write("Groceries List:\n%s" % str(Choice.get('1.0', END)));
        text_file.close();

        Choice.delete("1.0", END);
        FinishButton['text'] = "Items Saved";
        grossCombo.set("Please Select Yo Shizz");

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
