#---------------------------------------------------------
#
# Is it a palindrome?
#
# A palindrome is a sentence that reads the same backwards
# and forwards (ignoring capitalisation, punctuation and
# spaces).  See the test cases below for examples.
#
# Define a function with one parameter, a non-empty string,
# which returns True or False depending on whether or not
# that string is a palindrome.
#
# NB: To complete this exercise you must first complete
# the "Get Alphabetics" exercise, because we will import
# your solution to that exercise into this one.
#


# TESTCASES-----------------------------------------------
""" 

>>> is_palindrome('Hannah') # Test 1 (normal case)
True

>>> is_palindrome('Annie') # Test 2 (normal case)
False

>>> is_palindrome('amanaplanacanalpanama') # Test 3 (normal case)
True

>>> is_palindrome('A man, a plan, a canal, Panama!') # Test 4 (normal case)
True

>>> is_palindrome("Madam! In Eden, I'm Adam!") # Test 5 (normal case)
True

>>> is_palindrome("May a moody baby doom a yam?") # Test 6 (normal case)
True

>>> is_palindrome("A Toyota's a Toyota!") # Test 7 (normal case)
True

>>> is_palindrome("Was it a car or a cat I saw?") # Test 8 (normal case)
True

>>> is_palindrome('Frustrated palindrome') # Test 9 (normal case)
False

>>> is_palindrome('a') # Test 10 (boundary case)
True

"""

#---------------------------------------------------------
#

# Import your function for extracting the alphabetic
# characters from a string
from get_alphabetics import *

def is_palindrome(string) :
    test = get_alphas(string);
    result = False;
    #This is extended slice syntax.
    #It works by doing [begin:end:step] -
    #by leaving begin and end off and specifying a step of -1,
    #it reverses a string
    reversetest = test[::-1];
    
    if (test == reversetest) :
        result = True;
        

    
    
    return result;



#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = True,
              optionflags = REPORT_ONLY_FIRST_FAILURE))


