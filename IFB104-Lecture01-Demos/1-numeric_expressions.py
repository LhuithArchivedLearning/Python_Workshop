######################################################################
#
#  Demonstration - Numeric expressions (using the Python
#                  interpreter as a calculator)
#
#  Note: This file contains various expressions to be evaluated.
#  If you "run" this file in IDLE nothing will appear to happen,
#  because the expressions are evaluated but the results aren't
#  used anywhere.  To see the value of an expression below you
#  can either:
#
#    a) copy it into Idle's interpreter window and hit the Enter
#       key; or
#
#    b) place brackets around the expression below, then precede the
#       expression with "print", which tells IDLE to display the result
#       when the file is run, and then run the file.
#
#  Most importantly, experiment with your own expressions.  This
#  python doesn't bite!


# We can type "whole number" expressions into the Python interpreter
# and get answers in exactly the way we would with a calculator:

4 + 5

9 * 7

18 // 7  # integer division

18 // -7

4 ** 3  # i.e., four cubed

8 * 4 + 2


# Brackets can be used to override the default precedence of
# operators, as with normal mathematical expressions:

8 * (4 + 2)  # returns a different result than the expression above


# Special operations, that you may find on a scientific calculator,
# are available as predefined "functions":

6 + abs(-4)  # the "abs" function returns the absolute value

abs(3 * -4)


# Infrequently-used operations are not loaded into the Python
# interpreter by default, so we need to import them from
# a "library" of functions before using them:

from math import sqrt  # load the square root function

sqrt(16)

from math import floor, ceil  # load the ceiling and floor functions

ceil(5.4)  # the ceiling function rounds up

floor(5.4)  # the floor function rounds down


# Numerical expressions can also have a fractional part:

4.2 + 5.3

18 / 7 # floating point division (compare with 18 // 7)

