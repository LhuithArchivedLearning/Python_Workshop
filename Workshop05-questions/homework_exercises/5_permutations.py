#---------------------------------------------------------
#
# Permutations
#
# Develop a function to calculate how many ways a number 
# of items can be arranged in a limited number of spaces (e.g.,
# how many ways books arranged on a bookshelf).
#
# The function should expect two numeric arguments, one representing
# the number of items, and the other representing the number of spaces
# available in which to place those items.  Assume the number of
# items is greater than or equal to the number of spaces.
#
# For example, the three letters x, y and z can be arranged
# in two spaces (i.e., in pairs) six different ways:
# xy, xz, yx, yz, zx and zy.
#
# Similarly, the number of ways 6 items can be arranged in 3 spaces
# is 6 x 5 x 4 = 120.  The number of ways 10 items can be
# arranged in 4 spaces is 10 x 9 x 8 x 7 = 5040.
#
# This problem can be solved using a FOR loop, WHILE loop or
# a recursive function.  A recursive solution involves the
# least code, so is recommended here.
#

#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
Normal case: Three items in two places
>>> permutations(3, 2) # Test 1
6

Normal case: Six items in six places
>>> permutations(6, 6) # Test 2
720

Normal case: Six items in one place
>>> permutations(6, 1) # Test 3
6

Abnormal case: Insufficient items to fill the places
>>> permutations(2, 6) # Test 4
0

Normal case: Twenty items in five places
>>> permutations(20, 5) # Test 5
1860480

Boundary case: One space, one item
>>> permutations(1, 1) # Test 6
1

Boundary case: No spaces so only one arrangement possible
>>> permutations(3, 0) # Test 7
1

"""

#---------------------------------------------------------
#
# Suggested solution strategy: Your recursive function
# should have two alternative actions.
#
# a. (base case) If there are zero spaces avalable
#    return 1 (because there is only one arrangement
#    possible)
# b. (recursive case) Otherwise return the number of
#    items multiplied by the number of permutations
#    possible for one less item and one less space
#    (since we've just chosen one item and consumed
#    one space)
#

def permutations(items, spaces) :
    if spaces == 0 :
        return 1;
    else :
        return (items) * permutations(items - 1, spaces - 1);
    


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))

