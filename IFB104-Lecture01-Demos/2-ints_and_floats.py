######################################################################
#
#  Demonstration - Integers versus floating point numbers
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


# Floating point numbers are distinguished from integers by
# having a fractional part, even if it's zero:

type(4)             # print(type(4))

type(9.3)           # print(type(9.3))

type(4.5 + 6.7)

type(3.0 * 2.0)


# Different arithmetic operators return different types
# of result:

25 // 8  # returns an integer

25 / 8 # returns a floating point number

25.0 // 8.0  # returns a floating point number

3 * (4 + 5.0)  # returns a value of which type?


# Although integer 1 is numerically equal to floating point number
# 1.0, they do not denote the same data value:

1 == 1.0  # tests to see if 1 and 1.0 are numerically equal

1 is 1.0  # tests to see if 1 and 1.0 are the same "object"


# If necessary we can force a value to be either an integer or
# floating point number:

float(4 + 7)

int(4.0 ** 2.0)


# But converting a floating point to an integer loses the fractional
# part:

6.3 + 2.5  # is a value with a fractional part

int(6.3 + 2.5)  # chops off the fractional part

round(6.3 + 2.5)  # returns an integer, not a floating point number


# Base-10 floating point numbers are encoded by your computer
# as finite approximations in base-2 (binary) arithmetic which can
# lead to machine-specific inaccuracies and "rounding errors":

2 / 3  # can't encode the infinite fractional part

(0.1 * 6) / 0.1  # doesn't return 6 exactly (on my computer at least!)
