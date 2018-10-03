#---------------------------------------------------------
#
# Delete an element
#
# In this exercise you will develop a Python program that
# accesses SQLite database tables.  We assume that you have
# already loaded a version of the Elements tables using
# a graphical user interface.  You can do so by running the
# elements.sql script provided.  (These tables are
# slightly different than those used in last week's
# workshop.)
#
# In a previous exercise you were required to print the
# contents of the elements tables.  In doing so you
# may have noticed that the database contained two
# spurious entries, Kryptonite and Dalekanium.  You therefore
# need to clean the database by deleting these entries.
# However, to do so notice that you need to update both the
# "symbols" and "atomic_numbers" tables.
#
# 1) In a suitable graphical interface, select the "symbols"
# table and delete the row corresponding to Kryptonite.
#
# 2) In the graphical interface, use the SQL editor to create
# and execute a "DELETE FROM" statement to delete Kryptonite
# from the "atomic_numbers" table too.  Write the result to the
# permanent database file.
# 
# 3) Rather than manually deleting entries from both tables
# it would be more convenient to have a single Python
# function that did this for us.  Develop a function below
# that accepts an element name and deletes it from both
# the "atomic_numbers" and "symbols" tables.
#
# 4) Use your function to delete Dalekanium from the database
# in one step and confirm that you have succeeded by re-running
# your solution to the previous Print Elements exercise.
#


#---------------------------------------------------------

# Import the SQLite functions
from sqlite3 import *

## DEVELOP YOUR FUNCTION HERE BY REPLACING EACH OF THE 'pass'
## STATEMENTS BELOW (WHICH DO NOTHING) WITH THE NECESSARY CODE

# Connect to the elements database and delete the named
# element from both the atomic_numbers and symbols tables.

def delete_element(element_name):
    
    # 1. Make a connection to the elements database
    pass

    # 2. Get a cursor on the database
    pass

    # 3. Construct the first SQLite delete statement
    pass

    # 4. Construct the second SQLite delete statement
    pass

    # 5. Execute both statements
    pass

    # 6. Commit the changes to the database
    pass
    
    # 7. Close the cursor and connection
    pass
