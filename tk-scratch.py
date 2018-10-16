
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
from urllib.request import urlopen, Request

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

window = Tk();
window.title("TK Time");

##button1 = Button(text="1");
##button2 = Button(text="2");
##button3 = Button(text="3");
##button4 = Button(text="4");
##button5 = Button(text="5");
##button6 = Button(text="6");
##
##button1.grid(row=0,column = 0, padx=5, pady=5);
##button2.grid(row=0,column = 1, padx=5, pady=5);
##button3.grid(row=1,column = 0, padx=5, pady=5);
##button4.grid(row=1,column = 1, padx=5, pady=5);
##button5.grid(row=2,column = 0, padx=5, pady=5);
##button6.grid(row=2,column = 1, padx=5, pady=5);\

##def display_counter():
##    output = str(counter) + "/" +str(len(input_list));
##    labelCounter['text'] = output;
##    print(counter);
##    display_text();
##
##def display_text():
##    output = str(counter);
##    Text = 'Fart';
##    
##def countup(event):
##    global counter;
##    if counter < len(input_list):
##        counter = counter + 1;
##    print();
##    display_counter();
##
##def countdown(event):
##    global counter;
##    if counter > 0:
##        counter = counter - 1;
##        
##    display_counter();
##
##labelCounter = Label(window, text = ""); # to display the current and total item numbers
##labelCounter.pack();
##counter = 0;        # the index of the list item being displayed
##input_list = ['a', 'e', 'i', 'o', 'u'] # list of vowels
##display_counter();
##valuetext = Text(window,width=10, height=4);
##valuetext.pack();
###valuetext['text'] = input_list[counter];
##buttonholder = LabelFrame(window, height=2);
##
##prv = Button(window,height = 1, width=2, text='<<');
##prv.pack();
##prv.bind("<Button-1>", countdown);
##
##nxt = Button(window, height = 1, width=2,text='>>', command = countdown(counter));
##nxt.pack();
##nxt.bind("<Button-1>", countup);

##button1 = Button(text="1");
##button2 = Button(text="2");
##button3 = Button(text="3");
##button4 = Button(text="4");
##button5 = Button(text="5");
##button6 = Button(text="6");
##
##button1.grid(row=0,column = 0, padx=5, pady=5);
##button2.grid(row=0,column = 1, padx=5, pady=5);
##button3.grid(row=0,column = 2, padx=5, pady=5);
##button4.grid(row=1,column = 0, padx=5, pady=5);
##button5.grid(row=1,column = 1, padx=5, pady=5);
##button6.grid(row=1,column = 2, padx=5, pady=5);

names = ['ass', 'balls', 'shit', 'asdasdasdasd', 'poo', 'fartmonkey'];

best = names[0];

for index in range(len(names)):
    if len(names[index]) > len(best):
        best = names[index];

print(len(best));
'baab'        
