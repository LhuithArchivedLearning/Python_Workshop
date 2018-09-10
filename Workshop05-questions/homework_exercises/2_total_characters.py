#---------------------------------------------------------
#
# Total Characters
#
# Recall that you can get the number of characters in
# a string using Python's built-in "len" function.
# Consider now the problem of finding the total number
# of characters in a list of strings.
#
# Define an iterative function to count the number of
# characters in a given list of words.  The function
# should have one parameter, a list of strings, and
# should return the total number of characters in the
# whole list of strings.
#

 
#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
Normal case
>>> total_characters(['abc', 'xyz']) # Test 1
6

Normal case
>>> total_characters(['abc', 'xyz', '', 'whatever']) # Test 2
14

Normal case
>>> total_characters(['Excellent', 'Exquisite', 'Exceptional', 'Flawless']) # Test 3
37

Normal case - same characters as previous test, but as one word
>>> total_characters(['ExcellentExquisiteExceptionalFlawless']) # Test 4
37

Boundary case - empty list
>>> total_characters([]) # Test 5
0

Boundary case - list of empty strings
>>> total_characters(['', '']) # Test 6
0

Boundary case - list of spaces (which are characters!)
>>> total_characters([' ', '      ']) # Test 7
7

"""


#---------------------------------------------------------
#

def total_characters(array) :
    count = 0

    for element in array :
        count += len(element);

    return count;



#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))


