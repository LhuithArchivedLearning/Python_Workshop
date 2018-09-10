#---------------------------------------------------------------------
#
# Movie Title Scraper
#
# This exercise gives you practice at extracting elements from web
# documents and using them to create your own HTML file.
#
# One of the lecture demonstrations was a program that extracted the
# headings from Wikipedia pages.  Wikipedia was chosen because its pages
# have a consistent format that has remained unchanged for many years.
# However, the lecture demonstration program doesn't work for all
# Wikipedia pages, because the page headings come in two different
# styles.  Some pages have their headings between the following HTML
# tags:
#
#   <h1 id="firstHeading" class="firstHeading" lang="en">HEADING</h1>
#
# But when the heading is the name of a book or film the title is
# italicised, so it appears in the HTML source as follows:
#
#   <h1 id="firstHeading" class="firstHeading" lang="en"><i>HEADING</i></h1>
#
# Below is a list containing the URLs for several science fiction
# movies described in Wikipedia, all of which have their heading
# formatted in the second style above.  Your task is to extract the
# headings from each of these pages, excluding any of the surrounding
# HTML markups and generate a new, complete HTML document which
# contains the movie titles in a bulletted list.  Your generated
# document must contain all the standard mark-ups used in HTML
# documents such as a head and body section, title, etc.
#
# As well as the title of each movie, your generated document must
# also contain the date the Wikipedia page was last updated.  To
# do so, examine the source code of the Wikipedia pages to see
# how the edit date is written and devise code to find and extract
# just the date itself.  You should display the date in brackets
# after the movie title, e.g., "The Green Slime (19 December 2017)".
#
# Complete the code by replacing the "pass" statements.
#

# This list contains the Wikipedia pages of interest
sf_movies = ['https://en.wikipedia.org/wiki/The_Green_Slime',
             'https://en.wikipedia.org/wiki/Soylent_Green',
             'https://en.wikipedia.org/wiki/It_Came_from_Outer_Space',
             'https://en.wikipedia.org/wiki/The_Omega_Man',
             'https://en.wikipedia.org/wiki/Colossus:_The_Forbin_Project',
             'https://en.wikipedia.org/wiki/Earth_vs._the_Flying_Saucers']

# Import the necessary URL function
from urllib.request import urlopen

# Open the target HTML file (sf_movies.html) for writing as Unicode
pass

# Write standard HTML "header" markups into your file, up to
# and including the <body> tag.  Give your web document a
# meaningful title
pass

# Write the start of an unordered list into your file
pass

# For each of the Wikipedia pages listed above...
    # Open and download the page as a Unicode character string...
    # Extract the italicised heading ...
    # Extract the last date an edit was made ...
    # Write a "list item" containing the movie title and edit date into your file
pass

# Write the end of the unordered list into your file
pass

# Write the standard HTML "footer" markups into your file
# to complete the document
pass

# Close your HTML file (which you can now view in a web browser)
pass

