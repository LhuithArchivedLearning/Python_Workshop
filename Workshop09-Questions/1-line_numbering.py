#----------------------------------------------------------------
#
# Line numbering
#
# Define a function which accepts one argument, the name of a
# text file and prints the contents of that file line-by-line.
# Each line must be preceded by the line number.  For instance,
# the file 'AnimalFarm-Chapter1.txt' will be printed as follows:
#
#  1 Animal Farm by George Orwell
#  2 
#  3 Chapter I
#  4 
#  5 Mr. Jones, of the Manor Farm, had locked the hen-houses for the night, but
#  6 was too drunk to remember to shut the pop-holes. With the ring of light
#  7 ...
#
# Optional: Since the number of digits in the line number changes,
# you can make the output look neater by using Python's "rjust"
# method, or similar, to produce the line numbers in a fixed
# number of spaces.
#
# Note: You should open the file in "Universal mode" so that
# it doesn't matter whether the text lines are terminated with
# Microsoft DOS, Apple or UNIX/Linux newline characters.
#
# Note: When you read a line of text from a file it will have a
# "newline" character at the end.  Since Python's "print"
# function puts a newline at the end of its output by default
# this will result in extra blank lines being written.  There are
# two ways to solve this:
#
# 1) Remove the newline character '\n' from the end of each line
#    before printing it; or
# 2) Use the "end" parameter of the "print" function to specify
#    that it shouldn't put anything at the end of the string
#    printed.
#


#----------------------------------------------------------------
#

#### DEVELOP YOUR print_with_line_numbers FUNCTION HERE


#----------------------------------------------------------------
#
# Main program to test your code, using the first chapter of the
# book Animal Farm by George Orwell.
#
print_with_line_numbers('AnimalFarm-Chapter1.txt')
