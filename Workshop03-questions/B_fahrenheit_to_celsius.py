#---------------------------------------------------------
#
# Temperature Conversion
#
# Define a function with one parameter, a number representing
# a temperature in Fahrenheit, that returns that temperature
# in Celsius.  In general the relationship between a temperature
# in Celsius C and the corresponding temperature in Fahrenheit F
# is C = (F - 32) * (5 / 9).
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
# NB: For accuracy you should do the calculation using
# floating point arithmetic.  However, the tests show that
# we want the result as an integer (a whole number).
# Having calculated the answer as a floating point number
# you should therefore use the built-in "round" function
# to round the answer off to a whole number before
# returning it.
#
# Observation: This exercise takes us into the dangerous
# and complex territory of floating point arithmetic,
# where different answers may be produced by computers with
# different architectures, e.g., 32-bit versus 64-bit
# arithmetic.
# 
# Finally, the main program of this file runs the tests
# automatically.  The code is commented out, but if you
# want to run all the tests automatically, just uncomment
# the code and run this file.  Of course, you should pass
# all the tests in order to complete this exercise.


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> fahrenheit_to_celsius(32) # Test 1 - normal case (freezing point)
0

>>> fahrenheit_to_celsius(212) # Test 2 - normal case (boiling point)
100

>>> fahrenheit_to_celsius(100) # Test 3 - normal case (hot day!)
38

>>> fahrenheit_to_celsius(70) # Test 4 - normal case
21

>>> fahrenheit_to_celsius(86) # Test 5 - normal case 
30

>>> fahrenheit_to_celsius(-40) # Test 6 - special case (same result)
-40

>>> fahrenheit_to_celsius(32) == 0 # Test 7 - check value is returned and not just printed
True

"""


#---------------------------------------------------------
# Your solution
#

#### REPLACE THE "DO NOTHING" STATEMENT BELOW WITH YOUR
#### fahrenheit_to_celsius FUNCTION DEFINITION
def fahrenheit_to_celsius(F) :
    return  round((F - 32) * (5 / 9))
    


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
