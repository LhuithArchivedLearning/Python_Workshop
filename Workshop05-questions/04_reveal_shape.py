#---------------------------------------------------------------------
#
# Reveal Coded Shape
#
# This exercise will give you practice at using data stored in a list.
#
# Each of the sets of data below describes a simple shape encoded as a
# list of pairs.  The first element of the pair is a character C and the
# second is a number N.  To reveal the shape encoded in the data set
# you must write a program which, for each pair, prints N copies of C.
#
# Hint: You should build a string by processing the items in the
# list and then print the result at the end.
#

rectangle = [['+', 1],
             ['-', 5],
             ['+', 1],
             ['\n', 1],
             ['|', 1],
             [' ', 5],
             ['|', 1],
             ['\n', 1],
             ['|', 1],
             [' ', 5],
             ['|', 1],
             ['\n', 1],
             ['|', 1],
             [' ', 5],
             ['|', 1],
             ['\n', 1],
             ['+', 1],
             ['-', 5],
             ['+', 1]]

triangle = [[' ', 5],
            ['^', 1],
            ['\n', 1],
            [' ', 4],
            ['/', 1],
            [' ', 1],
            ['\\', 1],
            ['\n', 1],
            [' ', 3],
            ['/', 1],
            [' ', 3],
            ['\\', 1],
            ['\n', 1],
            [' ', 2],
            ['/', 1],
            [' ', 5],
            ['\\', 1],
            ['\n', 1],
            [' ', 1],
            ['/', 1],
            [' ', 7],
            ['\\', 1],
            ['\n', 1],
            ['<', 1],
            ['-', 9],
            ['>', 1]]

circle = [[' ', 4],
          ['*', 1],
          [' ', 2],
          ['*', 1],
          ['\n', 1],
          [' ', 1],
          ['*', 1],
          [' ', 8],
          ['*', 1],
          ['\n', 1],
          ['*', 1],
          [' ', 10],
          ['*', 1],
          ['\n', 1],
          ['*', 1],
          [' ', 10],
          ['*', 1],
          ['\n', 1],
          [' ', 1],
          ['*', 1],
          [' ', 8],
          ['*', 1],
          ['\n', 1],
          [' ', 4],
          ['*', 1],
          [' ', 2],
          ['*', 1]]



##### PUT YOUR CODE TO PRINT THE SHAPE ENCODED IN EACH DATA SET BELOW

def create_shape(data_list):
    for index in range(len(data_list)):
        steps = int(data_list[index][1]);
        for i in range(steps):
            print(data_list[index][0], end = '');

create_shape(rectangle);
print(" ");
create_shape(triangle);
print(" ");
create_shape(circle);
