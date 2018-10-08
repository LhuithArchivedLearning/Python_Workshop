#----------------------------------------------------------
#
#  Multiplier with GUI
#
#  The GUI program below presents the user with a small
#  window containing two text entry fields and a button
#  labelled 'Multiply'.  By entering a number and another
#  value in the fields and pressing the button the user
#  can multiply the second value by the number, e.g.,
#  2 * 3 produces 6 and 'Ha ' * 3 produces 'Ha Ha Ha '
#  and 6 * ['a'] produces [a', 'a', 'a', 'a', 'a', 'a'].
#
#  However, this program is fragile because it produces
#  error messages relating to unhandled exceptions
#  if the user enters operands in the text entry boxes
#  that don't form a valid Python expression when
#  multiplied.
#
#  Your job is to extend the code below so that it
#  never crashes, even if the user enters invalid
#  operands.  Furthermore, you should provide some form
#  of visual feedback to the user when their operands are
#  invalid.
#


# Import the GUI API
from tkinter import *


# Get the current operands in the text entry fields
# and multiply them
def multiply():
    result_display.delete(0.0, END)
    result_display.insert(END, str(eval(first_value.get() + '*' + second_value.get())).rjust(10))
    result_display['bg'] = 'light green'
       
    
# Create the interactive window
mult_window = Tk()
mult_window.title('Multiplier')

# Create a text area to display results
result_display = Text(mult_window, width = 10, height = 1,
                      borderwidth = 2, relief = 'groove',
                      bg = 'light green', font = ('Arial', 28))
result_display.pack(pady = 5, padx = 5)

# Create a text entry field for the user to enter the first operand
first_value = Entry(mult_window, width = 10,
                    font = ('Arial', 24), justify = RIGHT)
first_value.pack(padx = 15)

# Create a text entry field for the user to enter the second operand
second_value = Entry(mult_window, width = 10,
                     font = ('Arial', 24), justify = RIGHT)
second_value.pack(padx = 15)

# Create a button that multiplies the operands
multiply_button = Button(mult_window, text = ' Multiply ',
                         activeforeground = 'red',
                         font = ('Arial', 24), command = multiply)
multiply_button.pack(pady = 5)

# Start the event loop to react to user inputs
mult_window.mainloop()
