#---------------------------------------------------------------------#
#
# Morlock Finder
#
# This exercise gives you some practice at find patterns in a large
# amount of text, using both Python's "find" method and regular
# expressions.  The text in this case is the pioneering science fiction
# novel, "The Time Machine", by H. G. Wells.  This is contained in a
# plain text file, TheTimeMachine.txt, which is divided into individual
# lines separated by newline markers.
#
# Each of the tasks below begins by opening the file in "universal"
# mode, so that it doesn't matter whether the file uses DOS (Microsoft)
# or UNIX (Apple/Linux) newline markers.  The file is re-opened at the
# beginning of each task so that the file "pointer" will be at the
# beginning, ready for reading.  Some tasks begin by just opening the
# file and some begin by opening the file and reading its contents as
# a single (very long) string containing embedded newline markers.
#

from re import findall

# Task 1: The bad guys in the novel are the evil, underground-dwelling
# Morlocks.  Add a for-each loop to the following code and
# use the "find" method to find and print each line of the
# novel that mentions Morlocks.
time_machine = open('TheTimeMachine.txt', 'U') # open the file in "universal" mode
pass

# Task 2: The heroine is called Weena, one of a tribe of devolved human
# beings living in the distant future.  Using the "find" method and a
# while loop, print all the locations in the novel where Weena's name is
# mentioned.
time_machine_text = open('TheTimeMachine.txt', 'U').read() # read the file's contents
pass

# Task 3: Rather than using loops and repeated calls to "find", the
# "findall" function provides a much easier way to find all occurrences
# of a pattern.  Use the findall function to print how many times
# Weena's name appears in the novel.  Hint: This can be done very
# concisely by applying the built-in "len" function to the result
# returned by findall.
time_machine_text = open('TheTimeMachine.txt', 'U').read() # read the file's contents
pass
    
# Task 4: In this plain text version of the novel emphasis has been indicated
# by surrounding words with underscores, e.g., "_nil_".  Use the
# findall function and an appropriate regular expression to find and
# print all individual emphasised words in the novel's text.  Do not print the
# underscores.
time_machine_text = open('TheTimeMachine.txt', 'U').read() # read the file's contents
pass

# Task 5: The file contains many hyphenated words and phrases, e.g., "re-use".
# Use the findall function and an appropriate regular expression to find and
# print all phrases in the file containing a single hyphen. Ensure that you
# allow for both upper and lower case letters in the phrase.
time_machine_text = open('TheTimeMachine.txt', 'U').read() # read the file's contents
pass

