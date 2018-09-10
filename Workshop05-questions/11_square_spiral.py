#---------------------------------------------------------
#
# Square spiral
#
# This problem can be solved either iteratively (with a
# WHILE or FOR loop) or recursively (via a function that
# calls itself), but for practice we recommend you try
# solving it recursively.
#
# You are to develop a recursive function to draw a "spiral"
# formed from straight lines.  The spiral should be made of
# lines of increasing length at right angles to each other.
#
# 1) Your recursive function should have one parameter, the
#    current line length.
# 2) At each recursive step the function should draw
#    just one line, turn 90 degrees and then call itself
#    with a slightly longer length.
# 3) To limit the recursion, the function should just
#    call the "hideturtle" method when the given line
#    length exceeds a fixed limit.
#
# See file "square_spiral.pdf" for an example of the
# expected output.
#

from turtle import *

#---------------------------------------------------------
#

#### DEFINE YOUR square_spiral FUNCTION HERE


#---------------------------------------------------------
#
# This main program calls your function to start the
# process
# 
setup()
title("Square spiral")
speed("fast")
# square_spiral(1) # start with a line one pixel long
done()
