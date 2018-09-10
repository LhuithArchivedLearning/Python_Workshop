######################################################################
#
# Earth vs Moon
#
# The surface area of the earth is 5.1 x 10^8 sq km, and
# 71% of the earth's surface is covered in water.
# The diameter of the moon is 3,475 km, and there is no
# water on the surface of the moon.
# Which has more dry land, the earth or the moon?
#
# [Quiz question from Time magazine]


# First calculate the amount of dry land on the earth

earths_surface_area = 5.1 * (10 ** 8) # sq km

earths_water_area = earths_surface_area * 0.71

earths_dry_land = earths_surface_area - earths_water_area


# Now calculate the moon's surface area
# Remember that the surface area of a sphere is 4 pi r^2

moons_radius = 3475 / 2 # km

from math import pi

moons_surface_area = 4 * pi * (moons_radius ** 2) # sq km

moons_dry_land = moons_surface_area


# Now display the results, truncated to whole numbers

print('Earth:', int(earths_dry_land), 'sq km of dry land')
print('Moon:  ', int(moons_dry_land), 'sq km of dry land')

