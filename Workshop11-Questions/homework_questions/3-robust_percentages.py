#------------------------------------------------------------
#
# Robust percentages program
#
# The interactive function below accepts one parameter,
# a number representing the maximum possible value of some
# quantity.  The function then prompts the user for
# numeric values and for each one prints what percentage
# it is of the maximum possible value.  It assumes that
# the parameter and the numbers entered by the user
# are all positive numbers.  The function stops
# when the user enters 'stop', 'exit' or 'quit'.
#
# However, the percentages function is vulnerable to user errors,
# such as users typing non-numeric values, or the maximum
# possible value parameter being zero (which makes it impossible
# to calculate a percentage).  To solve these problems,
# modify the function so that it catches exceptions
# caused by invalid user inputs and prints a meaningful
# message for them.  Your new function should also raise an
# exception if its parameter is not positive.  Importantly,
# *you may not change* any code in the original function,
# you may only add new code.
#
# NB: Since this function depend on inputs entered by
# the user it is difficult to construct automated unit tests
# for it.  (This can be done, but is awkward.)  Instead,
# therefore, we have described typical test cases below
# as comments only.
#


##------------------------------------------------------------
##
##    TESTCASES
##
##    A typical interaction where the parameter and the user's
##    inputs are all valid:
##
##    >>> percentages(80)
##    Please enter a number: 40
##    50.0%
##    Please enter a number: 20
##    25.0%
##    Please enter a number: 120
##    150.0%
##    Please enter a number: 75 - 10
##    81.25%
##    Please enter a number: 1
##    1.25%
##    Please enter a number: -1
##    Goodbye
##
##    Function calls where the maximum-value parameter is
##    not positive cannot be used to calculate a sensible
##    percentage, so an appropriate exception is raised:
##
##    >>> percentages(0)
##    Traceback (most recent call last):
##    ...
##    AssertionError: Invalid parameter: 0
##
##    >>> percentages(-11)
##    Traceback (most recent call last):
##    ...
##    AssertionError: Invalid parameter: -11
##
##    An interaction where some of the user's inputs are
##    invalid should cause a meaningful message to be
##    displayed:
##
##    >>> percentages(200)
##    Please enter a number: 50
##    25.0%
##    Please enter a number: 'a'
##    Non-numeric value entered!
##    Please enter a number: [4]
##    Non-numeric value entered!
##    Please enter a number: 4
##    2.0%
##    Please enter a number: -1
##    Goodbye
##
##---------------------------------------------------------


#### CREATE A ROBUST VERSION OF THIS INTERACTIVE FUNCTION
#### BY ASSERTING THAT ITS PARAMETER IS VALID AND CATCHING
#### EXCEPTIONS THROWN BY USER INPUTS

# A robust function to prompt the user for numbers which are
# then printed as a percentage of the parameter
def percentages(max_value):
    # Read the first value
    users_value = input('Please enter a number: ')
    # Repeat until a 'stop' command is entered
    while not users_value.lower() in ['stop', 'exit', 'quit']:
        # Print percentage
        print(str((float(users_value) * 100.0) / max_value) + '%')
        # Get next value
        users_value = input('Please enter a number: ')
    # Confirm exit
    print('Goodbye')

# Uncomment the following line, and change the argument, to
# automatically call the function whenever this file is run:
#percentages(500)


