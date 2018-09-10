#--------------------
# Eight Eights
#
# Here's a challenging little puzzle you can solve with the
# help of Python.  Can you devise a numeric expression in
# which the digit 8 appears exactly 8 times and which
# evaluates to 1000?  To check your answer, evaluate the
# expression in Python and print the result.  There are many
# different solutions to this problem, so see if the other
# groups in your class come up with different answers.


#--------------------
# Integer version: Solve the problem using only the digit 8
# and the integer arithmetic operators +, -, * and //.  (You
# don't have to use them all.)  The result should be the
# integer value 1000.

print(8 * (8 * 8 + 8 * 8) - 8 - 8 - 8);

#--------------------
# Floating point version: Solve the problem using only the
# digit 8, decimal points, floating point arithmetic (+, -,
# * and /), the square root function and the exponentiation
# operator **.  (Again you don't have to use them all.)  In
# this case the result should be the floating point
# value 1000.0, but remember that the rounding errors inherent
# in computer arithmetic might not produce a mathematically
# precise result!

from math import sqrt
##### Put the code to evaluate and print your expression here

print(8.0 * (8.0 * 8.0 + 8.0 * 8.0) - 8.0 - 8.0 - 8.0);

