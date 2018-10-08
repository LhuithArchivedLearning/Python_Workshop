#---------------------------------------------------------
#
# Robust temperature conversion
#
# The function below converts a given temperature
# in Fahrenheit to Celsius (as a floating point number).
# Recall that:
#
#   Temp_in_Celsius = (Temp_in_Fahrenheit - 32) * (5 / 9)
#
# However, the function crashes when given non-numeric
# parameters.  Your job is to add exception handling code
# to print an appropriate message when an input of the
# wrong type is supplied as shown in the tests below.  NB:
# The Python interpreter will throw a "TypeError" exception
# if it is asked to perform arithmetic using a non-numeric
# value, so this is the exception you must "catch".
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
---------- Normal cases, with expected inputs ----------

Normal case - freezing point
>>> fahrenheit_to_celsius(32) # Test 1
0

Normal case - boiling point
>>> fahrenheit_to_celsius(212) # Test 2
100

Normal case - benchmark of a hot day!
>>> fahrenheit_to_celsius(100) # Test 3
38

Normal case
>>> fahrenheit_to_celsius(70) # Test 4
21

Normal case 
>>> fahrenheit_to_celsius(86) # Test 5
30

Special case - same result
>>> fahrenheit_to_celsius(-40) # Test 6
-40

-------- Invalid cases, with unexpected inputs ---------

Invalid case - incorrect input type
>>> fahrenheit_to_celsius('8') # Test 7
Fahrenheit value must be a numeric type

Invalid case - incorrect input type
>>> fahrenheit_to_celsius([1]) # Test 8
Fahrenheit value must be a numeric type

"""



#---------------------------------------------------------
#
# Make this function robust against invalid parameters
# by catching TypeError exceptions and printing a meaningful
# error message as shown in the tests above
#

# A function to convert a given temperature
# in Fahrenheit to Celsius
#
def fahrenheit_to_celsius(fahrenheit):

    return round((fahrenheit - 32) * (5 / 9))



#---------------------------------------------------------
# This function executes the unit tests above when called.
# To see if your solution passes all the tests, just call
# the function below.
#
def test():
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print(testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE))

# Uncomment the following line to call the test function
# automatically whenever this program is run:
#test()
