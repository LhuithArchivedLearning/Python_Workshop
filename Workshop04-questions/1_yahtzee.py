#---------------------------------------------------------
#
# Yahtzee
#
# In the game "Yahtzee" five dice are rolled and if all
# five have the same value the player scores 50, but
# otherwise zero.
#
# Define a function with five integer parameters, each
# representing a die's face value (i.e., between 1 and 6).
# The function should return 50 if all the supplied
# arguments are the same value, otherwise it should
# return 0.
#
# Trivia: The singular of "dice" is "die".
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
>>> yahtzee(5, 5, 5, 5, 5) # Test 1. Normal case - yahtzee with 5s
50

>>> yahtzee(1, 1, 1, 1, 1) # Test 2. Normal case - yahtzee with 1s
50

>>> yahtzee(1, 2, 3, 4, 5) # Test 3. Normal case - no yahtzee, all different numbers
0

>>> yahtzee(1, 1, 1, 1, 2) # Test 4. Normal case - no yahtzee, 4 numbers the same, last one different
0

>>> yahtzee(2, 1, 1, 1, 1) # Test 5. Normal case - no yahtzee, 4 numbers the same, first one different
0

>>> yahtzee(1, 1, 2, 1, 1) # Test 6. Normal case - no yahtzee, 4 numbers the same, middle one different
0

>>> yahtzee(1, 1, 2, 3, 1) # Test 7. Normal case - no yahtzee, 3 numbers the same
0

>>> yahtzee(1, 3, 2, 3, 2) # Test 8. Normal case - no yahtzee, 2 lots of 2 numbers the same
0

>>> yahtzee(5, 5, 5, 5, 5) == 50 # Test 9. Check value is returned not printed
True

"""


#---------------------------------------------------------

##### DEFINE YOUR yahtzee FUNCTION HERE
def yahtzee(a,b,c,d,e):
    result = a == a and b == a and c == a and d == a and e == a;
    if result :
        return 50
    else :
        return 0;
    
print(yahtzee(1, 3, 2, 3, 2));

#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))


