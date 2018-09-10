#percentage calculator

from tkinter import *


#Back end function to calculate percentages
def compute(numer, denom) :
    return str(round((numer * 100) / denom));

#bit in the middle
def calculate_and_display() :
    numer = numerator.get();
    denom = denomonator.get();
    answer = compute(int(numer), int(denom));
    result['text'] = answer + '%';
 

# The front end user interface  
#Create the window
calculator = Tk();
calculator.title("Percentages");

#Creating Widgets
numerator = Entry(calculator, font = ('Arial', 32), width = 4);
numerator.pack();

denomonator = Entry(calculator, font = ('Arial', 32), width = 4);
denomonator.pack();

result = Label(calculator, font = ('Arial', 32), text = '????');
result.pack();

start = Button(calculator, font = ('Arial', 32), text = 'Calculate',
               command = calculate_and_display);
start.pack();




#Start the event loop
calculator.mainloop();
