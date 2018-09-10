#--------------------------------------------------------------------#
#
# HTML Document Checker
#
# We have seen that HTML is a language with a specific syntax.  Web
# browsers make a "best effort" to display documents, and are often
# quite forgiving of errors in the HTML code, but there are obviously
# limits to what they can do with incorrectly marked-up documents.
#
# In this exercise you will write a Python program which reads an
# HTML document and checks that it has certain syntactic features.
#
# This exercise can be completed using Python's "S.find(T)" method
# for character strings which returns the position in string S where
# substring T first occurs or -1 if substring T does not occur in
# string S at all.
#
# Optional extension: Instead of printing your results to the shell
# window, write them out to a text file.
#

# Files to test your solution on - uncomment as appropriate
html_file = 'AdventuresOfSuperman-Good.html' # this file is syntactically correct
# html_file = 'AdventuresOfSuperman-Bad.html' # this file contains several syntax errors

# Open and read the contents of the HTML file
html_code = open(html_file).read()

# For each of the syntactic HTML features described below write
# Python code to check whether or not the file's contents are
# correct and report your findings to the user

# Put code here to tell the user which file you are checking
pass

# Put code here to confirm that the document begins with the HTML
# markup '<!DOCTYPE html>', which tells the web browser which language
# the document is written in
pass

# Put code here to confirm that the document includes a header section
# marked up as '<head> ... </head>'
pass

# Put code here to confirm that the document includes a title
# marked up as '<title> ... </title>'
pass

# Put code here to confirm that the document includes a body
# marked up as '<body> ... </body>'
pass
