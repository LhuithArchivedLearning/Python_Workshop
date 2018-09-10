#----------------------------------------------------------------
#
# "... And here's the number you first thought of!"
#
# In this exercise you will practice implementing a simple
# "algorithm" (a series of instructions for completing a task)
# in Python.  You will implement a simple mathematical puzzle in
# two different ways.
#
# The scenario: You have probably encountered one of those tricks
# in which someone asks you to think of a number, performs some
# seemingly-complicated series of calculations on it, and then
# miraculously arrives back at the number you first thought of.
# In this exercise you will implement just such a trick, where the
# numbers are dates.
#


#----------------------------------------------------------------
# Version 1
#
# In this version you will implement the algorithm one step at
# a time as a series of assignment statements.  Begin by replacing
# the zeros below with some date of interest (your birthday, today's
# date, etc).  Then replace each of the "pass" statements below
# with an assignment statement to complete the calculation.  In
# the last step, assign your final value to variable "result".
# When you run this script the date you have calculated will be
# printed as an 8-digit number.

day = 14 # Put your day here (one or two digits)
month = 9 # Put your month here (one or two digits)
year = 1990 # Put your year here (one to four digits)

# In each of the following steps, do the calculation and store
# the intermediate result in a variable.  Choose meaningful
# names for your variables.
#
# a. Multiply the day by 100
result = day * 100;
# b. Add the month
result = result + month;
# c. Multiply the result by 80
result = result * 80;
# d. Add 1
result = result + 1;
# e. Multiply the result by 250
result = result * 250;
# f. Add the year
result = result + year;
# g. Add the year again
result = result + year;
# h. Subtract 250
result = result -250;
# i. Halve the result using integer division
result = result // 2.0;
# j. Assign your final answer to variable "result" (replacing
# the value 0)

# Print the result as an eight digit number.  (The "str" function
# converts the number to a character string and the "zfill"
# method pads the resulting string with leading zeros, if necessary,
# to make the string 8 digits long.)
print('The first date you thought of was ' + str(result).zfill(8))


#----------------------------------------------------------------
# Version 2
#
# There are usually several different ways to implement a given
# algorithm.  The way we did the calculation above laid out
# the steps one-by-one, which makes it very clear but also very
# long-winded.  Your challenge in this version is to do exactly
# the same calculation but in only one step!  After choosing
# another date below, write an arithmetic expression that does
# the entire calculation all at once.
#

day = 18 # Put your day here (one or two digits)
month = 2 # Put your month here (one or two digits)
year = 1880 # Put your year here (one to four digits)

# Replace the value 0 in the following assignment statement
# with a single (large!) expression that does exactly the same
# calculation as described above (but without assigning the
# intermediate results to named variables).  It helps to make
# the expression more readable if you use plenty of brackets,
# even when they're not strictly necessary.
result = ((((((((day * 100) + month) * 80) + 1) * 250) + year) + year) - 250) // 2.0;

# Print the result as an eight digit number, preceded by a blank line
print()
print('The second date you thought of was ' + str(result).zfill(8))
