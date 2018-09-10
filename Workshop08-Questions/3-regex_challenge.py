##--------------------------------------------------------------------
##
##    Regular Expression Challenge
##
##    To give you practice at writing regular expressions, this
##    exercise involves solving a number of pattern matching tasks.
##    In each you need to use the "findall" function to extract
##    particular substrings from some given text.
##
##    Regular expressions are typically very compact, so rather
##    than asking you to write full Python programs for each one we
##    have set up the problems as a sequence of short "challenges".
##
##    For each challenge there is an input string, the "question",
##    a list of strings, the "answer", and a call to a function
##    called "attempt" which uses a global variable to
##    keep track of your score.  When you "run" this
##    program it will tell you how well you're doing.
##
##    Your challenge is to replace the 'YOUR REGEX' strings below with
##    regular expressions which produce the required "answer" from
##    the given "question".
##
##    The "question" strings below use triple quotes so that they
##    can include multiple lines.  For some challenges you may want
##    to use "^" and "$" in a regular expression to refer to the
##    beginning and ending of such a line, respectively.  If so you
##    need to specify Python's "MULTILINE" flag, e.g.,
##    "findall(..., ..., MULTILINE)".
##



##--------------------------------------------------------------------
##
##    Set up - The code below sets up the global variables and
##    function needed to keep score.  You do not
##    need to understand or modify this code.
##

from re import findall, MULTILINE

score = -1 # Don't count Challenge 0

# Increment the score if the given solution matches the
# expected answer
def attempt(solution):

    global score

    print('Your solution to Challenge ' + str(challenge_no) + ':',)
    if solution == answer:
        print('CORRECT!')
        score += 1
    else:
        print(solution)
    print()



##--------------------------------------------------------------------
##
##    Challenge 0: Demonstration.  To illustrate how the
##    various challenges are to be completed, this demo solves
##    the trivial problem of finding all whole numbers in a given
##    string.  The solution is entered as the parameter to the
##    function "findall".  You should do likewise in the
##    remaining questions, by replacing the 'YOUR REGEX'
##    placeholders.
##

challenge_no = 0

question = """
This sentence contains 2 lines, 16 words (including numbers),
and 117 characters (including spaces and punctuation).
"""

answer = ['2', '16', '117']

attempt(findall('[0-9]+', question))
# This pattern matches any non-empty sequence of digits.



##--------------------------------------------------------------------
##
##    Challenge 1: The question text below refers to a number of
##    individuals whose title is 'Dr'.  Your goal is to extract
##    the name of each such person but no other.
##

challenge_no = 1

question = """
Dr Cooper often frustrates Dr Hofstadter and is dismissive
of Mr Wolowitz for not having a PhD.  Meanwhile, Dr Koothrappali
and Ms Penny (surname unknown) look on in amazement.
"""

answer = ['Dr Cooper', 'Dr Hofstadter', 'Dr Koothrappali']

attempt(findall('YOUR REGEX', question))



##--------------------------------------------------------------------
##
##    Challenge 2: Given a list of the computer files in a particular
##    folder, extract the names of all the Python files, i.e.,
##    those ending with '.py'.  Filenames may include alphabetic
##    characters and underscores "_".
##

challenge_no = 2

question = """
re.py
regex_for_python.txt
airline.sql
IntroToRegularExpressions.doc
Trees.html
ispy.ppt
workshop_solutions.py
python_tutorial.pdf
OpSys.py
"""

answer = ['re.py', 'workshop_solutions.py', 'OpSys.py']

attempt(findall('YOUR REGEX', question))



##--------------------------------------------------------------------
##
##    Challenge 3: Given some text, extract all words containing at least
##    one capital letter.  You can assume that a "word" consists of
##    alphabetic characters only, i.e., no numbers or punctuation marks.
##    NB: The capital letter does not necessarily need to occur at the
##    beginning of the word.
##

challenge_no = 3

question = """
Regular expressions in Python have nothing at all to do
with the MapReduce functions used by Google but they can
be used with some scripting apps on iPads.
"""

answer = ['Regular', 'Python', 'MapReduce', 'Google', 'iPads']

attempt(findall('YOUR REGEX', question))



##--------------------------------------------------------------------
##
##    Challenge 4: HTML tags usually appear in pairs of the form
##    <X>...</X>, where X is a lowercase word.  Given some text marked
##    up with HTML tags, find all start tags appearing in the text,
##    but don't return the corresponding end tags.
##

challenge_no = 4

question = """
<em>New Zealand</em> has more species of
<big>flightless</big> birds (including the <small>kiwis</small>,
several species of <b>penguins</b>, and the <i>takahe</i>) than
<strong>any other</strong> country.
"""

answer = ['<em>', '<big>', '<small>', '<b>', '<i>', '<strong>']

attempt(findall('YOUR REGEX', question))



##--------------------------------------------------------------------
##
##    Challenge 5: This challenge also involves extracting HTML
##    start tags, but in this case we just want to return the name of
##    of the tag, not the whole tag, because some of the tags
##    have extra attributes.  Hint: You will need to use grouping
##    brackets to identify the part of the pattern you want to
##    return.
##

challenge_no = 5

question = """
<p align='center'> This centered paragraph of <em>marked-up</em>
text contains a number of <b>tags</b> used to make certain
words stand out. It is followed by an <b>unordered list</b>
with</p>
<ul type='square'>
<li>two items, and</li>
<li>square bullets.</li>
</ul>
"""

answer = ['p', 'em', 'b', 'b', 'ul', 'li', 'li']

attempt(findall('YOUR REGEX', question))



##--------------------------------------------------------------------
##
##    Challenge 6: The text below contains certain phrases
##    which have been marked up with HTML tags.  Your goal is to
##    return the annotated phrases, but not the tags.
##

challenge_no = 6

question = """
Flightless birds are those that <em>lack the ability to fly</em>;
i.e., they rely on their ability to run or swim.  There are about
<big>forty species</big> in existence today, e.g., the
<b>ostrich</b>, <b>emu</b>, <b>cassowary</b>, etc.  Like all
birds they lay eggs.
"""

answer = ['lack the ability to fly', 'forty species',
          'ostrich', 'emu', 'cassowary']

attempt(findall('YOUR REGEX', question))



##--------------------------------------------------------------------
##
##    Challenge 7: Given some text, extract all URLs it contains.
##    We assume that a URL begins with either 'http://' or 'https://',
##    followed by non-empty '/'-separated segments, each containing
##    lower-case alphabetic characters and full stops '.' only.

challenge_no = 7

question = """
Google's URL is http://www.google.com.au, you can get help
for Wikipedia from http://en.wikipedia.org/wiki/help and
you can get lots of information from QUT Virtual at
https://qutvirtual.qut.edu.au (once you figure out how to
navigate around the site).
"""

answer = ['http://www.google.com.au', 
          'http://en.wikipedia.org/wiki/help', 
          'https://qutvirtual.qut.edu.au']

attempt(findall('YOUR REGEX', question))



##--------------------------------------------------------------------
##
##    Challenge 8: Hyphens serve a number of purposes in english.
##    In the following text find just those words containing exactly
##    two hyphens.  Words with one hyphen or numbers should not
##    be matched.
##

challenge_no = 8

question = """
Out-of-date phone numbers, such as 03-534-8011, are of little
use to us in this new-fangled digital age.  Did you know that
the plural of mother-in-law is mothers-in-law?  English changes
rapidly -- not too long ago words like to-day and to-morrow were
hyphenated, but no-one would do so today.
"""

answer = ['Out-of-date', 'mother-in-law', 'mothers-in-law']

attempt(findall('YOUR REGEX', question))



##--------------------------------------------------------------------
##
##    Challenge 9: Binary data received from a communications channel
##    typically arrives in the form of discrete "packets".  Each packet is a
##    sequence of bits (binary digits) and must conform to a specific format
##    to be interpreted correctly at the receiving end.  Given a sequence of
##    packets, one per line, extract only those packets that both
##    begin and end with three 1s, e.g., '111010111'.  The packets can
##    have any number of bits in between these beginning and ending
##    markers.  Furthermore, the beginning and ending sequences must be
##    distinct.  Thus '1111' is not a valid packet, even though it both
##    begins and ends with three 1s, because the beginning and ending
##    overlap.
##
##    NB: You will probably find it helpful to use patterns '^' and '$'
##    to refer to the beginning and ending of a line of text in the
##    question string, respectively, so we have included the MULTILINE tag
##    in the call to the findall function to indicate that the question
##    string contains multiple lines of text.
##

challenge_no = 9

question = """
111
111111
11111111
11101111
1110101010111
11100000011
111001110
1110001011
001110011100
"""

answer = ['111111', '11111111', '11101111', '1110101010111']

attempt(findall('YOUR REGEX', question, MULTILINE))



##--------------------------------------------------------------------
##
##    Ultimate Challenge 10: In the following text there are
##    nine words that begin and end with the same two letters.
##    For instance, 'educated' both begins and ends with 'ed'.  Your
##    challenge is to find all the pairs of letters that both begin
##    and end the same word.  We require that the two letters at
##    the beginning and end of the word are separate, so a word
##    like 'at' is excluded even though it both begins and ends
##    with the same two letters.  The result should be case sensitive,
##    so 'dodo' should be considered to be such a word, but 'Dodo'
##    should not.  Your solution should return both the word and
##    two matching letters.  Hint: Recall that if a regular
##    expression contains more than one group then all groups
##    are returned by "findall".  NB: This is HARD!  To solve
##    this problem you will need to use a "backreference" as
##    explained in the appendix to the lecture notes.
##

challenge_no = 10

question = """
The dodo was one of the sturdiest birds.  An educated termite may
learn how to operate a phonograph, but it's unlikely.  I sense
that an amalgam that includes magma will enlighten Papa.
"""

answer = [('dodo', 'do'), ('sturdiest', 'st'), ('educated', 'ed'),
          ('termite', 'te'), ('phonograph', 'ph'),
          ('sense', 'se'), ('amalgam', 'am'), ('magma', 'ma'),
          ('enlighten', 'en')]

attempt(findall(r'YOUR REGEX', question))



##--------------------------------------------------------------------
##
##    Finish up - Display the final score.
##

print('Your score: ' + str(score) + '/' + str(challenge_no))



