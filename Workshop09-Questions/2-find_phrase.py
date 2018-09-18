#----------------------------------------------------------------
#
# Find a phrase in a file
#
# Define a function which accepts two string-valued arguments,
# the name of a text file and a string representing a particular
# phrase we expect to occur in the file.  The function must
# print each line in the file where the phrase appears.  NB: The
# capitalisation of the phrase shouldn't matter, so you will
# find Python's "lower" method useful.
#
# Observation: If the phrase is a long one containing multiple
# words it may be split across two or more lines.  For the
# purposes of this exercise we will not attempt to find such
# occurrences, only those where the phrase appears wholly within
# one line.
#


#----------------------------------------------------------------
#

##### DEVELOP YOUR find_phrase FUNCTION HERE


#----------------------------------------------------------------
#
# Some tests - uncomment as needed.
#
find_phrase('AnimalFarm-Chapter1.txt', 'Major') # should produce 11 lines
# find_phrase('AnimalFarm-Chapter1.txt', 'Old Major') # should produce 3 lines
# find_phrase('AnimalFarm-TheWholeBook.txt', 'Snowball!') # should produce 2 lines
# find_phrase('AnimalFarm-TheWholeBook.txt', 'wheat crop') # should produce 2 lines
