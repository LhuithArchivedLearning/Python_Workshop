#---------------------------------------------------------------------
#
# Movie Title Scraper 2
#
# This exercise gives you practice at extracting elements from web
# documents using a regular expressions and using them to create
# your own HTML file.
#
# In last week's workshop you completed an exercise in which you used
# Python's built-in string "find" method to extract the titles of
# movies from Wikipedia pages.  Your task here is to do the same
# task, but this time using the regular expression "findall" function
# instead of the "find" method.  You can do this either by modifying
# your solution to last week's exercise or by completing the entire
# task from scratch.  The full set of instructions for the
# modified task follow...
#
# One of the lecture demonstrations was a program that extracted the
# headings from Wikipedia pages.  Wikipedia was chosen because its pages
# have a consistent format that has remained unchanged for many years.
# However, the lecture demonstration program doesn't work for all
# Wikipedia pages, because the page headings come in two different
# styles.  Some pages have their headings between the following HTML
# tags:
#        <h1 ...>HEADING</h1>
#
# But when the heading is the name of a book or film the title is
# italicised, so it appears in the HTML source as follows:
#
#        <h1 ...><i>HEADING</i></h1>
#
# An easy way to match this pattern is to find "><i>" followed by
# some characters followed by "</i></h1>".
#
# Below is a list containing the URLs for several science fiction
# movies described in Wikipedia, all of which have their heading
# formatted in the second style above.  Your task is to extract the
# headings from each of these pages, excluding any of the surrounding
# HTML markups and generate a new HTML document which contains these
# movie titles in a bulletted list.
#
# Complete the code by replacing the "pass" statements.

# This list contains the Wikipedia pages of interest
sf_movies = ['https://en.wikipedia.org/wiki/The_Green_Slime',
             'https://en.wikipedia.org/wiki/Soylent_Green',
             'https://en.wikipedia.org/wiki/It_Came_from_Outer_Space',
             'https://en.wikipedia.org/wiki/The_Omega_Man',
             'https://en.wikipedia.org/wiki/Colossus:_The_Forbin_Project',
             'https://en.wikipedia.org/wiki/Earth_vs._the_Flying_Saucers']

# Import the necessary URL and RE functions
from urllib.request  import urlopen
from re import findall

# Open the target HTML file (sf_movies.html) for writing
pass

# Write standard HTML "header" markups into your file
pass

# Write the start of an unordered list into your file
pass

# For each of the Wikipedia pages listed above...
    # Open and download the page as a character string...
    # Extract the italicised heading using a regular expression...
    # Write a "list item" containing the heading into your file
pass

# Write the end of the unordered list into your file
pass

# Write standard HTML "footer" markups into our file
pass

# Close your HTML file (and you should then view it in a web browser)
pass

