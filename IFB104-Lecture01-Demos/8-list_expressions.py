######################################################################
#
#  Demonstration - List expressions
#
#  Note: This file contains various expressions which are evaluated
#  and the result is printed.  You should run this file and then
#  compare the expressions below with each line that is printed to
#  the screen.


# Lists can be formed from items of different types, including
# sublists:

print([1, 2, 3])

print(['a', 'bb', 'ccc', 'dddd'])

print([10, 'x', 9, 'y', 8, 'z'])

print([[1, 'a'], [2, 'b'], [3, 'c']])


# Lists are a "sequence" type like strings and share many of the same
# operators:

print([1, 2, 3] + [4, 5])

print(['Ho'] * 3)


# The "len" function tells us how long a list is:

numbers_and_letters = [10, 'x', 9, 'y', 8, 'z']

print(len(numbers_and_letters))

print(len([[1, 'a'], [2, 'b'], [3, 'c']]))  # doesn't print 6 - why?


# Lists can be indexed using natural number indices in
# the same way as strings:

a_to_dddd = ['a', 'bb', 'ccc', 'dddd']

print(a_to_dddd[0]) # prints the first item in this list

print((['a', 'b', 'c'] + ['d', 'e'])[3])


# Something we can do with lists, that we can't do with
# strings, is to replace values (this is because lists
# are "mutable"):

the_three_stooges = ['Moe', 'Curly', 'Larry']

print(the_three_stooges)

the_three_stooges[1] = 'Shemp'  # replaces Curly with Shemp

print(the_three_stooges)
