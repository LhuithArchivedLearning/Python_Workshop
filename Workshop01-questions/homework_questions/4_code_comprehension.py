# Code comprehension questions
#
# The following small exercises are designed to help you confirm
# that you understand the way computer languages evaluate
# expressions.  There is no "solution" file for this question - you
# get the answers by "running" this file and seeing what it
# prints.  However, DON'T do so until you've answered
# the questions yourself!


# Question 1:
#
# Without running the program, work out what value the following
# code segment will print.  (The code is meaningless, but it helps
# confirm that you understand the relationship between variables,
# values and sequences of assignments.)

a = 5
b = 2
b = a # a's value is copied to b, but variable a's value is unchanged 
b = b + 3 # b's new value is defined using its old value
a = b * b
print(a - b) # What value is printed?

print() # Print a blank line as a separator


# Question 2:
#
# Without running the program, work out what final value the
# following code will print.  The lessons here are that:
#
# a) you have a free choice of variable names;
# b) your choice of variable names has no effect on the way
#    the computer does its calculations because it doesn't
#    understand what the names mean; and
# c) you are well-advised to choose sensible variable names
#    that make your code easier to understand, unlike the
#    misleading choices of variable names below.

x = 10
y = 5
z = 6
x_squared = x + x # Does the variable name describe its value?
y_times_2 = z / 2
x_squared_plus_y_times_2 = x_squared * y_times_2

print('Variable x equals 10 and variable y equals 5,')
print('so x squared plus y times 2 equals', x_squared_plus_y_times_2)
print('(or does it?)')

