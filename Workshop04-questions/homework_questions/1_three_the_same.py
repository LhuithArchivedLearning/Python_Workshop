#---------------------------------------------------------
#
# Three the same
#
# Define a "predicate" function (one that returns True or False)
# with three parameters.  The function should return True
# only if all three parameters have the same value.
#
# Comment: This is very easy in Python compared to some older
# programming languages.
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
>>> same(1, 2, 3) # Test 1. Normal case
False

>>> same('b', 'b', 'b') # Test 2. Normal case, another type
True

>>> same('b', 'b', 'a') # Test 3. Normal case
False

>>> same([3], [3, 3], [3]) # Test 4. Normal case, yet another type
False

>>> same([], [], []) # Test 5. Normal case
True

"""


#---------------------------------------------------------

##### DEFINE YOUR same FUNCTION HERE
def same(a, b, c) :
    return a == b == c;

#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
