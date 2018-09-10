#--------------------------------------------------------------------------
#
#   Used Car Browser
#
#   In this exercise you will create a Graphical User Interface to make
#   it easy to browse a large data collection.  Beginning with a large
#   randomly-organised file of used car details, you will present it to
#   the user sorted alphabetically, thus making it easier to search.
#
#   1) Before you begin you must have access to the "car_details.csv" file.
#   This file contains details of over 3,000 used cars for sale.
#
#   2) Open the file in either a spreadsheet application or a text editor
#   and familiarise yourself with its contents.  Note that it contains
#   numerous lines of text, each of which consists of several comma-separated
#   fields.
#
#   3) Below is some code which creates an empty Tkinter window.
#   Follow the instructions in this code to complete a program that
#   extracts relevant details from the file and displays them
#   in a scrollable Text widget to allow the user to browse just the
#   basic car details, without all the other distracting information
#   in the database table.  Most importantly, your task is to make
#   it easier for the user to search for a particular car by presenting
#   the list of cars sorted alphabetically by make and model.
#


# Import the necessary Tkinter functions
from tkinter import Tk, Text, END

# Create a window
window = Tk()

# Give the window a title
window.title('Used Car Browser')

###### ADD YOUR CODE TO CREATE WIDGETS AND THEIR BEHAVIOUR HERE

# 1. Define a function which opens the "car_details.csv" file
# and returns a list of strings describing each car.  The
# description of each car should consist of the make, model
# price and "car id" in that order (and nothing else).  Most
# importantly, the list should be sorted alphabetically, which
# will make it much easier for the user to find a particular
# make and model.
pass

# 2. Create a Text widget to display the results and pack
# it into the Tk window
pass

# 3. Call your function to get the relevant data from the
# car_details file and store the list of results in a variable
pass

# 4. Insert each item in the list of results into the "END" of
# the Text widget, one line each.
pass

# 5. Using your mouse's scroll wheel you should now be able to
# easily browse the details extracted from the file, to help
# you find a used car of the make and model you prefer.
# (Tk Text widgets are scrollable under Apple macOS.  You
# may find different behaviours on different operating
# systems.)

# Start the event loop to react to user inputs
window.mainloop()
