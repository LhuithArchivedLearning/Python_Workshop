#---------------------------------------------------------
#
# Calculate Wages
#
# As an example of a numerical calculation that includes
# a condition, define a function to calculate and return
# the weekly wages to be paid to an employee. The function
# should have two parameters:
#
# 1)  a number representing the total number of hours worked;
#     and
# 2)  a number representing the hourly rate of pay.
#
# Apart from the amount paid for a "normal" week's work,
# there are two special conditions applicable:
#
# a) a penalty rate of time and a half (i.e., one and a half times
#    the normal hourly rate) is payable for hours worked in
#    excess of 40; and
# b) a weekly bonus of $50 is also payable if the number
#    of hours worked exceeds 50.
#
# The result should be returned as a floating point number.
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
>>> calculate_wages(40, 20) # Test 1. Normal case - no penalty rates
800.0

>>> calculate_wages(41, 20) # Test 2. Normal case - one penalty hour
830.0

>>> calculate_wages(55, 20) # Test 3. Normal case - penalty rates over 50 hours
1300.0

>>> calculate_wages(45, 10.10) # Test 4. Normal case - penalty rates, floating point numbers
479.75

>>> calculate_wages(43.5, 90.40) # Test 5. Normal case - penalty rates, floating point numbers
4090.6

>>> calculate_wages(0, 10.5) # Test 6. Boundary case - 0 hours worked
0.0

>>> calculate_wages(45, 0) # Test 7. Boundary case - 0 hourly rate
0.0

>>> calculate_wages(0, 0) # Test 8. Boundary case - 0 hours and rate
0.0

>>> calculate_wages(50, 110) # Test 9. Boundary case - exactly 50 hours worked
6050.0

>>> calculate_wages(45, 10.10) == 479.75 # Test 10. Check value is returned not printed
True

"""


#---------------------------------------------------------

##### DEFINE YOUR calculate_wages FUNCTION HERE
def calculate_wages(hours, rate) :
    if hours > 50 :
        return ((rate) * 40) + ((rate * 1.5) * (hours - 40)) + 50;
    elif hours > 40:
        return ((rate) * 40) + ((rate * 1.5) * (hours - 40));
    else :
        return float(rate * hours)
    
    


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))


