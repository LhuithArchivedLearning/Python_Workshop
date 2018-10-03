#---------------------------------------------------------
#
# Updating data in a table
#
# In this exercise you will develop a Python program that
# accesses SQLite database tables.  We assume that you have
# already restored the Airline database.  (You can do so
# by executing the airline.sql script.)
#
# Your tasks:
#
# 1) Using a graphical interface, examine the "flights"
# table and set the number of seats remaining for
# Flight Number 6 to zero, on the assumption that
# this flight is now fully booked.  Write the change
# to the database.
#
# 2) Using the graphical interface's SQL editor, write and
# execute an "UPDATE" statement that does exactly the
# same thing for Flight Number 3.  Examine the result to
# confirm that your SQL statement changes the relevant
# value just like you did interactively.
# 
# 3) Using this knowledge, write a Python function called
# "close_flight" that prompts the user for a flight
# number and sets its number of seats remaining to zero.
# In the shell window, use your function to close Flight
# Numbers 9 and 10 and check that it worked by examining
# the table in the GUI.
#

#---------------------------------------------------------

# Import the SQLite functions
from sqlite3 import *

# Connects to the airline database and updates the number
# of seats remaining.
#
def close_flight():

    # 1. Make a connection to the airline database
    pass

    # 2. Get a cursor on the database
    pass

    # 3. Prompt the user for a the number of a flight
    #    to close
    pass

    # 4. Construct the SQLite UPDATE statement 
    pass

    # 5. Execute the statement
    pass

    # 6. Commit the update to the database
    pass
    
    # 7. Close the cursor and connection
    pass
    
