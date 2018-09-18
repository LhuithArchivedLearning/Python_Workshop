#----------------------------------------------------------------
#
# Number of occurrences of a phrase in a file
#
# Define a function which accepts two string-valued arguments,
# the name of a text file and a string representing a particular
# phrase we expect to occur in the file.  The function must
# return the number of occurrences of that phrase in the file.
#
# NB: The capitalisation of the phrase shouldn't matter.
#
# NB: Keep in mind that the phrase may appear more than once
# on a given line.
#
# Observation: If the phrase is a long one containing multiple
# words it may be split across two or more lines.  For the
# purposes of this exercise we will not attempt to find such
# occurrences, only those where the phrase appears wholly within
# one line.
#


#----------------------------------------------------------------
#
# Some tests
#
"""
>>> num_occurrences('AnimalFarm-Chapter1.txt', 'Mr. Jones') # Test 1
4

>>> num_occurrences('AnimalFarm-TheWholeBook.txt', 'Mr. Jones') # Test 2
23

>>> num_occurrences('AnimalFarm-TheWholeBook.txt', 'Comrades') # Test 3
56

>>> num_occurrences('AnimalFarm-TheWholeBook.txt', 'Internet') # Test 4
0
"""


#----------------------------------------------------------------
#

##### DEVELOP YOUR num_occurrences FUNCTION HERE


#----------------------------------------------------------------
# This main program executes the tests above when this
# file is run.  Uncomment the following code if you want to run
# the tests automatically.

##from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
##print (testmod(verbose = False,
##              optionflags = REPORT_ONLY_FIRST_FAILURE))

