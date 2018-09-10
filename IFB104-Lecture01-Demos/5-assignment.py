######################################################################
#
#  Demonstration - More Lessons in Assignment
#
#  Note: This file contains various statements and expressions to be
#  evaluated.  If you "run" this file in IDLE only the lines
#  containing calls to the "print" function will produce text in the
#  shell window, even though all the statements will be executed.


######################################################################
# Assignment allows us to remember values for use in subsequent
# expressions:

width = 2  # store the width of a cupboard (in metres)

height =  3  # store its height

depth = 1.5  # store its depth

footprint = width * depth # store its footprint (floor area)

print("Floor space is", footprint, "square metres")

print("Volume is", footprint * height, "cubic metres")

print() # print a blank line to separate the examples


######################################################################
# We can assign to a variable more than once:

temperature = 25 # initialise the variable

print("The temperature is", temperature, "degrees")

temperature = 10 # assign a new value to the same variable

print("The temperature now is", temperature, "degrees")

temperature = temperature + 6

print("The temperature has gone up to", temperature, "degrees")

print()


######################################################################
# The type of the target variable (on the left) depends on the
# type of the source expression (on the right):

length = 4 # assign an integer value to the variable

print("Variable length's value is", length, "and its type is", type(length))

length = 3.5 # assign a floating point value to the variable

print("Variable length's value is", length, "and its type is", type(length))

print()

# Note that although Python allows us to change the type of a variable
# this is confusing - you should use each variable for just one purpose
# and always make it hold values of the same type


######################################################################
# Assignments involving simple types just copy the value of one
# variable into another, leaving the "source" variable (on the right)
# unaffected

number_of_books = 5

number_of_chairs = number_of_books + 1

print("There are", number_of_books, "books and", number_of_chairs, "chairs")

number_of_books = 13 # changing this variable doesn't affect number_of_chairs

print("There are", number_of_books, "books and", number_of_chairs, "chairs")

print()


######################################################################
# As a more meaningful example, imagine that you wanted to calculate
# the Goods and Services Tax paid on your purchases at the
# supermarket.  Assume GST is mandated to be 10% of an item's
# untaxed cost - this means that it's one eleventh of the taxed cost.

# The following values are how much you paid for certain items at
# the supermarket:

coca_cola = 2.70 # dollars
donuts = 3.50 # dollars
ice_cream = 5.25 # dollars

# One way to calculate the GST is as follows:

tax_a = (coca_cola / 11.0) + (donuts / 11.0) + (ice_cream / 11.0) # dollars

# Another way is like this:

tax_b = (coca_cola + donuts + ice_cream) / 11.0 # dollars

# But both produce the same answer (rounded to two decimal places):

print('The first GST calculation produced', round(tax_a, 2), 'dollars')
print('The second GST calculation produced', round(tax_b, 2), 'dollars')

print()


######################################################################
# To confirm that you understand the way assignment of values to
# variables works, work out what value will be printed by the
# last line below.  Uncomment the "print" statement and run this
# file to check your answer.

first = 3
second = 2
third = first * second
first = first + third
mystery = first - 1  # What value is stored in variable "mystery"?

# print('The mystery value is', mystery)
