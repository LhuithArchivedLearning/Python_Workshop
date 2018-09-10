# Average speed
#
# Imagine that you get on your bicycle and travel from
# your home to QUT at 30 km/hr.  After a hard day's
# study you cycle home again more slowly at 20 km/hr.
#
# Quickly now, what is your average speed for the whole
# round trip?  Be careful - most people get this
# wrong!  (Thanks to Professor Julius Sumner Miller for
# this brainteaser.)
#
# To check the correct answer, complete the code below.
# We have chosen an arbitrary distance of 6 km between
# your house and the university but the result is the
# same regardless of the distance.


# Given values:

distance = 6 # km

s_to_uni = 30 # km/hr

s_to_home = 20 # km/hr


# Complete the following code by replacing the zeros:

time_to_get_to_uni = distance / s_to_uni; # hours

time_to_get_home = distance / s_to_home # hours

total_travelling_time = (time_to_get_home + time_to_get_to_uni) # hours

total_distance_travelled = distance * 2; # km

speed_for_round_trip = total_distance_travelled / total_travelling_time # km/hr

print ('The average speed for the round trip was', speed_for_round_trip, 'km/hr');

