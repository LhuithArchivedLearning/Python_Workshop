
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10318313
#    Student name: Eugene Martens
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  The Best, Then and Now
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to preview and print lists of
#  top-ten rankings.  See the instruction sheet accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.  YOU MAY NOT USE
# ANY NON-STANDARD MODULES SUCH AS 'Beautiful Soup' OR 'Pillow'.  ONLY
# MODULES THAT COME WITH A STANDARD PYTHON 3 INSTALLATION MAY BE
# USED.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

#Dirty Dirty Approuch To fix Security Issues
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *
import os
# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL, sub

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce a
# meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

##### DEVELOP YOUR SOLUTION HERE #####

def CleanUpWhiteSpace(text):
        for i in range(len(text)):
            text[i] = text[i].strip();
        return text;

#using this as a text scrub to remove anything i dont want in text(&quot)
def GeneralCleanUp(text):

    for i in range(len(text)):
        text[i] = text[i].replace("&quot", "");
    return text;

def PrintInformation(InformationBlock, limit = 10):
    print("#-----------------------------------------#");
    for i in range(len(InformationBlock)):

        if i <= limit:
            print(InformationBlock[i]);
    print("#-----------------------------------------#");


#download from source, or access archive
def AcessBookInformation(downloadsource = False):
    #Download Book Weekling Top, Grabbing names, now need to cull the list, and grab any relevant information (pictures, dates, links and so on)
    #https://www.goodreads.com/book/most_read
    bookreadingdownload = "";
    html_file = "";
    
    if downloadsource:
        print("Downloading......");
        bookreadingdownload = download("https://www.goodreads.com/book/most_read", "download/bookreadingdownload");
    else:
        print("Accessing From Archive");
        html_file = open("Archived/bookreadingdownload.html", 'r', encoding='utf-8');
        bookreadingdownload = html_file.read();
        
    booktitles = findall("<span itemprop='name'>(.*?)</span>", bookreadingdownload);

    #clean up and remove titles past 10
    del booktitles[10:];
    bookindex = findall('<td valign="top" class="number">(.*?)</td>', bookreadingdownload);
    #PrintInformation(booktitles);

    #Close File Read if were not downloading
    if not(downloadsource):
        html_file.close();

    return booktitles;

def AccessMusicInformation(downloadsource = False):
    #https://www.billboard.com/charts/pop-songs

    musictopdownload = "";
    html_file = "";
    
    if downloadsource:
        print("Downloading......");
        musictopdownload = download("http://www.bbc.co.uk/radio1/chart/singles", "download/musictopdownload");
    else:
        print("Accessing From Archive");
        html_file = open("Archived/musictopdownload.html", 'r', encoding='utf-8');
        musictopdownload = html_file.read();
        
    musictitles = findall('<div class="cht-entry-title">(.*?)</div>', musictopdownload);
    del musictitles[10:];
    musicindex = findall('<div class="cht-entry-position">(.*?)</div>', musictopdownload);
    #PrintInformation(musictitles);

    #Close File Read if were not downloading
    if not(downloadsource):
        html_file.close();
        
    return musictitles;
    
def AccessElectronicInformation(downloadsource = False):
    #https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics
    electronicstopsaledownload = "";
    html_file = "";
    
    if downloadsource :
        print("Downloading......");
        electronicstopsaledownload = download("https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics", "download/electronicstopsaledownload");
    else:
        print("Accessing From Archive");
        html_file = open("Archived/electronicstopsaledownload.html", 'r', encoding='utf-8');
        electronicstopsaledownload = html_file.read();


    electronicstopsaletitle = findall('<div class="p13n-sc-truncate p13n-sc-line-clamp-2" aria-hidden="true" data-rows="2">(.*?)</div>', electronicstopsaledownload, DOTALL);
    electronicstopsaletitle = CleanUpWhiteSpace(electronicstopsaletitle);
    electronicstopsaletitle = GeneralCleanUp(electronicstopsaletitle);
    del electronicstopsaletitle[10:];
    electronicstopsaleindex = findall('<span class="zg-badge-text">(.*?)</span>', electronicstopsaledownload);
    #PrintInformation(electronicstopsaletitle);

    #Close File Read if were not downloading
    if not(downloadsource):
        html_file.close();

    return electronicstopsaletitle;

def Test():
    print("Poo");

def DisplayInformation(information):
    new_window = Toplevel(window);

    displayLabel = Label(new_window, font = ('Ariel', 12), justify=LEFT);
    displayLabel.grid(row=1, column=2)

    for i in range(len(information)):
        displayLabel["text"] += "["+str(i + 1)+"]" +"  "+ (information[i] + "\n")
        
window = Tk();
window.title("Spicy Data");
window.geometry("600x300");

BookInformation = AcessBookInformation(False);
MusicInformation = AccessMusicInformation(True);
ElectronicInformation = AccessElectronicInformation(False);

#Setting it up


leftFrame = Frame(window, width = 200, height = 600);
leftFrame.grid(row=0,column=0, padx=10,pady=2);

rightFrame = Frame(window, width = 100, height = 5, borderwidth = 5);
rightFrame.grid(row=0,column=1, padx=0,pady=0);

img = PhotoImage(file = "images/tenor.gif");
ChillImageLabel = Label(leftFrame, image = img).grid(row = 0, column = 0);


MostReadFrame = LabelFrame(rightFrame, text="Most Read Books", width = 25, height = 3, borderwidth = 1, relief = GROOVE);
MostReadFrame.grid(row=0,column=0, padx=0,pady=0, sticky=N);

MostListenedPreviousRadial = Radiobutton(MostReadFrame, text="Previous", width = 10);
MostListenedPreviousRadial.grid(row = 0, column = 1, padx=(0, 0), pady=(0, 0));

MostListenedCurrentRadial= Radiobutton(MostReadFrame, text="Current", width = 10);
MostListenedCurrentRadial.grid(row = 0, column = 2, padx=(0, 0), pady=(0, 0));

MostListenframe = LabelFrame(rightFrame, text="Most Listened To Music", width = 25, height =3, borderwidth = 1, relief = GROOVE);
MostListenframe.grid(row=1,column=0, padx=0,pady=0, sticky=N);

MostListenedPreviousRadial = Radiobutton(MostListenframe, text="Previous", width = 10);
MostListenedPreviousRadial.grid(row = 0, column = 1, padx=(0, 0), pady=(0, 0));

MostListenedCurrentRadial= Radiobutton(MostListenframe, text="Current", width = 10);
MostListenedCurrentRadial.grid(row = 0, column = 2, padx=(0, 0), pady=(0, 0));

MostBoughtFrame = LabelFrame(rightFrame, text="Most Bought Electronics", width = 25, height =3, borderwidth = 1, relief = GROOVE);
MostBoughtFrame.grid(row=2,column=0, padx=0,pady=0, sticky=N);

MostListenedPreviousRadial = Radiobutton(MostBoughtFrame, text="Previous", width = 10);
MostListenedPreviousRadial.grid(row = 0, column = 1, padx=(0, 0), pady=(0, 0));

MostListenedCurrentRadial= Radiobutton(MostBoughtFrame, text="Current", width = 10);
MostListenedCurrentRadial.grid(row = 0, column = 2, padx=(0, 0), pady=(0, 0));
#PreviewButton.bind('<Button>', Test());
DisplayInformation(BookInformation);
DisplayInformation(MusicInformation);
DisplayInformation(ElectronicInformation);



