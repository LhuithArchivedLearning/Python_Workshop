#----------------------------------------------------------------
#
# Mini Siri
#
# Computer programs that can have meaningful conversations with
# humans have been a dream for many decades, but the emergence
# of interactive apps like Apple's Siri are starting to make this
# dream reality.  In this exercise you will develop a program which
# can carry out a very rudimentary form of "conversation".  For
# example, here's a conversation in which each of the computer's
# prompts is followed by the user's responses:
#
#    Hello, I'm Mini Siri. G'day.
#    Tell me more. What do you want me to say?
#    Why do you ask? I'm confused!
#    Please don't shout. Sorry.
#    Tell me more. Can you tell me how to get out of here?
#    Why do you ask? Because.
#    I'm tired, goodbye.
#
# This is to be done in two stages:
#
# 1) Develop a function called "respond" which accepts a string
# as its parameter and returns various strings depending on the
# parameter's contents, using the following rules, in the order
# listed here:
# a) If the parameter contains a question mark return "Why do
#    you ask?"
# b) If the parameter contains an exclamation mark return "Please
#    don't shout."
# c) If the parameter is less than 10 characters long return
#    "Tell me more."
# d) In all other cases return "What do you mean?"
#
# 2) Once your function is working correctly, and passes all the
# tests below, write some interactive code using a "for each"
# loop and the "input" function to repeatedly prompt the
# user with the reply to their previous input to get the next
# user input.  To get started, the first prompt should be "Hello,
# I'm Mini Siri."  This will allow the program to carry out a
# "conversation" with the user (but one which will get boring
# very quickly!).  When developing your solution to this part of
# the exercise you should leave the testing code at the end
# of this file commented out.
#
# Hint: Note that the Boolean "in" operator can be used on
# character strings.
#
# The tests below tell us how your function is expected to
# behave when called.  After you've written your function,
# confirm that it works correctly by (a) running this module
# so that your function is defined and then (b) copying
# each of the function calls in the set of tests into the
# shell to see if the right answer is returned.  Obviously
# if you don't get the expected answers then you'll need
# to modify your code until you do.
# 
# Finally, the main program of this file runs the tests
# automatically.  The code is commented out, but if you
# want to run all the tests automatically, just uncomment
# the code and run this file.  When developing your solution
# to the second part of this exercise you should leave the
# testing code commented out.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> respond("What do you want?")
'Why do you ask?'

>>> respond("I don't like that!")
"Please don't shout."

>>> respond("I dunno.")
'Tell me more.'

>>> respond("I haven't much to tell you.")
'What do you mean?'

"""


#---------------------------------------------------------

##### DEFINE YOUR reply FUNCTION HERE
isrunning = True;

def respond (string):
    global isrunning;
    
    if "?" in string :
        return 'Why do you ask?';
    elif "!" in string:
        return "Please don't shout.";
    elif "sorry" in string:
        return "Its ok :)";
    elif "funny" in string:
        return "thank you, my humor is at 80%";
    elif "exit" in string or "leave" in string or "escape" in string or "exit" in string or "bye" in string:
        isrunning = False;
        return "GoodBye";
    elif len(string) < 10:
        return 'Tell me more.';
    else:
        return 'What do you mean?';

##### DEVELOP YOUR INTERACTIVE MAIN PROGRAM HERE
print("Hello im Mini-Siri, Please Type Something");


while(isrunning):
    q = input("");

    print(respond(q));
    


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.  Leave this code commented
# out when developing your interactive main program.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))

