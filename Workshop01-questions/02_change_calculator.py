# Change Calculator
#
# THE PROBLEM
#
# You need to calculate how much change is due when you go shopping.
# You have a $20 note and buy the following:
#   2 cartons of milk @ $2.50
#   5 Mars bars @ $1.20 each
#   1 pkt indigestion tablets @ $3.50
#
# Write an expression to calculate the change you should be given
# from $20, after buying those groceries.  Display the value of the
# change in a message to the screen.

# HINTS:
# * You will need to use built-in mathematical operators: *, + and -
# * You may like to introduce variables to accumulate and store values
# * The Python function call "print(E)" will print the value of expression E


global total_cash;
total_cash = 20.00;

#add function later
def DeductFromTotal(amount):
    global total_cash;
    total_cash -= amount;

milk_cost = 2.50;
marsbar_cost = 1.20;
i_tablets_cost = 3.50;

#incase # of products change eg. 6 milks or 3 i_tablets

total_milk = milk_cost * 2.0;
total_mars = marsbar_cost * 5.0;
total_i_tablets = i_tablets_cost * 1.0;

total_amount = total_milk + total_mars + total_i_tablets;

#total_cash = total_cash - total_amount;

DeductFromTotal(total_milk);
DeductFromTotal(total_mars);
DeductFromTotal(total_i_tablets);

print ("Your Change Is: " + "$" + format(total_cash, '.2f'));



