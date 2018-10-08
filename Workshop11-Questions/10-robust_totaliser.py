#-------------------------------------------------------------
#
# Robust totaliser program
#
# The interactive function below repeatedly
# prompts the user to enter a positive number.  For each
# number entered, the function prints the sum of all
# the numbers entered so far.  It stops when 0 is entered.
#
# However, this function is vulnerable to user errors, such
# as typing non-numeric values or using a keyboard interrupt
# (Control-C) to try to stop the program. To solve this,
# modify the function so that it catches exceptions
# caused by invalid user inputs and prints a meaningful
# message for them.  Your code must distinguish between
# four different kinds of user errors and must respond
# with a different, meaningful message for each one:
#
# a) The user entering a non-numeric value, e.g., the
#    string 'joe';
#
# b) The user entering a syntactically malformed expression,
#    e.g., +[[$;
#
# c) The user entering the name of an undefined variable,
#    e.g., fred, where no assignment has ever been made to
#    fred; and
#
# d) The user issuing a keyboard interrupt (Control-C) to
#    try to terminate the program immediately.
#
# Note that we have used the "eval" function below which
# means that the "totaliser" crashes as soon as the user
# enters anything that isn't a valid Python expression.
#
# Hint: You may find it helpful to introduce a "helper"
# function to read user inputs until a valid one is
# entered, to allow for the possibility of the user
# repeatedly entering bad values.
#
# NB: Since this function depends on inputs entered by
# the user it is difficult to construct automated unit tests
# for it.  (This can be done, but is awkward.)  Instead,
# therefore, we have described typical test cases below
# as comments only.
#

##---------------------------------------------------------
##
##    TESTCASES
##
##    Example of an interaction with the function in which
##    the user enters a mixture of both valid and invalid
##    values (the invalid cases won't be handled properly
##    until you modify the function):
##
##    >>> totaliser()
##    Please enter a number: 5
##    The total so far is 5
##
##    Please enter a number: 3 * 2   <---- Numeric expressions are OK
##    The total so far is 11
##
##    Please enter a number: fred   <---- Can't use undefined variable names
##    ** Unknown variable ignored
##    Please enter a number: 'joe'   <---- Can't use non-numeric values
##    ** Non-numeric value ignored
##    Please enter a number: 4
##    The total so far is 15
##
##    Please enter a number: 'quit'
##    ** Non-numeric value ignored
##    Please enter a number: ^C   <---- User types Control-C
##    ** Enter a 0 to stop the program
##    Please enter a number: 7
##    The total so far is 22
##
##    Please enter a number: 2 + 3
##    The total so far is 27
##
##    Please enter a number: [+  <---- Can't use syntactically invalid expressions
##    ** Malformed expression ignored
##    Please enter a number: 2
##    The total so far is 29
##
##    Please enter a number: -1
##    Goodbye    
##
##---------------------------------------------------------


##### MAKE THE FOLLOWING INTERACTIVE FUNCTION ROBUST
##### AGAINST INVALID USER INPUTS

# An interactive function which repeatedly prompts the
# user to enter a number and for each one entered shows the
# sum of all the numbers entered so far, until a 0 is entered
def totaliser():

    # Initialise the running total
    total = 0

    # Get the first response from the user
    response = eval(input('Please enter a number: '))

    # As long as the user's response is positive display the
    # running total
    while response >= 0:
        total = total + response
        print('The total so far is', total)
        print()
        response = eval(input('Please enter a number: '))

    # Exit gracefully
    print('Goodbye')


# Uncomment the following line to call the function
# automatically whenever this file is run:
totaliser()
