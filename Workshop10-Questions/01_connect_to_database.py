#----------------------------------------------------------------------
#
# Check database connection
#
# This program retrieves and displays some simple data,
# in order to confirm that we can access the Airline database
# from a Python script.
#
# Before running this script you should read the instruction sheet,
# and use the DB Browser for SQLite or a similar tool to create
# the Airline database from the script provided.
#
# After you've run this script, try adding some flights into the
# database via its graphical interface and run the script again
# to confirm that the database has been updated.
#

# Import the SQLite functions
from sqlite3 import *

# Create a connection to the database.
connection = connect(database = 'airline.db')

# Get a cursor on the database.  This allows you to execute SQLite
# queries and get the results.
airline_db = connection.cursor()

# Execute an SQLite query which retrieves the number of flights
# listed in the "flights" table.
airline_db.execute("SELECT count(*) FROM flights")

# Get the first row from the query's Result Set.
row = airline_db.fetchone()

# Display the first element of the row.
print("Number of flights:", row[0])

# Close the cursor.
airline_db.close()

# Close the database connection.
connection.close()
