from math import pi
#My Solution to the Earth vs Moon

#dry land area of the earth
earth_a = 5.1*(10**8);
earth_w_a = earth_a * 0.71;
earth_d_l = earth_a - earth_w_a;

#Moon Dry Land Area
moon_rad = 3475//2;
moon_d_l = 4 * pi * ((moon_rad) ** 2);


if moon_d_l >= earth_d_l :
    print("Moon is Bigger = ", round(moon_d_l));
else :
    print("Earths Huge man");


    
