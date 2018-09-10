#---------------------------------------------------------
#
# A String Module
#
# So far we have been defining individual functions.  In
# this exercise you will create a module containing three
# distinct functions for manipulating text strings.  This
# module will then be used in the subsequent "Telegrams"
# exercise.
#
# Hint: You will find some very helpful string methods for
# this exercise in the Python Standard Library
# reference manual.
#
# The tests below tell us how your functions are expected to
# behave when called.  After you've written your functions,
# confirm that they work correctly by (a) running this module
# so that your functions are defined and then (b) copying
# each of the function calls in the set of tests into the
# shell to see if the right answer is returned.  Obviously
# if you don't get the expected answers then you'll need
# to modify your code until you do.
# 
# Finally, the main program of this file runs the tests
# automatically.  The code is commented out, but if you
# want to run all the tests automatically, just uncomment
# the code and run this file.  Of course, you should pass
# all the tests in order to complete this exercise.  Note
# that even if the main program is uncommented, the tests
# will not be executed if this module is imported into
# another, i.e., if it is not the "main" program.
#



#---------------------------------------------------------
# These are the tests your three functions must pass.  We
# have included a number of tests for each of the three
# functions you have to write.
#
""" 
Part 1: Tests for the convert_to_upper function

>>> convert_to_upper('what') # Test A1 - normal case (all lower case chars)
'WHAT'

>>> convert_to_upper('WHY') # Test A2 - normal case (all upper case chars)
'WHY'

>>> convert_to_upper('Which, Who, When') # Test A3 - normal case (mixed case chars)
'WHICH, WHO, WHEN'

>>> convert_to_upper('') # Test A4 - boundary case (empty string)
''


Part 2: Tests for the remove_spaces function

>>> remove_spaces('H E L P !!') # Test B1 - normal case (multiple spaces)
'HELP!!'

>>> remove_spaces('  The End   ') # Test B2 - normal case (leading and trailing spaces)
'TheEnd'

>>> remove_spaces('ThisOneIsOkAsIs') # Test B3 - boundary case (no spaces)
'ThisOneIsOkAsIs'

>>> remove_spaces('') # Test B4 - boundary case (empty string)
''

>>> remove_spaces('    ') # Test B5 - boundary case (only spaces)
''


Part 3: Tests for the replace_stops function

>>> replace_stops('Stop.') # Test C1 - normal case (one occurrence)
'StopSTOP'

>>> replace_stops('Need help. Reply urgently.') # Test C2 - normal case (two occurrences)
'Need helpSTOP Reply urgentlySTOP'

>>> replace_stops('...') # Test C3 - unusual case (nothing but full stops)
'STOPSTOPSTOP'

>>> replace_stops('Hello world, how are you today?') # Test C4 - boundary case (no full stops)
'Hello world, how are you today?'

"""


#---------------------------------------------------------
# Define a function which, when given a string, returns
# it with all alphabetic characters in upper case.
# (Hint: This can be done trivially using Python's
# built-in "upper" method for strings.)

#### DEFINE YOUR convert_to_upper FUNCTION HERE
pass


#---------------------------------------------------------
# Define a function which, when given a string, returns
# it with all blank spaces removed.
# (Hint: This can be done easily using Python's built-in
# "replace" method for strings.)

#### DEFINE YOUR remove_spaces FUNCTION HERE
pass


#---------------------------------------------------------
# Define a function which, when given a string, returns
# it with all occurrences of full stops '.'
# replaced with the word 'STOP'.

#### DEFINE YOUR replace_stops FUNCTION HERE
pass


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run, provided it is being executed as a main
# program and not as a module in another program.
# Uncomment the code below if you want to run the tests
# automatically.

##if __name__ == '__main__':
##    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
##    print(testmod(verbose = False,
##                  optionflags = REPORT_ONLY_FIRST_FAILURE))
