# Volume of a sphere
#
# THE PROBLEM
#
# Assume the following value has already been entered into the
# Python interpreter, denoting the radius of a sphere:

radius = 4 # metres

# Also assume that we have imported the existential constant "pi"
# from the "math" library module:

from math import pi

# Write an expression, or expressions, to calculate the volume
# of the sphere.  Print the result in a message to the screen,
# which for the radius above should be around 268 metres cubed.
# (Hint: The volume of a sphere of radius r is four-thirds times
# pi times r cubed.)

v = 4/3 * ((pi * (radius ** 3)))

print(v)
