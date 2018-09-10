#---------------------------------------------------------
#
# Number of digits
#
# As an exercise in recursion, develop a recursive function
# with one parameter, an integer, that returns the number
# of digits in that integer.
#
# Hint: Dividing a decimal integer number by ten reduces
# the number of digits it contains by one.
#

 
#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> num_digits(142) # Test 1 (normal case)
3

>>> num_digits(1000000) # Test 2 (normal case)
7

>>> num_digits(-5461) # Test 3 (negative case)
4

>>> num_digits(-5) # Test 4 (negative case)
1

>>> num_digits(1) # Test 5 (boundary case)
1

>>> num_digits(0) # Test 6 (boundary case)
1

"""


#---------------------------------------------------------
#
# Observation: You can solve the problem of returning the
# number of digits in a given integer value by defining
# a recursive function with three alternative actions.
#
# a. (recursive case 1) Integer is negative: Return the
#    number of digits in the corresponding positive
#    integer value
# b. (base case) Integer has only one digit: Return 1
# c. (recursive case 2) Otherwise: Return 1 plus
#    the number of digits in the given integer
#    divided by 10
#


def num_digits(num) :
    num = abs(num);

    if num == 0:
        return 1;
    elif num < 10:
        return 1;
    else :
        return (1 + num_digits(num//10));
    



#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

print(num_digits(22));

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = True,
              optionflags = REPORT_ONLY_FIRST_FAILURE))


