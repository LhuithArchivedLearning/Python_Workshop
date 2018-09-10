# Number of Digits
#
# THE PROBLEM
#
# You have to number all the pages in a book which has a total
# of 366 pages.  Write a Python script to calculate how
# many individual digits you have to write down.  (NB: You are
# not expected to write "leading zeros" before the page numbers.)
#
# Ask yourself how many page numbers will have one digit, how
# many have two digits, and so on.  Hint: In an inclusive range
# of numbers from M to N there are (N - M) + 1 distinct values.
# For instance, there are (99 - 10) + 1 = 90 numbers in the range
# from 10 to 99, inclusive.

#### Complete your solution by replacing the zeros below

# First work out how many pages there are with one, two and three digits

total_pages = 366;
num_one_digit_pages = 9;
num_two_digit_pages = (99 - 10 + 1) * 2;
num_three_digit_pages = (366 - 100 + 1) * 3;

# Now work out how many individual digits there are

total_digits = num_one_digit_pages + num_two_digit_pages + num_three_digit_pages;

# Finally print the result       

print ('You will have to write', total_digits, 'digits')
