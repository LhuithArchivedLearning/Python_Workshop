#---------------------------------------------------------
#
# Average
#
# As a very simple exercise in defining your own reusable
# function, define a function with two parameters, both numbers,
# that calculates and returns the average of those numbers.
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
>>> average(2, 10) # Test 1 - normal case, integer inputs
6.0

>>> average(3, 10) # Test 2 - normal case, integer inputs
6.5

>>> average(9.5, 10) # Test 3 - floating point input
9.75

>>> average(5, 5) # Test 4 - same values
3.0

>>> average(0, 0) # Test 5 - boundary case
0.0

"""


#---------------------------------------------------------
# Problem solving strategy for the "average" function:
# 1. Return ...
# 2.   the sum of the two numbers ...
# 3.   divided by two (using floating point division).

#### REPLACE THE "DO NOTHING" STATEMENT BELOW
##### WITH YOUR average FUNCTION DEFINITION
def average(num0, num1):
    return (num0 + num1) / 2.0;

#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
