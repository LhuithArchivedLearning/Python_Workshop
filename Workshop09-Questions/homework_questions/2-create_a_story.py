#----------------------------------------------------------------
#
# Create your own story
#
# In this exercise you will practice iterating over both lines
# in a file and items in a list.
#
# Publishers offer customised gift books for children in which
# the child's name is inserted into the book as the protagonist.
# Here you will do this using the names of your teammates in the
# workshop and the first chapter of the book "The Secret of the
# Old Mill" by Enid Blyton.
#
# "The Secret of the Old Mill" is the first of the many "Secret
# Seven" adventures.  In this first installment Peter and Janet
# discuss creation of their secret group, accompanied by
# Scamper the dog.  The other members of the seven, Colin,
# Jack, Pam, George and Barbara are mentioned briefly in the
# final paragraphs.
#
# Your task is to create a new version of the story with your
# name and those of your classmates replacing the secret seven.
# Below are two lists, the original names and their replacements.
# Substitute your chosen names for the replacements, and then
# write a program which displays the contents of file
# "TheSecretOfTheOldMill.txt" with your choices of names
# replacing those of the original characters.
#


#----------------------------------------------------------------
#
# These lists define the original and new names (put your names
# into the second list instead of the placeholders)
#
old_names = ['Peter', 'Janet', 'Colin', 'Jack', 'Pam', 'George', 'Barbara']
new_names = ['AAAAA', 'BBBBB', 'CCCCC', 'DDDDD', 'EEEEE', 'FFFFF', 'GGGGG']


#----------------------------------------------------------------
#

# Open the file
story = open('TheSecretOfTheOldMill.txt', 'U')

##### DEVELOP YOUR PROGRAM HERE
# Read each line of the story, replace all occurrences of old names
# with new ones, and print the updated line

# Close the file
story.close()
