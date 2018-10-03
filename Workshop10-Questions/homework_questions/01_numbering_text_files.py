#---------------------------------------------------------
#
# Numbering text files
#
# Text files are a convenient, but unstructured way of
# storing data.  In this exercise you are required to
# write a Python function which creates a copy of a
# given text file.  However, each line in the copy should
# be preceded by the line number.
#
# Hints: Last week's "line numbering" exercise was very
# similar, except that it printed the numbered lines to
# the screen instead of writing them to a file.  You can
# also make use of some similar code from this week's
# "text formatter" lecture demonstration.
#


#---------------------------------------------------------
#
# Complete the following function by replacing the "pass"
# lines (which do nothing)
#
def number_file(input_file_name, output_file_name):

    # 1. Open the input file for reading
    pass
       
    # 2. Create the output file
    pass

    # 3. Initialise a variable to keep track of the line number
    pass
    
    # 4. For each line in the input file:
    pass
        # 4a. Increment the line number
 
        # 4b. Write the line number and the line of text from
        #     the input file to the output file, separated
        #     by a space
 
    # 5. Close both the files
    pass


#---------------------------------------------------------
#
# A main program to call the function, using a
# provided text file
#
number_file('Monty_Python.txt', 'Monty_Python_Numbered.txt')
