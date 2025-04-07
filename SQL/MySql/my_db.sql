## Created a random database to perform all kind of basic sql quary.
## My preference, open this file with MySQL software.

## create a database:
CREATE DATABASE my_db;              # or 'IF NOT EXISTS' can be use. Like, 'CREATE DATABASE IF NOT EXISTS  my_db;'

## show all created databases:
SHOW DATABASES;

## use the database:
USE my_db;

## create a table:
CREATE TABLE tr_table (
	customer_id INT PRIMARY KEY,       # PK is unique and not null
	customer VARCHAR(50),
    # age INT NOT NULL DEFAULT 21,     # sets a default age in every row
    # age INT CHECK (age > 20),        # 'CHECK' keyword, basic syntax 'CONSTRAINT constraint_name CHECK (constraint1, constraint2, ...)'
	mode VARCHAR(50),
	city VARCHAR(50)
);

## insert entry in table:
INSERT INTO tr_table
VALUES
(101, 'Olivia Barrett', 'Netbanking', 'Portland'),
(102, 'Ethan Sinclair', 'Credit Card', 'Miami'),
(103, 'Maya Hernandez', 'Credit Card', 'Seattle'),
(104, 'Liam Donovan', 'Netbanking', 'Denver'),
(105, 'Sophia Nguyen', 'Credit Card', 'New Orieans'),
(106, 'Caleb Foster', 'Debit Card', 'Minneapolis'),
(107, 'Ava Patel', 'Debit Card', 'Phoenix'),
(108, 'Lucas Carter', 'Netbanking', 'Boston'),
(109, 'Isabella Martinez', 'Netbanking', 'Nashville'),
(110, 'Jackson Brooks', 'Credit Card', 'Boston');

## select and view columns:
SELECT * FROM tr_table;                                               # to select all
SELECT customer_id, customer FROM tr_table;                           # to select specific
SELECT DISTINCT mode FROM tr_table;                                   # shows all distinct mode names
# SELECT * FROM tr_table WHERE mode = 'Credit Card' AND age > 20;     # select with where cause, logical and copparison opertor
# SELECT * FROM tr_table WHERE age BETWEEN 21 AND 30;                 # 'BETWEEN' keyword (80 and 90 inclusive)
SELECT * FROM tr_table WHERE city IN ('Boston', 'Denver');            # 'IN' keyword ('Boston' and 'Denver' inclusive)
SELECT * FROM tr_table WHERE city NOT IN ('Boston', 'Denver');        # 'NOT IN' keyword
SELECT * FROM tr_table LIMIT 6;                                       # 'LIMIT' keyword

SELECT * FROM tr_table
ORDER BY city                     # order by clause (to sort ASC or DESC), default value 'ASC'
LIMIT 6;                          # (optional)


## show all created tables:
SHOW TABLES;

SELECT mode, COUNT(customer)
FROM tr_table
GROUP BY mode;

ALTER TABLE tr_table
CHANGE customer customer_name VARCHAR(50);

ALTER TABLE tr_table
ADD COLUMN age INT NOT NULL DEFAULT 30;

ALTER TABLE tr_table
DROP COLUMN age;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM tr_table
WHERE mode = 'Debit Card';

TRUNCATE TABLE tr_table;

DROP TABLE tr_table;

DROP DATABASE my_db;