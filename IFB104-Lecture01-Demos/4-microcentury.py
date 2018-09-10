######################################################################
#
# Microcentury
#
# When asked how long his lectures were, Professor
# Julius Sumner Miller usually answered "about a
# microcentury."  As an example involving assignments, we
# can write a program to tell us how long a microcentury is
# in whole minutes.

minutes_per_hour = 60

hours_per_day = 24

minutes_per_day = minutes_per_hour * hours_per_day

days_per_year = 365

years_per_century = 100

minutes_per_century = minutes_per_day * days_per_year * years_per_century

microcentury = minutes_per_century / 1000000 # "micro" means one millionth

print('A microcentury is about', round(microcentury), 'minutes')
