#---------------------------------------------------------
#
# Is the number a square?
#
# Define a Boolean function with one parameter, a number,
# which determines if that number is a square of an integer.
# A Boolean function is one which returns True or False
# - also called a 'predicate'.
#
# Hints: A given number is the square of an integer if
# its square root is a whole number.  A whole number is
# one which has no remainder when divided by 1.
#
# Warning: Remember that negative numbers don't have a
# square root!
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
>>> square(9) # Test 1. Normal case
True

>>> square(100) # Test 2. Normal case
True

>>> square(99) # Test 3. Normal case
False

>>> square(22500) # Test 4. Normal case
True

>>> square(134688) # Test 5. Normal case
False

>>> square(1) # Test 6. Boundary case
True

>>> square(0) # Test 7. Boundary case
True

>>> square(-1) # Test 8. Boundary case
False

>>> square(-100) # Test 9. Normal case
False

"""


#---------------------------------------------------------

##### DEFINE YOUR square FUNCTION HERE
def square(val) :
    if val < 0 :
        return False
    else :
        return (val ** (1/2.0)) % 1 == 0;
    


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))

