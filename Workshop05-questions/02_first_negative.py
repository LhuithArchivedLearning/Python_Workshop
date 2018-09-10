#---------------------------------------------------------
#
# Find first negative
#
# Define an iterative function with one parameter, a
# list of numbers. The function should return the first
# negative number in that list, or return 0 if there
# are no negative numbers.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
Normal case - different numbers
>>> first_negative([1, 2, 3, -4, 5, 6]) # Test 1
-4

Normal case - all the same negative number
>>> first_negative([-2, -2,- 2, -2]) # Test 2
-2

Normal case - some duplicates
>>> first_negative([3, -14, 1, -20, 3, -14, -20, 6]) # Test 3
-14

Normal case - no negatives
>>> first_negative([4, 1, 2, 3, 4, 2, 6]) # Test 4
0

Normal case - all negatives
>>> first_negative([-3, -1, -2, -3, -4, -2, -6]) # Test 5
-3

Normal case - check for returned value, rather than printed
>>> first_negative([7, -3, -4, 5]) == -3 # Test 6
True

"""


#---------------------------------------------------------
#

##### DEVELOP YOUR first_negative FUNCTION HERE

def first_negative(val_list) :

    for element in val_list :
        if element < 0 :
            return element;
        
    return 0;

#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
