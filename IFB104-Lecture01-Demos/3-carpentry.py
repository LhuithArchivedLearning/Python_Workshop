######################################################################
#
# Carpentry
#
# A carpenter is required to saw planks into 4 equal size pieces.
# He saws the planks at the rate of 5 cuts per minute.  How many
# planks does he fully complete sawing in 13 minutes?
#

total_number_of_cuts = 13 * 5 # Minutes times cuts per minute

number_of_cuts_per_plank = 3 # Not four!  Three cuts make four pieces!

number_of_planks_cut = total_number_of_cuts // number_of_cuts_per_plank # Whole-number arithmetic

print('He cuts', number_of_planks_cut, 'whole planks') # Answer is 21 (with one unfinished)

