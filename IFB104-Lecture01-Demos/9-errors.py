######################################################################
#
#  Demonstration - Syntactic and semantic errors
#
#  Note: This file contains (deliberate) errors, so you can't "run"
#  it in IDLE.  To see the result of trying to evaluate one of
#  the expressions below you must copy it into Idle's interpreter
#  window and hit the Enter key.


# A "syntactic error" is caused by entering a malformed expression:

3 + )6 * 7)  # has a bracket around the wrong way


# Similarly, using operators or functions that Python doesn't know
# about will produce error messages:

4.0 + flot(5)  # includes a misspelling of "float"


# A "static semantic" error usually results from trying to use
# operators in the wrong way:

3 + 'x'  # doesn't make sense because you can't add numbers and text


# The hardest type of error to resolve is a "runtime" or "semantic"
# error in which the program gets part way through a calculation
# before something goes wrong:

(9 * 7) / ((6 + 2) - 8)  # looks OK until you try to evaluate it


# Most importantly, whenever you get an error, read the error
# message carefully (especially the last line) because it (usually)
# gives you some idea of how to fix it!
