
/* A simple "dump" script to recreate the table needed
   for Assignment 2, Part B.  If you choose to use this
   script to re-create the database, make sure that you
   name it "top_ten.db". */

CREATE TABLE "top_ten" (
	`publication_date`	TEXT NOT NULL,
	`ranking`	INTEGER NOT NULL,
	`item`	TEXT NOT NULL,
	`main_attribute`	TEXT NOT NULL
);

