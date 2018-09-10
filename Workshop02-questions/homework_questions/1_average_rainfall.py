# Highest average rainfall
#
# THE PROBLEM
#
# This exercise tests your ability to use lists in Python.
# Assume the following values have already been entered into the
# Python interpreter, denoting the rainfall in millimetres recorded
# for several Queensland towns over a one month period.  No
# record was made for days when it didn't rain, so each of the
# lists is of a different length.

aurukun =  [15, 9, 11, 4, 10, 20, 95]
burdekin = [13, 9, 5, 80, 150, 145]
cardwell = [115, 90, 100, 46, 130, 200, 195, 10, 3, 8]
daintree = [140, 120, 110, 53, 100, 50, 175]
tully =    [115, 90, 100, 130, 200, 195]

# Write code to calculate the highest average rainfall
# and print the result in a meaningful message to the screen.
#
# HINTS:
# * Use the following built-in functions: sum, len and max.
# * Your task is to find the highest average rainfall - NOT the
#   town with the highest average rainfall.
# * The correct answer is 138mm.

aurukun_avg = sum(aurukun)/len(aurukun);
burdekin_avg = sum(burdekin)/len(burdekin);
cardwell_avg = sum(cardwell)/len(cardwell);
daintree_avg = sum(daintree)/len(daintree);
tull_avg = sum(tully)/len(tully);

rain_max = max(aurukun_avg, burdekin_avg, cardwell_avg, daintree_avg, tull_avg);

print("The highest avarage rainfall is ", int(rain_max), 'mm');
