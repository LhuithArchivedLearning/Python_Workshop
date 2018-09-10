#---------------------------------------------------------
#
# Odd?
#
# Define a "predicate" function (one that returns True or False)
# with one parameter, an integer, that determines whether or
# not the given integer is odd.
#
# Hints: An odd integer is one which has something left over
# when it is divided by 2.  Python's built-in "n % d" operator
# returns the remainder when numerator n is divided by
# denominator d.
#
# The tests below tell us how your function is expected to
# behave when called.  After you've written your function,
# confirm that it works correctly by (a) running this module
# so that your function is defined and then (b) copying
# each of the function calls in the set of tests into the
# shell to see if the right answer is returned.  Obviously
# if you don't get the expected answers then you'll need
# to modify your code until you do.
# 
# Finally, the main program of this file runs the tests
# automatically.  The code is commented out, but if you
# want to run all the tests automatically, just uncomment
# the code and run this file.  Of course, you should pass
# all the tests in order to complete this exercise.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> odd(1) # Test 1. Normal case
True

>>> odd(4) # Test 2. Normal case
False

>>> odd(1000001) # Test 3. Normal case
True

>>> odd(0) # Test 4. Boundary case
False

>>> odd(-1) # Test 5. Another boundary case
True

"""


#---------------------------------------------------------

##### DEFINE YOUR odd FUNCTION HERE
def odd(val):
    return val % 2 != 0;


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))

