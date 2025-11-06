# Database
A place to store data in an organized way.

# 2 types:
1. SQL - mysql, postgres
2. NoSQL - Mongodb

# SQL - Structured query language
Language to communicate with databses and retrieve and update data

# DBMS - Database Management System
It a software used to store the data.

# Postrgesql
https://pg-sql.com/

# Tables - relations
Tables contains columns and rows

1. Which data are we storing?
2. What columns do we need?
3. Data type

# Create a languages table
CREATE TABLE languages (language VARCHAR(50), speakers INTEGER, family VARCHAR(50));


# CRUD Operations - Create, Read, Update and Delete

# Create
--------
# Insert data into the table
INSERT INTO languages (language, speakers, family)
VALUES ('Mandarin Chinese', 990, 'Sino-Tibetan');

# Insert multiple values into the table
INSERT INTO languages (language, speakers, family)
VALUES ('Spanish', 484, 'Indo-European'),
	   ('English', 390, 'Indo-European'),
       ('Hindi',   345, 'Indo-European');


# Read
-------
# Retrieve all rows from the table
SELECT * FROM languages;

# Retrieve specific column from the table
SELECT language FROM languages;

# Filter data from the table
SELECT * FROM languages 
WHERE family = 'Indo-European';

# Update
--------
# Update a row from the table
UPDATE languages
SET speakers = 260
WHERE language = 'Portuguese';

# Delete
--------
# Delete a row from the table
DELETE FROM languages
WHERE language = 'Hindi'

--------------------------------------------------

# Transform or process data before we receive it
Lets says we created a cities table with columns name, country, population and area.

SELECT name, population / area AS population_density 
FROM cities;

# String Operators and Functions
|| = Join two strings
CONCAT() = Join two strings
LOWER() = Gives lower case string
LENGTH() = Gives number of characters
UPPER() = Gives upper case string

# Join two strings
SELECT name || ', ' || country AS location FROM cities;
SELECT CONCAT(name, ', ', country) AS location FROM cities;

# Uppercase
SELECT CONCAT(UPPER(name), ', ', UPPER(country)) AS location FROM cities;
SELECT UPPER(CONCAT(name, ', ', country)) AS location FROM cities;