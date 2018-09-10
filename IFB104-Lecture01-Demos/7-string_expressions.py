######################################################################
#
#  Demonstration - Character strings
#
#  Note: This file contains various expressions which are evaluated
#  and the result is printed.  You should run this file and then
#  compare the expressions below with each line that is printed to
#  the screen.


# Strings can be delimited by either single or double quotes:

print("Hello")

print('World')

print("Goodbye" is 'Goodbye')  # these are the same,
                               # but it's best to stick with one style


# But since quote marks tell the Python interpreter where a string
# begins and ends we can precede quotes that we want to appear
# inside a string with the special "escape" character "\":

print('Alice said, \'Curiouser and curiouser!\'')


# Alternatively, we can enclose a single quote within a double-
# quoted string and vice versa:

print("Then listen to this, 'I am Mr Ed!'")

print('Then listen to this, "I am Mr Ed!"')


# Printing nothing at all produces a blank line

print()


# If a string is too long to fit comfortably on one line you can
# use a backslash at the end of a line as a "continuation"
# character:

print('A horse is \
a horse,')

print('Of course, \
of course,')


# Conversely, if you actually want a "newline" marker to
# appear in a string you can embed it as the escape
# sequence "\n":

print('And no one can talk to a horse,\nOf course.')


# Alternatively, you can use a triple-quoted string to embed
# newlines as they appear in the source code:

print('''That is,
Of course,
Unless the horse,
Is the famous Mr Ed!
''')

print('''first
second''' is 'first\nsecond')


# New strings can be constructed from others by concatenation and
# repetition:

print('Hello' + ' ' + 'World' + '!')

print('Ho, ' * 3 + 'Merry Christmas!')


# Finally, we can extract individual characters from strings by
# indexing, counting from zero:

print('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[2])

print('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[25])

print('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[4:9]) # from index 4, inclusive, to 9, exclusive


# Lyrics quoted from "Mr Ed Main Title" by Jay Livingston and
# Ray Evans (1961)

