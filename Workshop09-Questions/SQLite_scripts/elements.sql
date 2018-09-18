-- This script creates the tables needed for the
-- "Elements Database" exercise.  Import and
-- run this script in your database browser interface to
-- create and populate the database.

-- 1. Create the tables 

CREATE TABLE atomic_symbols (
   element  VARCHAR(30) NOT NULL,
   symbol   VARCHAR(2) NOT NULL,
   PRIMARY KEY (element)
);

CREATE TABLE atomic_numbers (
   element  VARCHAR(30) NOT NULL,
   number   INTEGER(3) NOT NULL,
   PRIMARY KEY (element)
);

-- 2. Populate the tables with the first 20 elements

INSERT INTO atomic_symbols
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
       ('Calcium', 'Ca');

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
       ('Calcium', 20)
