#-----------------------------------------------------------
#
# Web Document Copier
#
# The Python script below reads the contents of a web
# document, the Wikipedia home page, and prints it to the
# shell window.  Since Tk windows cannot handle all Unicode
# characters, it converts the text to an equivalent ASCII
# character string before printing it.
#
# To make this program more useful, modify it in two
# ways:
#
# 1) Instead of hardwiring the web document's address in the
#    Python code, prompt the user for the address of the web
#    document they want to copy.
#
# 2) Instead of printing the contents of the web document
#    to the shell window, write them to an HTML file, so
#    that you have a permanent copy of the document.  In this
#    situation you should save the text as Unicode rather
#    than ASCII.  (However, if you view the document in a web
#    browser you may be disappointed to discover that some of
#    the links to images and other "external" document elements
#    no longer work properly, depending on whether the URLs
#    involved are relative or absolute.)
#
# 3) Once your "copier" is working, use it to download a number
#    of web pages to your computer, then open the files in a
#    text editor or a web browser.  Examine the document's
#    source code and ensure that you can identify the main
#    elements in the document such as the head and body
#    sections, the document title, headings within the body,
#    etc.
#
# NB: If you examine the downloaded web pages in a web browser
# you may find that some hyperlinks are broken.  This can
# happen when the HTML source code contains links relative to
# current file, rather than using a full URL address.  By
# copying the code to a new place, but not adjusting the
# relative links accordingly, we can "break" them.
# 

from urllib.request import urlopen

# This is the web page that will be downloaded
url = 'http://www.wikipedia.org/'

# Read the contents of the web page as a character string,
# suitable for printing to an ASCII-only Tk widget, using
# backslashes to "escape" any non-ASCII characters
web_page = urlopen(url)
web_page_bytes = web_page.read()
web_page_text = web_page_bytes.decode('ASCII', 'backslashreplace')

# Print the downloaded web page source code in IDLE's
# shell window (which is a Tk GUI widget)
print(web_page_text)


