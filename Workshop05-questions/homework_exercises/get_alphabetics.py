#---------------------------------------------------------
#
# Get alphabetic characters
#
# Define a function which, given a character string,
# returns the string with all non-alphabetic characters
# removed and all remaining characters in lower case.
#
# NB: We will import your solution to this exercise
# into the "Is Palindrome?" exercise, so you must
# complete this one first.
#
# Hint: You will find Python's built-in "lower" and
# "isalpha" functions most helpful.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
Normal case - contains non-alphabetics
>>> get_alphas(':-) Smiley says " HI! "') # Test 1
'smileysayshi'

Normal case - sentence with punctuation
>>> get_alphas('Last boarding call for Mr. Dobalina, Mr. Bob Dobalina!')
'lastboardingcallformrdobalinamrbobdobalina'

Normal case - contains only non-alphabetics
>>> get_alphas(';->') # Test 3
''

Normal case - contains only alphabetics
>>> get_alphas('abc') # Test 4
'abc'

Boundary case - empty string
>>> get_alphas('') # Test 5
''

"""


#---------------------------------------------------------
#

def get_alphas(string) :
    result = '';

    for char in string :
        if char.isalpha() :
            charval = char.lower();
            result += charval;
        else :
            continue
        
    return result;

        

#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

get_alphas('');
get_alphas('Last boarding call');

if __name__ == '__main__':
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print(testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE))

