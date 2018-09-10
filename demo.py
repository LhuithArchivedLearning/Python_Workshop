#Correctness Test for our function

"""
This function is supposed to calculate a volume
here are some tests to ensure it is working

Test 1 - no params
>>> cylinder_volume()
3

Test 2 - 1 param
>>> cylinder_volume(1)
3

Test 3 - 1 param on right side
>>> cylinder_volume(height = 2)
6

Test 4 - 2 params
>>> cylinder_volume(5,6)
478

"""

#calculate the volume of a cylinder

#how much room do we have in a tank of radius 5 metres and height of 10 metres

from math import pi

#function definition
def cylinder_volume(rad = 1, height = 1) :
    return int ((pi * (rad ** 2)) * height);

#run the tests automatically
from doctest import testmod
print(testmod(verbose = True));

#print("Tanks volume is ", cylinder_volume(3, 2), "metres cubed");

