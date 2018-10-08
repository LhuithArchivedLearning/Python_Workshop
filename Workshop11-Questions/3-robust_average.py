#---------------------------------------------------------
#
# Robust average function
#
# The function below accepts a list of numbers and
# returns their average (as a floating point value), but
# crashes when invalid input is supplied.
#
# Your job is to add exception handling code so that the
# function no longer crashes, but instead produces a
# sensible error message as shown in the tests below.
#
# NB: Pay attention to the error messages generated when you
# call the function with an invalid parameter.  They will
# tell you what kind of exception you need to catch, e.g.,
# "TypeError".
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
---------- Normal cases, with expected inputs ----------

Normal case
>>> average([2, 10]) # Test 1
6.0

Normal case - incorporating fractional result
>>> average([3, 10, 6.5]) # Test 2
6.5

Normal case - floating point numbers
>>> average([9.5, 10]) # Test 3
9.75

Boundary case - one value
>>> average([5]) # Test 4
5.0

-------- Invalid cases, with unexpected inputs ---------

Invalid case - incorrect type
>>> average('1, 2, 3, 4, 5, 6') # Test 5
Argument must be a list of numbers

Invalid case - incorrect type
>>> average(1) # Test 6
Argument must be a list of numbers

Invalid case - incorrect type
>>> average(['a', 'b', 'c']) # Test 7
Argument must be a list of numbers

Invalid case - incorrect type
>>> average(sum) # Test 8
Argument must be a list of numbers

Invalid case - incorrect type
>>> average([1, 'a', 2]) # Test 9
Argument must be a list of numbers

Invalid case - empty list 
>>> average([]) # Test 10
Cannot find average of an empty list

"""


#---------------------------------------------------------
#
# Make this function robust to errors by catching
# exceptions and printing an error message as shown
# in the tests above


# A function that accepts a list of numbers and returns
# their average
#
def average(num_list):

    return float(sum(num_list) / len(num_list))



#---------------------------------------------------------
# This function executes the unit tests above when called.
# To see if your solution passes all the tests, just call
# the function below.
#
def test():
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print(testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE))

# Uncomment the following line to automatically call
# the test function whenever you run this file:
#test()


