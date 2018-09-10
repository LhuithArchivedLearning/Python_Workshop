#---------------------------------------------------------
#
# Telegrams
#
# Define a function with one parameter, a string representing
# a message.  Your function is to return that message in capital
# letters, with every full-stop replaced with "STOP", and 
# all spaces removed, so that it looks like an old-fashioned
# telegram.  (Telegrams were sent on equipment that could transmit
# upper-case letters only.  The operator would cut the words
# from a ticker-tape strip and paste them onto a piece of paper
# to create the telegram for delivery to the recipient.)
#
# As an exercise in reuse of functions, you must do this using
# your solution to the preceding "string module" exercise.  Import
# and use your previously defined functions "replace_stops",
# "remove_spaces" and "convert_to_upper" to implement your
# "telegram" function.
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
>>> telegram('Urgent Message.  Please Read.') # Test 1 - normal case
'URGENTMESSAGESTOPPLEASEREADSTOP'

>>> telegram('Do not stop.') # Test 2 - normal case
'DONOTSTOPSTOP'

>>> telegram('Return home. Explain later.') # Test 3 - normal case
'RETURNHOMESTOPEXPLAINLATERSTOP'

>>> telegram('URGENTMESSAGEPLEASEREAD') # Test 4 - all caps, no spaces
'URGENTMESSAGEPLEASEREAD'

>>> telegram('UrgentMessagePleaseRead') # Test 5 - mixed case, no spaces
'URGENTMESSAGEPLEASEREAD'

>>> telegram(' . . . ') # Test 6 - unusual case: only stops and spaces
'STOPSTOPSTOP'

>>> telegram('') # Test 7 - boundary case: empty string 
''

"""


#---------------------------------------------------------
# Import your solutions from the "string module"
# exercise.  (Change the file name if necessary.)
#
from I_string_module import *


#---------------------------------------------------------
# Define a function which, when given a string, returns
# it in telegram format, i.e., all in caps, with full-stops
# replaced with the word "STOP" and spaces removed.
#

#### DEFINE YOUR telegram FUNCTION HERE
pass


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

##from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
##print(testmod(verbose = False,
##              optionflags = REPORT_ONLY_FIRST_FAILURE))
