#---------------------------------------------------------
#
# Alert date printer
#
# The following function accepts three positive
# numbers, expected to denote a day, month and year, and
# prints them as a date in the usual format.
#
# However, this function can be misused by providing
# numbers that don't form a valid date.
#
# Your task is to add assertions to the function which raise
# an AssertionError exception if the given numbers cannot
# be a valid A.D. date, e.g., if the month value is greater
# than 12 or if the year is negative.  (To keep the exercise
# simple you don't need to worry about leap years or the
# different number of days in different months, although a
# "real" function along these lines would need to do so.)
# The test cases below show the messages that should be
# returned with an exception violation.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
---------- "Normal" cases, with expected inputs ----------

Normal case
>>> print_date(9, 12, 2012) # Test 1
9/12/2012

Normal case
>>> print_date(1, 1, 1960) # Test 2
1/1/1960

Normal case
>>> print_date(28, 2, 1950) # Test 3
28/2/1950

-------- "Invalid" cases, with unexpected inputs ---------

Invalid case - impossible month
>>> print_date(13, 0, 2012) # Test 4
Traceback (most recent call last):
AssertionError: Invalid month: 0

Invalid case - impossible A.D. year (but could be B.C.?)
>>> print_date(6, 5, -10) # Test 5
Traceback (most recent call last):
AssertionError: Invalid year: -10

Invalid case - impossible day
>>> print_date(-2, 3, 2001) # Test 6
Traceback (most recent call last):
AssertionError: Invalid day: -2

"""


#---------------------------------------------------------
#
# Make the following function alert its caller to
# invalid parameters by raising an AssertionError
# exception.
#

# A function to print a given date.
#
def print_date(day, month, year):

    # Print the date
    print(str(day) + '/' + str(month) + '/' + str(year))
 

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
# test()
