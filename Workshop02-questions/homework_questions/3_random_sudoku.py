#--------------------------------------------------------------------------#
#
# Random Sudoku
#
# One of this week's lecture demonstrations was a program called Random
# Scrabble which produced an image similar to the board in a game of
# Scrabble, except that the letters were chosen randomly.  As an easier
# exercise in using random numbers and simple repetition, here you will
# create a program which prints a game of Sudoku.  Again, however, we
# will ignore the rules of the game and just print random numbers.
#
# A Sudoku board consists of a 9 x 9 grid into which the user must
# write numbers from 1 to 9, inclusive.  Your job is to print such
# a grid in IDLE's Shell window, using random numbers.  (This is not
# a Turtle exercise.)  Below are some constant values you will need
# in order to do this.  Your solution will require two FOR-EACH loops
# and a call to the "random" module's "choice" function.  For instance,
# your code may print the following Sudoku board:
#
#     5 4 5 1 3 4 4 4 5
#     2 4 3 3 8 9 3 8 9
#     1 1 8 1 1 5 9 6 7
#     4 3 6 2 6 1 2 8 2
#     7 4 6 2 6 1 4 3 2
#     4 2 9 1 1 9 9 6 7
#     8 6 5 5 7 1 4 1 5
#     8 5 5 7 4 9 9 5 1
#     3 9 7 2 4 1 7 6 7
#
# NB: If you want to print a value without a "newline" at the end in
# Python, specify that the "end" parameter in the call to the print
# function should be the empty string ''.  For instance,
#
#    print('a', end = '')
#    print('b')
#
# will print
#
#    ab
#
# in the Shell window.  Also, calling the print function without any
# arguments prints just a newline.
#
# Challenge: Having completed this exercise, modify your code so
# the board printed is of a different size.  You should be able
# to do this by changing only one value in your code.
#

# Import a function you will need
from random import choice

# Define two helpful constant values you should use
digits = '123456789'
grid_size = 9

for row in range(grid_size) :
    print();
    for col in range (grid_size) :
        digit = choice(digits);
        print(digit, end = ' ');


# A suggested solution strategy:
#
# 1) For each row number in the required range:
#    a) For each column number in the required range:
#       i)  Choose a random digit from the string above
#       ii) Print the digit, without a newline
#    b) Print a newline to end the row

### PUT YOUR PYTHON CODE HERE

