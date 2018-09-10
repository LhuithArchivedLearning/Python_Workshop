#-----------------------------------------------------------------
#
# Guessing Game
#
# As an example of a program involving making a decision and
# user interaction, here you will develop a simple guessing
# game in a couple of stages.
#
# Stage 1
#
# Write code that :
#
# (a) chooses a random number between 0 and 9, inclusive;
# (b) prints a prompt asking the user to guess what the number is,
#     such as "What number am I thinking of?" or similar;
# (c) reads a number typed by the user; and
# (d) prints "You're right!" if the number typed by the user
#     is the same as the random number chosen, or "Sorry." if
#     the numbers do not match.
#
# To do this you will need the "randint", "input" and "eval"
# functions as well as an IF statement.
#
# Stage 2
#
# Having gotten the code outlined above to work, you can make
# the "game" more interesting by asking the user to guess
# several times and then keeping and displaying a total score.
# To do this you will need to
#
# (a) introduce a variable to keep track of the score and
#     increment it each time the user guesses correctly;
# (b) put a FOR loop around your code so that it is run
#     several times, allowing multiple tries; and
# (c) display the score at the end.
#
# Comment: This is a hard game for the user to win!  You can
# make it fairer by reducing the range of numbers to choose
# from.
#

# Import the random integer function
from random import randint
guess = randint(0, 3);
attempts = 20;
score = 0;

for guesses in range(attempts) :
    val = (input('What number am i thinking of? : ', ));

    if len(val) == 0 :
        val = 0;
    else :
        val = eval(val);
    
    if val == guess :
        print('Your right!!!');
        score +=1;
    else :
        print('Sorry, you guessed', val, 'and i gussed ', guess);

    guess = randint(0, 3);

print('You scored : ', score,'!!!');
