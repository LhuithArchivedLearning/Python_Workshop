#---------------------------------------------------------
#
# Robust "is square?" predicate
#
# The following Boolean function determines if a
# given non-negative number is a square of another number
# (i.e., if its square root is a whole number).
#
# However, this predicate crashes when given an invalid
# parameter.  Your job is to add exception handling code to print
# an appropriate message when an invalid input is
# supplied.  Here we assume that an invalid input is a
# value which is not a number, or a number which is negative.
#
# NB: Pay attention to the error messages generated when
# the original function is called with an invalid parameter.
# They will tell you what kind of exception you need to catch,
# e.g., a "TypeError" exception will be thrown if you attempt
# an arithmetic operation with a non-numeric value.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
---------- Normal cases, with expected inputs ----------

Normal case
>>> is_square(9) # Test 1
True

Normal case
>>> is_square(10) # Test 2
False

Normal case
>>> is_square(22500) # Test 3
True

Normal case
>>> is_square(134688) # Test 4
False

Boundary case
>>> is_square(1) # Test 5
True

Boundary case
>>> is_square(0) # Test 6
True

-------- "Invalid" cases, with unexpected inputs ---------

Invalid case - string instead of number
>>> is_square('10') # Test 7
Argument must be numeric

Invalid case - list instead of number
>>> is_square([10]) # Test 8
Argument must be numeric

Invalid case - a negative number
>>> is_square(-2) # Test 9
Argument must be non-negative

"""


#---------------------------------------------------------
#
# Make this function robust against invalid parameters
# by catching exceptions and printing a meaningful
# error message as shown in the tests above.
#

# A Boolean function to determine if a given number
# is a square (i.e., its square root is a whole number)
#
def is_square(number):

    from math import sqrt

    return sqrt(number) % 1 == 0



#---------------------------------------------------------
# This function executes the unit tests above when called.
# To see if your solution passes all the tests, just call
# the function below.
#
def test():
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print(testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE))

# Uncomment the following line to call the test function
# automatically whenever this program is run:
test()
