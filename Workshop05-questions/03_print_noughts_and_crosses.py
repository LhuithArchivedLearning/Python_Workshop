#----------------------------------------------------------------#
#
# PRINT NOUGHTS AND CROSSES
#
# As an exercise in processing data stored in lists, here you
# are required to write several small code segments that extract
# data stored in lists both by value and position.
#
# Recall that the children's game of Noughts and Crosses (US:
# Tic-Tac-Toe) is played on a 3 x 3 matrix in which the cells
# may be empty '_', a cross 'X' or a nought 'O'.  Such a matrix
# can be represented using a list containing three
# rows, each of which is a list containing three values.
#
# Below are the outcomes of four games of Noughts and Crosses.
# represented as lists. Games 1 and 2 have been represented as
# a single list (of lists) and Games 3 and 4 have been represented
# as three separate lists.
#
# For each game there is a series of challenges for you
# to solve by printing appropriate values extracted from the
# lists.  Note that all of these can be solved with just a
# few lines of Python code.  In all cases you must use
# FOR-EACH loops to solve the problem.


#----------------------------------------------------------------#
# Very easy: Write FOR-EACH code to print the three rows in
# Game 1, all on one line.  Your code should print:
#
#     ['X', 'O', 'X'] ['X', 'X', 'O'] ['O', 'O', 'O']
#
# Remember that using parameter "end = ''" at the end of a
# call to a PRINT function prevents it from printing a
# newline.

# Game 1 - Noughts win
#
game1 = [['X', 'O', 'X'],
         ['X', 'X', 'O'],
         ['O', 'O', 'O']]

##### PUT YOUR CODE HERE

for row in game1 :
    print(row, end ='');

print();
print();
#----------------------------------------------------------------#
# Easy: Write FOR-EACH code to print the values of all cells
# in Game 2, all on one line.  Your code should print:
#
#     OXOXXXOOX
#
# Hint: You will need two FOR-EACH loops.

# Game 2 - Crosses win
#
game2 = [['O', 'X', 'O'],
         ['X', 'X', 'X'],
         ['O', 'O', 'X']]

##### PUT YOUR CODE HERE

for row in game2 :
    for element in row :
        print(element, end = '');

print();
#----------------------------------------------------------------#
# Medium difficulty: Write FOR-EACH code to print all
# the cells in Game 3, row by row, from top to bottom.
# Your code should print:
#
#    XOXXOOOXX
#
# Hint: You can do this with just a single FOR-EACH
# loop by "adding" the separate rows.

# Game 3 - It's a tie
#
game3a = ['X', 'O', 'X']
game3b = ['X', 'O', 'O']
game3c = ['O', 'X', 'X']

##### PUT YOUR CODE HERE
maingame = game3a + game3b + game3c;

for cell in maingame:
    print(cell, end ='');


#----------------------------------------------------------------#
# Medium difficulty: Write FOR-EACH code to print the cells
# on the diagonal from top-left to bottom-right for Game 1.
# Your code should print:
#
#    XXO
#
# Hint: You will need to use a numeric loop variable to keep
# track of the position of each cell to be printed.

# Game 1 - Noughts win
#

print();

game1 = [['X', 'O', 'X'],
         ['X', 'X', 'O'],
         ['O', 'O', 'O']]

##### PUT YOUR CODE HERE
for i, row in enumerate(game1) :
    print(row[i], end='');

print();
#----------------------------------------------------------------#
# A bit harder: Write FOR-EACH code to print the cells
# in Game 4 by columns, rather than rows.  In other
# words, you must print the first element from each of
# the three rows, then the second, then the third.
# Your code should print:
#
#   XO__XO_OX
#
# Hint: You will need to use a numeric loop variable to
# keep track of which column you're up to.

# Game 4 - Crosses wins easily
#
game4a = ['X', '_', '_']
game4b = ['O', 'X', 'O']
game4c = ['_', 'O', 'X']

for i in range(3):
    print(game4a[i] + game4b[i] + game4c[i], end ='');


    
