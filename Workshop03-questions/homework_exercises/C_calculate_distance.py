#---------------------------------------------------------
#
# Calculate Distance
#
# Define a function with two parameters, a number to
# represent time taken (in minutes) and average speed
# (in kms/hr).  The function should return the distance
# travelled given the time taken and the average speed.
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
# Comment: Notice in each test case below that we
# round the result to a whole number.  This is because
# the actual answer returned, e.g., 16.6666..., may depend
# on the precision of your particular computer architecture.
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
>>> round(calculate_distance(60, 5)) # Test 1 - normal case
5

>>> round(calculate_distance(30, 8)) # Test 2 - normal case
4

>>> round(calculate_distance(1, 1000)) # Test 3 - short time, high speed
17

>>> round(calculate_distance(60000, 1)) # Test 4 - long time, low speed
1000

>>> round(calculate_distance(600, 0)) # Test 5 - boundary case, no speed 
0

>>> round(calculate_distance(60, 1)) == 1 # Test 6 - check value is returned not printed
True

"""


#---------------------------------------------------------
# Solution strategy: You will need to calculate how far
# the vehicle travels in one minute and then multiply
# this by the time taken.
#

### PUT YOUR calculate_distance FUNCTION HERE
pass


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

##from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
##print(testmod(verbose = False,
##              optionflags = REPORT_ONLY_FIRST_FAILURE))

