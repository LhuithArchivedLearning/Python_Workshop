#------------------------------------------------------------------------#
#
# Minimum and Maximum Random Numbers
#
# In this week's exercises we are using several pre-defined
# functions, as well as character strings and lists.  As a simple
# exercise with lists, here you will implement a small program which
# generates a large collection of random numbers and then finds the
# smallest and largest numbers produced.  After a large number of
# trials it should print the smallest and largest random numbers
# generated, e.g.:
#
#     Results for 100 trials for random numbers between 1 and 1000
#     The smallest number generated was 25
#     The largest number generated was 987
#
# The goal is to produce a large collection of random numbers below
# a certain size and then print the smallest and largest numbers
# produced.
#
# To do this you will need to use:
# a) The randint function to generate random numbers
# b) A for-each loop to do an action several times
# c) A list-valued variable which is initially the empty list []
# d) The "+" operator (or the "append" method) to add a value to
#    the list.  Note that the "+" operator joins two lists, not a
#    value and a list.  A value can be turned into a singleton list
#    just by putting square brackets around it.
#

# Import the random function needed
from random import randint

# Define some convenient constant values
number_of_trials = 100
limit_of_random_numbers = 1000
random_numbers = [];


for x in range(number_of_trials) :
    random_numbers.append(randint(0, limit_of_random_numbers));


# Solution strategy:
#
# 1) Create an empty list to hold the random numbers
# 2) For each of the number of trials:
#    a) Produce a random number between 1 and the limit
#    b) Add the random number to the end of the list
#       of random numbers
# 3) Print a message saying how many trials were performed
# 4) Print the minimum number in the list of random numbers
# 5) Print the maximum number in the list of random numbers

print(len(random_numbers));
print(min(random_numbers));
print(max(random_numbers));
print(random_numbers);

