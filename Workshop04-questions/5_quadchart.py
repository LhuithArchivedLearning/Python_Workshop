#---------------------------------------------------------------
#
# Quadchart
#
# A quadchart is a commonly-used decision making tool, applicable
# when a decision is based on two Boolean values.  In this
# exercise you will develop a function which makes a
# quadchart-based decision.
#
# Imagine that you need to decide what activity to perform today,
# based on two facts, whether or not the weather is nice and
# whether or not it's the weekend.  Your options could be
# presented as the following quadchart.
#
#                  Weather nice       Weather nasty
#                +------------------+------------------+
#                |                  |                  |
#  Weekend today | Go to the beach! | Catch a movie!   |
#                |                  |                  |
#                +------------------+------------------+
#                |                  |                  |
#  Weekday today | Daydream time    | Good day to work |
#                |                  |                  |
#                +------------------+------------------+
#
# Define a function which expects two Boolean arguments:
#   a value which is True if the weather is fine; and
#   a value which is True if it is the weekend.
# Depending on the weather and the day of the week, return
# an appropriate message according to the table above.
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
>>> today(True, True) # Test 1. Normal case
'Go to the beach!'

>>> today(True, False) # Test 2. Normal case
'Daydream time'

>>> today(False, True) # Test 3. Normal case
'Catch a movie!'

>>> today(False, False) # Test 4. Normal case
'Good day to work'

"""

#---------------------------------------------------------

##### DEFINE YOUR today FUNCTION HERE

def today(weather, weekend):
    if weather and weekend:
        return 'Go to the beach!';
    elif not(weather) and weekend:
        return 'Catch a movie!';
    elif not(weather) and not(weekend):
        return 'Good day to work';
    elif weather and not(weekend):
        return 'Daydream time';
    


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))

