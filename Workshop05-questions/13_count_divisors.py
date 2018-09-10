#---------------------------------------------------------
#
# Count divisors
#
# A "divisor" of a natural number is a number less than or
# equal to the integer that divides the number without a
# remainder.  For instance, 4 is a divisor of 12 because
# 12 / 4 = 3 with nothing left over, but 7 is not a
# divisor of 12 because 12 / 7 = 1 with 5 left over.
#
# Define a function to count the divisors of a given
# natural number and return the result.  For instance, 12
# has 6 divisors (namely 1, 2, 3, 4, 6 and 12).
#
# Observation: Every positive integer has itself and 1 as
# divisors.
#
# Hints:
#
# * Given a numerator n and and a denominator d, then
#   "n % d" returns the remainder after integer
#   division in Python.  If this value is 0 then
#   d must be a divisor of n.
#
# * This problem can be solve using a FOR loop, a
#   WHILE loop or recursion, but is probably easiest
#   using a FOR loop.

 
#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> count_divisors(10) # Test 1 (normal case)
4

>>> count_divisors(4) # Test 2 (normal case)
3

>>> count_divisors(24) # Test 3 (normal case)
8

>>> count_divisors(100) # Test 4 (normal case)
9

>>> count_divisors(1) # Test 5 (boundary case)
1

>>> count_divisors(7) # Test 6 (prime number)
2

"""


#---------------------------------------------------------
#

##### DEVELOP YOUR count_divisors FUNCTION HERE



#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
##from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
##print(testmod(verbose = False,
##              optionflags = REPORT_ONLY_FIRST_FAILURE))

