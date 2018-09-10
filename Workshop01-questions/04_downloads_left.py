# Music download credits
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the cost in cents for downloading one
# music track, your original budget in dollars, and the number of tracks
# already downloaded:

track_cost = 120 # cost in cents for downloading one track
budget = 50 # dollars
num_downloaded = 15 # number of tracks already downloaded

# Write expressions to calculate how many more tracks you can afford
# to download and print that value to the screen.
#
# A problem solving strategy:
# 1. Calculate the amount spent so far by
#    multiplying the number downloaded by the track cost
# 2. Calculate the balance left by
#    deducting the amount spent so far from the budget
# 3. Divide the balance left by the track cost to a whole number
# 4. Print the number of tracks left
#
# Be careful to allow for the fact that one of the given values
# is expressed in cents and the other is in dollars, i.e., the
# units associated with the values are different.

currently_spent = track_cost * num_downloaded;
remainingbudget = (budget * 100) - currently_spent;

#number of songs 50 dollars will get u
maxsongamount = 5000/120;

#max songs for 50 - # currently downloaded
remainingsong = maxsongamount - num_downloaded;

print("Able to buy " + format(int(remainingsong), '.0f') + " songs with " + "$" + format(remainingbudget/100, '.2f') + " remaining");

