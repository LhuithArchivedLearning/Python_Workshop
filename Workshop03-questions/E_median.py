#---------------------------------------------------------
#
# Median
#
# The median of a set of values is a measure of central
# tendency like the average, but has the advantage of
# being less affected by outliers.  Define a function
# with one parameter, a non-empty list, which returns
# the median item in that list.
#
# For the purpose of this exercise, the median item is
# the middle value when the list is arranged in ascending
# order.
#
# (Comment: In fact, the mathematical definition of a
# "median" is the middle value when the given list has an
# odd length, but is the average of the two values in the
# middle when the list contains an even number of items.
# We ignore this fine distinction here.  All of the lists
# in our test suite contain an odd number of items,
# which makes the problem easier to solve.)
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
 

#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> median([8, 5, 1, 2, 3]) # Test 1 - normal case (list of positive numbers)
3

>>> median([-5, -6, -10, -8, -7, -8, -1]) # Test 2 - normal case (negatives)
-7

>>> median([1, 1, 1, 1, 1, 1, 1, 1, 1]) # Test 3 - normal case (all same number)
1

>>> median([0, 1, 67899, 2, 100000, 5, 4, -54321, 3]) # Test 4 - normal case (small and large numbers)
3

>>> median(['Donna', 'Kim', 'Alice', 'Joe', 'Xavier']) # Test 5 - normal case (list of strings)
'Joe'

>>> median([99]) # Test 6 - boundary case (list of length one)
99

"""


#---------------------------------------------------------
# Solution strategy:
# 1. Sort the given list
# 2. Calculate the position of the middle value
# 3. Return the value at that position
#

#### REPLACE THE "DO NOTHING" STATEMENT BELOW
##### WITH YOUR median FUNCTION DEFINITION
def median(l):
    l.sort();
    middle = float(len(l))/2.0;
    #its an even number
    if(middle % 2 != 0):
        return l[round(middle -.5)];
    else :
        return l[middle];
    

print (median(['Donna', 'Kim', 'Alice', 'Joe', 'Xavier']));
#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
