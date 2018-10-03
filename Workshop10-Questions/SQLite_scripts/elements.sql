-- This script creates the database needed for the
-- "Elements Database" exercises.  Either import or
-- run this script in your favourite GUI to create
-- and populate the database.

-- 1. Create the tables 

CREATE TABLE symbols (
   element_name   VARCHAR(30) NOT NULL,
   symbol         VARCHAR(2) NOT NULL,
   PRIMARY KEY (element_name)
);

CREATE TABLE atomic_numbers (
   element_name   VARCHAR(30) NOT NULL,
   atomic_number  INTEGER(3) NOT NULL,
   PRIMARY KEY (element_name)
);

-- 2. Populate the tables with the first 20 elements

INSERT INTO symbols
VALUES ('Hydrogen', 'H'),
       ('Helium', 'He'),
       ('Lithium', 'Li'),
       ('Beryllium', 'Be'),
       ('Boron', 'B'),
       ('Carbon', 'C'),
       ('Nitrogen', 'N'),
       ('Oxygen', 'O'),
       ('Fluorine', 'F'),
       ('Neon', 'Ne'),
       ('Sodium', 'Na'),
       ('Magnesium', 'Mg'),
       ('Aluminium', 'Al'),
       ('Silicon', 'Si'),
       ('Phosphorous', 'P'),
       ('Sulphur', 'S'),
       ('Chlorine', 'Cl'),
       ('Argon', 'Ar'),
       ('Potassium', 'K'),
       ('Calcium', 'Ca'),
       ('Kryptonite', 'Kr'),
       ('Dalekanium', 'Dk');

INSERT INTO atomic_numbers
VALUES ('Hydrogen', 1),
       ('Helium', 2),
       ('Lithium', 3),
       ('Beryllium', 4),
       ('Boron', 5),
       ('Carbon', 6),
       ('Nitrogen', 7),
       ('Oxygen', 8),
       ('Fluorine', 9),
       ('Neon', 10),
       ('Sodium', 11),
       ('Magnesium', 12),
       ('Aluminium', 13),
       ('Silicon', 14),
       ('Phosphorous', 15),
       ('Sulphur', 16),
       ('Chlorine', 17),
       ('Argon', 18),
       ('Potassium', 19),
       ('Calcium', 20),
       ('Kryptonite', 21),
       ('Dalekanium', 22)
