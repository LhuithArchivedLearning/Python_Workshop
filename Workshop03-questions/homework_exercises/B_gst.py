#---------------------------------------------------------
#
# Goods and Services Tax
#
# Define a function with one parameter, a number representing
# a wholesale price, that returns the GST component to be added
# to that wholesale price (where GST is 10%).
#
# Observation: Computer-based floating point arithmetic
# doesn't always produce mathematically-precise results (see
# Appendix B of the Python Tutorial).  Therefore, we've
# rounded off the answers to two decimal places in the tests.
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
>>> round(gst(100), 2) # Test 1 - normal case (integer)
10.0

>>> round(gst(123.56), 2) # Test 2 - normal case (floating point number)
12.36

>>> round(gst(100 + 50), 2) # Test 3 - normal case (wholesale price as an expression)
15.0

>>> round(gst(0), 2) # Test 4 - boundary case (price is zero)
0.0

>>> round(gst(123456789), 2) # Test 5 - price is a very large number
12345678.9

"""


#---------------------------------------------------------
# Your solution
#

#### DEFINE YOUR gst FUNCTION HERE
pass


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

##from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
##print(testmod(verbose = False,
##              optionflags = REPORT_ONLY_FIRST_FAILURE))
