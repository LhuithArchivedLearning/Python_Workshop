jelly = "jelly"
icecream = "icecream"
honey = "honey"

jelly = icecream;
icecream = honey;
honey = jelly;

print("Jelly "+jelly);
print("icecream "+icecream);
print("honey "+honey);

width = 2
depth = 1.5
footprint = width * depth;

print(type(width))

rock = 1
paper = 2
scissors = 3
lizard = 4
spock = 5

print(format(rock) + " " + format(paper) + " " + format(scissors) + " " + format(lizard) + " " + format(spock));


temp = scissors
scissors = lizard
lizard = spock
spock = rock
rock = paper
paper = temp

print(format(rock) + " " + format(paper) + " " + format(scissors) + " " + format(lizard) + " " + format(spock));
