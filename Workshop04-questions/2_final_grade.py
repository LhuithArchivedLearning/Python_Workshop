#---------------------------------------------------------
#
# Final grade
#
# QUT's default percentage cut-offs for the final grade
# awarded in a teaching unit are as follows.
#
#  Percentage   Grade
#   0 .. 24       1
#  25 .. 39       2
#  40 .. 49       3
#  50 .. 64       4
#  65 .. 74       5
#  75 .. 84       6
#  85 .. 100      7
#
# Notice that this is not a simple linear relationship.
# The first grade covers 25 percentage marks, the
# second 15, the third 10, and so on.  Therefore, to
# write some code to translate percentage marks into
# grades we will need to use one or more conditional
# statements.
#
# Below are some unit tests for a function called
# "final_grade" which accepts a percentage as its sole
# parameter and returns the corresponding grade.  Your
# job is to write the function which passes all these
# tests.  Note in the final two tests that if an
# invalid percentage is provided then the function
# returns -1, which cannot be a valid result, to flag
# the error.
#
# Also note that in cases where the final mark includes
# a fraction of a percent the mark is rounded off
# to the nearest whole number.
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
# Footnote: Although the ranges above are the default
# cut-offs, there is no guarantee they will used by a
# particular teaching unit in a particular semester. The
# Faculty can always choose to change the cut-offs at the
# end of the semester.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> final_grade(85) # Test 1. Normal case - high distinction, borderline
7

>>> final_grade(80) # Test 2. Normal case - distinction
6

>>> final_grade(74) # Test 3. Normal case - borderline credit
5

>>> final_grade(49.9) # Test 4. Normal case - borderline pass, floating point
4

>>> final_grade(49.1) # Test 5. Normal case - just failed
3

>>> final_grade(24.3) # Test 6. Normal case - low fail
1

>>> final_grade(10) # Test 7. Normal case - low fail
1

>>> final_grade(0) # Test 8. Boundary case - never showed up!
1

>>> final_grade(-1) # Test 9. Invalid case - mark too low
-1

>>> final_grade(110) # Test 10. Invalid case - mark too high
-1

"""

#---------------------------------------------------------
# A function which, when given a percentage, returns
# the corresponding grade.
#
#  Percentage   Grade
#   0 .. 24       1
#  25 .. 39       2
#  40 .. 49       3
#  50 .. 64       4
#  65 .. 74       5
#  75 .. 84       6
#  85 .. 100      7

import math

##### DEFINE YOUR final_grade FUNCTION HERE
def final_grade(grade):
    grade = round(grade);
    returngrade = 0;
    if grade >= 0.00 and grade <= 24.00 :
        returngrade = 1;
    elif grade >= 25.00 and grade <= 39.00 :
        returngrade = 2;
    elif grade >= 40.00 and grade <= 49.00 :
        returngrade = 3;
    elif grade >= 50.00 and grade <= 64.00 :
        returngrade = 4;
    elif grade >= 65.00 and grade <= 74.00 :
        returngrade = 5;
    elif grade >= 75.00 and grade <= 84.00 :
        returngrade = 6;
    elif grade >= 85.00 and grade <= 100.00 :
        returngrade = 7;
    else :
        returngrade = -1;
    return returngrade;

#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.
final_grade(24.3);
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
