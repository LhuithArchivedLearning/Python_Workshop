#----------------------------------------------------------------
#
# Invalid Query
#
# As an example of making a fragile IT system robust, in this
# exercise you will prevent a program that accesses a database
# from crashing.
#
# NB: Before you can complete this exercise you may need to create
# the "used_cars.db" database by importing and running
# the "car_details.sql" dump script in your favourite SQLite
# GUI, if it has not already been provided.
#
# The program below provides a simple textual interface to the
# used car database.  It prompts the user to enter an SQL
# query, runs the query, and then prints the results.
#
# Some queries the user may want to enter are as follows:
#
#     SELECT DISTINCT make FROM car_details
#
#     SELECT DISTINCT model FROM car_details WHERE make = 'HOLDEN'
#
#     SELECT make, model FROM car_details WHERE seriesYear = '1968'
#
#     SELECT carId, make FROM car_details WHERE engineSize = '1.5L'
#
# However, this program will crash if the user enters invalid
# SQLite code.
#
# Your task is to use exception handling to stop the program
# crashing in this circumstance.  Firstly run the
# program to find out which exception is thrown by this
# problem.  Then add "TRY ... EXCEPT ..." code to allow the
# program to continue executing even after such an error occurs.
#


#----------------------------------------------------------------

# Import the SQLite functions
from sqlite3 import *

# Connect to the database
connection = connect(database='used_cars.db')

# Get a cursor into the database
cars_db = connection.cursor()

# Get queries from the user and execute them
query = input('Enter an SQLite query on the Used Cars data: ')

while not query.lower() in ['stop', 'exit', 'quit']:
    # Execute the query
    cars_db.execute(query)
    # Display the results
    for row in cars_db.fetchall():
        for cell in row:
            print(cell, end = ' ')
        print()
    # Get the next query
    print()
    query = input('Enter an SQLite query on the Used Cars data: ')
    
# Unlock the database
cars_db.close()
connection.close()
