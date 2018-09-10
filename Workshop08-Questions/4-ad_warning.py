#---------------------------------------------------------------------
#
# Ad warning
#
# We're all too familiar with the way the Internet has been infested
# with annoying advertising.  Ad blocker plug ins for web browsers
# are a partial solution.  They usually work by inspecting the contents
# of downloaded web documents for URLs that appear in a blacklist of
# sites the user wants blocked.  (When the ad blocker is first
# installed it usually has a pre-defined blacklist, which the user
# can extend later.)
#
# In this task you will use regular expressions to detect and alert the
# user to the presence of blacklisted URLs in downloaded web documents.
# Your program should download a particular web document and then
# search it for the presence of any blacklisted URLs.  If any such
# URLs are found they should be printed, in full, to the screen to
# alert the user to the presence of unwanted advertising in the
# document.
#
# To get you started we have supplied the addresses of some web documents
# and some blacklisted regular expressions, but you should aim to
# extend these lists by discovering the URLs of advertisements and
# creating your own blacklist entries.
#

#-----
# Import the necessary URL and RE functions
from urllib.request  import urlopen
from re import findall

#-----
# Web documents - These are the URLs of some web documents you can
# use to test your program to see if it can detect advertisements in
# them.  Uncomment whichever one you want to use.  Feel free to
# add others.
#
document = 'http://www.ebay.com.au/'
# document = 'http://www.tutorialspoint.com/python/python_gui_programming.htm'
# document = 'http://www.bom.gov.au/products/IDR664.loop.shtml'

#----
# Advertising blacklist - This is the blacklist of banned advertisement
# URLs.  Each has been written as a regular expression so that minor
# variants of the URL will all be detected.  You should identify other
# advertising URLs and add them to this list as regular expressions.
#
blacklist = [
    '[a-z\\\/]*marketing.php',
    '[a-z\\\/]*marketing2.php',
    'http://[a-zA-Z\.\/]*gmarket[a-zA-Z\.\/]*',
    'https://[0-9a-zA-Z\.\/]*show\_ads[a-zA-Z\.]*'
    ]


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

#----
# Step 4. For each regular expression in the blacklist, print all
# matching URLs you can find in the web document, to alert the
# user to the presence of advertising
pass
