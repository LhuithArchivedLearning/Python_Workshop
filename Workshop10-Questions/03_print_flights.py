#---------------------------------------------------------
#
# A function to print flight details
#
# In this exercise you will develop a Python program that
# accesses SQLite database tables.  We assume that you have
# already restored the Airline database.  (You can do so
# by running the airline.sql script.)
#
# Your tasks:
#
# 1) Browse the database's contents in a suitable graphical
# interface to ensure that you're familiar with its tables and
# their columns.
#
# 2) In the graphical interface, develop a SELECT query which prints
# all details of flights departing from a particular city code, as they
# appear in the "flights" table.  For instance, if you use the
# FromCityCode "BNE" the result set should be:
#
#   FlightNum FromCityCode ToCityCode SeatsRemaining AircraftType
#   1         BNE          SYD        10             AB3
#   5         BNE          CGK        50             757
#   6         BNE          LAX        60             74L
# 
# 3) Using this SELECT query, write a Python function called
# "print_flights" which accepts a FromCityCode and prints all
# the corresponding flight details.  (Don't worry about formatting
# the output nicely.)  The docstring below shows the output
# this function should produce.  Recall that after an SQL query
# has been executed on a database "cursor", method call
# "cursor.fetchall()" will return a list of all rows in the
# result set, and you can then use a FOR-EACH loop to process each
# row in the list.
#


#---------------------------------------------------------
# The following docstring contains examples of the
# expected output from your function.
#
""" 
The following tests call your function and check that it
prints the right data from the database.

>>> print_flights('SYD')
2 SYD CBR 20 727
3 SYD MEL 30 757
4 SYD AKL 40 D10
7 SYD HNL 70 767
9 SYD LAX 90 744
10 SYD BNE 100 AB3

>>> print_flights('BNE')
1 BNE SYD 10 AB3
5 BNE CGK 50 757
6 BNE LAX 60 74L

>>> print_flights('HNL')
8 HNL SFO 80 767

"""


#---------------------------------------------------------

# Import the SQLite functions
from sqlite3 import *

## DEVELOP YOUR FUNCTION HERE BY REPLACING EACH OF THE 'pass'
## STATEMENTS BELOW (WHICH DO NOTHING) WITH THE NECESSARY CODE

# A function to connect to the airline database, retrieve
# data from the flights table for a specific departure point
# and print the FlightNum, FromCityCode, ToCityCode, SeatsRemining
# and AircraftType for each flight leaving from that location.
#
def print_flights(departure_city):

    # 1. Make a connection to the database
    connection = connect(database = 'airline.db');

    # 2. Get a cursor on the database
    airline_db = connection.cursor

    # 3. Construct the SQLite query (being careful to include quote marks
    #    around the city code string as per the SQLite syntax)
    pass

    # 4. Execute the query
    pass

    # 5. Fetch the result set and print each row
    pass
 
    # 6. Close the database cursor and connection
    pass


#---------------------------------------------------------
# Uncomment the main program below if you want to test
# your function against the docstring above automatically.
#
# from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
# print(testmod(verbose = False,
#               optionflags = REPORT_ONLY_FIRST_FAILURE))
