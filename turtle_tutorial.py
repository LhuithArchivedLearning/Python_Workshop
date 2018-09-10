#Draw a Pretty Picture

#import Tutrtle

from turtle import*



def DrawPacMan() :
    {
    }

#setup Window
setup();
title('Pacman');
bgcolor('black');

#choose some colors
pencolor('black');
fillcolor('yellow');

#choose some Pacman properties
diametre = 350;
position = [0, 0];

#draw lots of packman
for pacman in range(7) :
    goto(position);
    pendown();
    #draw pacmans head
    begin_fill();
    setheading(30);
    forward(diametre // 2);
    left(90);
    circle(diametre // 2, extent = 300);
    goto(position);
    end_fill();
    #draw pacmans eye
    setheading(100);
    penup()
    forward(diametre // 4);
    dot(diametre // 7, 'black');

    # Change Position up to the right
    position = [position[0] + 100 , position[1] + 75];

#close program
hideturtle();
done();
