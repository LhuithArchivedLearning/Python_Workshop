#----------------------------------------------------------------
#
# Image Finder
#
# As an exercise in extracting information from web pages, here
# you will develop a program that extracts the locations of all
# images in a given web page.  Recall that images are inserted
# into HTML documents using the following kind of markup, which
# has a URL indicating the source of the image to be displayed
# in the current document:
#
#    <img src="URL">
#
# However, you need to keep in mind that apart from the "src"
# attribute there may be other attributes within the image tag,
# so you can't just search for the simple pattern above.  Also
# some other kinds of HTML tags have a "src" attribute too, so
# you can't just search for the attribute pattern on its own.
#
# For this exercise we will extract images from Wikipedia pages.
# Before starting, open a Wikipedia page in a web browser and
# examine its source code to see the markup notation used for
# images, which are usually in JPEG format.
#
# The URL you produce must be complete and suitable for finding
# the image in isolation - you can test this just by entering it
# into the address bar of a web browser.  Sometimes the URLs
# you find in a page may be relative addresses, not absolute
# ones, in which case, for instance, they will be missing a
# "http:" prefix.  This is true for most images in Wikipedia
# pages.  In this case you need to add the necessary
# prefix to create a complete, stand-alone URL like the
# following one extracted from the Wikipedia page on
# Superman (url6 below).
#
#   http://upload.wikimedia.org/wikipedia/en/7/74/Clark-Kent.png
#
# Similarly, some standard images in Wikipedia begin with "/static"
# in which case you need to prepend them with "https://en.wikipedia.org"
# as in the following one from the same page.
#
#   https://en.wikipedia.org/static/images/wikimedia-button.png

 
#-----
# Import the necessary URL and RE functions
from urllib.request  import urlopen
from re import findall

#-----
# Here are some web pages to try, each of which is a Wikipedia
# page, so we can assume they have a fairly consistent structure.
# As well as large images, you will also discover the images for
# small icons, as well as single pixel meta-data images hidden in
# the page.
url1 = 'http://en.wikipedia.org/wiki/Jack_Benny'
url2 = 'http://en.wikipedia.org/wiki/QUT'
url3 = 'http://en.wikipedia.org/wiki/Flags'
url4 = 'http://en.wikipedia.org/wiki/Robby_the_Robot'
url5 = 'http://en.wikipedia.org/wiki/Baby_Huey'
url6 = 'http://en.wikipedia.org/wiki/Superman'

##### COMPLETE YOUR SOLUTION BELOW BY REPLACING THE "pass" STATEMENTS

#-----
# Step 1. Get a link to the web page from the server, using one
# of the URLs above
pass

#-----
# Step 2. Extract the web page's content as a character string
pass

#----
# Step 3. Close the connection to the web server
pass

#-----
# Step 4. Find and print the URL for each of the images
# in the web page.  You should print just the URL, not
# any of the surrounding tags, attributes or other text.
# Importantly, the URL must be complete, so if it missing
# the 'http:' or 'https://en.wikipedia.org' prefix you
# need to add it.
pass
