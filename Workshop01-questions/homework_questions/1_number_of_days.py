# Days calculator
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, representing the number of days in each
# month of a given (non-leap) year.

january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31

# PART 1
#
# Write an expression, or expressions, to calculate the number of days
# in each quarter (three month period) of the year, using the values
# introduced above, and print the result.

quarter0 = january + february + march;
quarter1 = april + may + june;
quarter2 = july + august + september;
quarter3 = october + november + december;

# PART 2
#
# Write an expression, or expressions, to calculate the number of days
# in each half of the calendar year, and print the result.  NB: Your
# solution to Part 2 should use your solution to Part 1.

half0 = quarter0 + quarter1;
half1 = quarter2 + quarter3;

# PART 3
#
# Write an expression, or expressions, to calculate the number of days
# in the year, and print the result  NB: Your solution to Part 3
# should use your solution to Part 2.

print(half0 + half1)


