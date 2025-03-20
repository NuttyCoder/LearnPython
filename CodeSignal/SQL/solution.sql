-- Databases and SQL
-- A database is like a huge, digital filing cabinet where you can store, manage, and retrieve data. In this course, 
-- we'll focus on a specific type of database known as a relational database. A relational database stores data in tables, 
-- much like how an Excel file has different sheets for different sets of data.

-- Now, SQL, which stands for Structured Query Language, is the standard language used to interact with these databases. 
-- Think of it as a toolbox for managing and manipulating data. Whether you want to find a specific piece of data, update it, 
-- delete it, or create a new one, SQL is your go-to resource.

-- SQL and Its Tools - Introduction to MySQL
-- The tool we're going to use in these lessons is MySQL. While there are multiple database management systems that use SQL, 
-- such as PostgreSQL and SQLite, MySQL is a well-established, flexible tool. That's why we've chosen it to kickstart our SQL journey.

-- Additionally, MySQL's widespread use and supportive community make it an excellent starting point for beginners, 
-- ensuring you can find help and resources easily as you learn.

-- Your Dataset - SQL for Online Shopping
-- To make our data journey engaging, we're using a dataset that captures various aspects of an online shopping platform. 
-- This dataset includes detailed records of categories, customers, products, orders, and order items. For now, let's focus on one table: Categories. Here's the Categories table:

category_id	category_name
1	          Flashcards
2	          Worksheets
3          	Guides
4	          Podcasts
5	          Courses
-- This table records each category with a unique identifier and the name of the category. With this in mind, let's move on to writing our first simple SQL command.

-- ---------------------> The SHOW TABLES Command
-- Sometimes you might want to know what tables are present in the database you're working with. Here is where the SHOW TABLES command comes in handy:

SHOW TABLES;
-- Executing this command returns a list of all the tables in your current database:

-- Tables_in_practice_db
-- categories
-- customers
-- orderitems
-- orders
-- products

-- Understanding SQL Syntax Essentials
-- Learning SQL syntax effectively is crucial for communicating clearly with databases. Here are some fundamental syntax components to know:

-- Semicolon (;): Serves as the end of a statement, similar to a period in a sentence. Correct usage is crucial for clear command separation. Example: SHOW TABLES;.

-- Comments: Comments are used for adding notes or explanations within your SQL code, which are ignored during execution. SQL supports both single-line and multi-line comments.

-- Single-line comments start with --. The rest of the line after -- is ignored by SQL. For example:
-- This command lists all tables
SHOW TABLES;
-- Multi-line comments are enclosed in /* and */, ignoring everything in between. These are useful for longer explanations or notes. Example:

/*
The following command is used
to display all tables in the database
*/
SHOW TABLES;
-- Grasping the use of semicolons for statement demarcation and comments for annotating your SQL scripts ensures your queries are both effective and easily understandable.

-- Getting to Know a Table - Viewing All Data
-- Next, let's learn how to view all data from a table.


SELECT * FROM Categories;
-- The SELECT keyword is used to specify the data we wish to see. The asterisk * represents our request to see all the data. Lastly, 
-- FROM Categories; instructs the database to display the data from the Categories table.

-- Upon executing this command, we'll receive a comprehensive list of all the data present in the Categories table. You'll get to try it in the practice section that follows.

-- Recap
-- That's a wrap for our first lesson! We've journeyed from understanding the basics of databases and SQL to learning how to write our first query. 
-- Now, you're equipped to display a list of all tables in your dataset using SHOW TABLES; and to view all data from a table with SELECT * FROM Categories;.

-- Now, let's apply our newly acquired knowledge to some practical exercises! The upcoming practice exercises are based on the topics covered in this lesson. 
-- These will reinforce your understanding and help you become comfortable with the basics of SQL.

SHOW TABLES;

-- output

+-----------------------+
| Tables_in_practice_db |
+-----------------------+
| categories            |
| customers             |
| orderitems            |
| orders                |
| products              |
+-----------------------+

  
SELECT * FROM Categories;

--output 

+-------------+---------------+
| category_id | category_name |
+-------------+---------------+
|           1 | Flashcards    |
|           2 | Worksheets    |
|           3 | Guides        |
|           4 | Podcasts      |
|           5 | Courses       |
+-------------+---------------+


-- Navigating the SQL SELECT Statement
-- Greetings, and welcome to our second unit in the "Getting Started with SQL for Online Shopping" course!

-- You have already journeyed through what databases are, explored the world of SQL, and understood the usage of MySQL. 
  --Remember how we wrote our first SHOW TABLES SQL command to list all the tables in our Online Shop database? That was your first step into SQL syntax!

-- SQL, unlike many programming languages, doesn't deal with logic or flow control; instead, it understands, manipulates, 
-- and retrieves data stored in databases in a structured manner.


-- Getting to Know SELECT Syntax
-- In this lesson, we will cover the SELECT keyword. The syntax is straightforward.

-- General Syntax:

SELECT column1, column2, ..., columnN FROM table_name
-- In this syntax, you mention the column names that you want to retrieve, separated by commas. If you want to retrieve all columns, 
-- replace the column names with an asterisk (*).


-- Querying the Database: Select All
-- Let's pull all the data from the Products table. We'll use the asterisk (*) symbol to do this.


SELECT * FROM Products;
-- This statement fetches all columns, along with their data, from the table Products. You would see product_id, product_name, product_price, category_id, 
-- and more, all displaying data related to the products available in the Online Shop.

-- Note: When using SELECT *, the database fetches every column and every row from the specified table. While this is useful for exploring the table’s 
-- structure or inspecting all data at once, it can be inefficient, especially for large tables. For instance, if the Products table has thousands of rows 
-- and includes columns like product_id, product_name, product_price, and category_id, SELECT * retrieves everything — which might include data you don’t need.

-- Best Practice: Use SELECT * sparingly. For precise and efficient queries, always specify the required columns.

SELECT for Specific Columns
-- Now, what if we want only specific information, such as the product name and product price? It's simple. 
-- We replace the asterisk with the required column names. Here's how:

SELECT product_name, product_price FROM Products;
-- In this example, we have fetched only the product_name and product_price columns from our Products table. Isn't fine-tuning our query results exciting?

-- Alias in SQL: Using AS Keyword
-- Can we rename column names in the output for better understanding? Yes, we can! Thanks to SQL aliasing features. 
-- The AS keyword is used to rename a column or table with an alias.


SELECT product_name AS "Product Name", product_price AS Price FROM Products;
-- In this statement, AS is used to rename product_name to "Product Name" and product_price to Price in our output. 
-- Notice that we use double quotes around "Product Name" because the new name contains spaces. This way, our result set has more comprehensible column names.

-- Rules for Using Aliases:

-- Use double quotes (") around the alias if it contains spaces or special characters.
-- Aliases exist only for the duration of the query and do not alter the database schema.
-- The output of this query would be:



Product Name	Price
Vocabulary Flashcards	9.34
Math Problems Flashcards	12.84
Science Facts Flashcards	10.66

-- Wrapping Up: Summary and Preparing for Practice
-- Let's recap what we've covered:

-- SELECT * FROM Products will fetch all columns.
-- SELECT product_name, product_price FROM Products will fetch specific columns.
-- SELECT product_name AS "Product Name", product_price AS Price FROM Products will fetch specific columns and rename them in the output.
-- Practice these commands with different columns and aliases to gain a firm understanding of the SELECT statement. Don't worry if you make mistakes — 
-- they are stepping stones to mastering any new skill. Let's get to practice.

-- That wraps up our second unit! You now understand the SQL syntax, the SELECT command, and the usage of the AS keyword to rename items in the output of your query.

-- The practice exercises that follow this lesson will further reinforce these concepts. Remember, the best way to learn is by doing. 
-- So, try writing and running your own SQL commands before you move on to the practice exercises.

-- TODO: Select product_name and product_price from the Products tabl

SELECT product_name, product_price FROM Products;

+----------------------------------+---------------+
| product_name                     | product_price |
+----------------------------------+---------------+
| Vocabulary Flashcards            |          9.34 |
| Math Problems Flashcards         |         12.84 |
| Science Facts Flashcards         |         10.66 |
| History Events Flashcards        |         13.58 |
| Language Phrases Flashcards      |          5.95 |
| Geography Terms Flashcards       |         10.28 |
| Chemistry Elements Flashcards    |          5.43 |
| Art Styles Flashcards            |          7.11 |
| Grammar Rules Flashcards         |         13.68 |
| Financial Terms Flashcards       |         13.88 |
| Algebra Practice Worksheets      |         17.13 |
| Grammar Exercises Worksheets     |         10.70 |
| Reading Comprehension Worksheets |         11.12 |
| Science Experiment Worksheets    |         23.88 |
| History Timeline Worksheets      |         23.49 |
| Vocabulary Practice Worksheets   |         18.45 |
| Geography Mapping Worksheets     |         10.49 |
| Chemistry Lab Worksheets         |         23.93 |
| Art Creation Worksheets          |         14.72 |
| Budgeting Practice Worksheets    |         24.42 |
| Study Techniques Guide           |         23.81 |
| Essay Writing Guide              |         26.28 |
| Time Management Guide            |         25.69 |
| Research Methods Guide           |         20.97 |
| Critical Thinking Guide          |         16.15 |
| Presentation Skills Guide        |         17.44 |
| Career Planning Guide            |         18.61 |
| Coding Fundamentals Guide        |         27.52 |
| Personal Finance Guide           |         20.84 |
| Public Speaking Guide            |         28.45 |
| History Insights Podcast         |         26.63 |
| Science Discoveries Podcast      |         35.11 |
| Language Learning Podcast        |         22.80 |
| Math Concepts Podcast            |         39.77 |
| Literature Analysis Podcast      |         34.48 |
| Business Trends Podcast          |         30.02 |
| Health and Wellness Podcast      |         39.49 |
| Art History Podcast              |         21.07 |
| Technology Advances Podcast      |         28.74 |
| Psychology Concepts Podcast      |         36.77 |
| Beginner Coding Course           |         84.06 |
| Advanced Writing Course          |        126.90 |
| Personal Finance Course          |        145.49 |
| Data Analysis Course             |         89.67 |
| Public Speaking Course           |        127.36 |
| Graphic Design Course            |         52.96 |
| Language Proficiency Course      |         77.33 |
| Project Management Course        |        149.26 |
| Marketing Strategies Course      |         99.06 |
| Leadership Development Course    |         85.58 |
+----------------------------------+---------------+


-- Introduction
-- Greetings! In the previous lessons, we immersed ourselves in the basics of SQL, learned about databases, and discussed the SELECT statement. 
-- We practiced those concepts using data from an online shopping platform. This lesson brings us to another important aspect of SQL — the WHERE clause. 
-- With this tool, we'll be able to narrow down our data retrieval to only select the records that meet certain conditions.

-- Understanding the WHERE Clause
-- The WHERE clause is an essential part of SQL used to filter records. This clause extracts only those records from a table that fulfill a specified condition. 
-- The WHERE clause can be used with SQL commands like SELECT, UPDATE, DELETE, etc. It significantly enhances our ability to interact with a database by allowing 
-- us to retrieve targeted data instead of complete sets of records.

-- Syntax of WHERE Clause
-- The syntax of the WHERE clause looks like this:

SELECT column1, column2, ...
FROM table_name
WHERE condition;

-- In this syntax, after the SELECT statement and the FROM statement, we add the WHERE clause followed by a condition. 
-- The condition is what we set to filter our data. If the condition is true for a record, then that record is selected.

-- Your Dataset - Orders in Online Shopping
-- Before we dive into examples of using the WHERE clause, let's familiarize ourselves with the Orders table. 
-- This table stores details about orders placed on the online shopping platform and includes the following columns:

order_id	customer_id	order_date	order_status
1	41	2021-08-17	Delivered
2	16	2022-04-03	Processed

-- Example of WHERE Clause Use
-- Let's see the WHERE clause in action to fetch orders from a specific year. 
-- Suppose you want to know all the orders placed after the year 2020. Here's how you would write the SQL query:

SELECT * FROM Orders
WHERE YEAR(order_date) > 2020;
-- This query uses the WHERE clause to filter orders where the order_date year is greater than 2020. 
-- Note how we used the YEAR() function on order_date for this query, as order_date is a DATE type column.

-- Bringing it Together and Next Steps
-- Well done for getting through this new concept. We've just learned what the WHERE clause is, how its syntax works, 
-- and how it helps us customize our data retrieval process. By using the WHERE clause, we were able to retrieve all orders placed after 2020 from the Orders table.


-- Selecting all orders placed after the year 2020
SELECT * FROM Orders
WHERE YEAR(order_date) > 2020;

-- Logical Operators are at the heart of any computational language, SQL being no exception. They're used in the WHERE clause of 
-- SELECT statements (as well as other statements like INSERT, UPDATE, and DELETE which you'll learn about in the future) to combine 
-- or negate conditions and ultimately help us sieve out precise information from our database.

-- Understanding AND and OR Operators in SQL
-- Firstly, we have the AND and OR operators.

-- An AND operator returns TRUE if both listed conditions are true. It essentially narrows your search results because it adds more conditions that records must meet.

-- Meanwhile, an OR operator returns TRUE if either of the conditions listed is true, effectively broadening your search results because it only requires one of the conditions to be met.

-- To see them in action, follow the code examples:


/* Using 'AND' operator */
SELECT * FROM Orders WHERE YEAR(order_date) > 2022 AND order_status = 'Delivered';

/* Using 'OR' operator */
SELECT * FROM OrderItems WHERE extended_support = 1;
-- Now let's analyze the above code snippets:

-- In the first example, we employ the AND operator, which will extract orders from the database (SELECT * FROM Orders) that meet both conditions - 
-- the order was made after 2022 and the order_status is 'Delivered'.

-- In the second snippet, an OR operator is not directly used, but it's implied as we filter the rows in OrderItems table where the extended_support 
-- field is true (1). This is a single-condition filter and doesn't showcase OR directly.

-- Introduction to IN and BETWEEN Operators in SQL
-- Next, we have the IN and BETWEEN operators:

-- The IN operator allows us to specify multiple values in a WHERE clause, a clean, efficient alternative to multiple OR conditions.

-- The BETWEEN operator selects values within a given range, which can be numbers, text, or dates.

-- Now let's use these operators:

/* Using 'IN' operator */
SELECT * FROM Orders WHERE customer_id IN (1, 2);
/* Same query using multiple 'OR' operators */
SELECT * FROM Orders WHERE customer_id = 1 OR customer_id = 2;

/* Using 'BETWEEN' operator */
SELECT * FROM Orders WHERE order_date BETWEEN '2021-01-01' AND '2022-01-01';
/* Excluding boundary values */
SELECT * FROM Orders WHERE order_date > '2021-01-01' AND order_date < '2022-01-01';
-- The first example employs the IN operator to extract orders placed by customers with customer_id 1 or 2.

-- The BETWEEN operator in the third query performs a range-based search, extracting orders with an order date between '2021-01-01' and '2022-01-01', including both dates. If you don’t want the boundary values, refer to the last line where explicit conditions are used to exclude them.

-- Note: Modern SQL engines optimize IN and OR similarly, so there’s no significant difference in execution for small lists. However, for longer lists, IN is preferred for clarity.

-- Conceptualizing the NOT Operator
-- Finally, we have the NOT operator, which is used to exclude records that meet specific conditions. Let's try it out in a SELECT statement:


/* Using 'NOT' operator */
SELECT * FROM Orders WHERE order_date NOT BETWEEN '2021-06-01' AND '2021-12-31';
-- In the snippet above, we use the NOT operator to exclude certain records from our selection. This line extracts orders where the order_date is not in the range from '2021-06-01' to '2021-12-31'.

-- Logical operators, such as AND, OR, IN, NOT IN, and BETWEEN, help us refine our SQL queries to get the data we need in a more efficient and specific way. These tools will allow us to retrieve specific sets of data from our database, which in this case concern online shopping data.

-- TODO: Fetch orders with specific conditions
SELECT * FROM Orders WHERE order_id > 1 AND order_status = 'Delivered';
-- TODO: Fetch orders occurring between '2021-01-01' and '2022-01-01'
SELECT * FROM Orders
WHERE order_date BETWEEN '2021-01-01' AND '2022-01-01';

-- TODO: Fetch orders from year 2021 or 2022, with order IDs between 100 and 400, where the order status was either Delivered or Canceled
SELECT * FROM Orders WHERE YEAR (order_date) IN (2021, 2022) AND order_id BETWEEN 100 AND 400 AND (order_status = "Delivered" OR order_status = "Canceled");


--*****new key SQL keyword — ORDER BY — and discover how we can use this to organize and sort our data.

-- Understanding ORDER BY Clause
-- In SQL, the ORDER BY keyword is used to sort the result set in ascending or descending order. 
-- It's an invaluable tool when seeking insights from data and one that you will use frequently. 
-- The ORDER BY keyword sorts the records in ascending order by default, but descending order can be applied by using DESC after the column name.

-- To illustrate how this works, let's say we have a Products table with columns: product_id, product_name, and product_price. 
-- If we would like to sort our list of products by their names in descending order, we could use the ORDER BY clause like this:


SELECT product_name, product_id 
FROM Products 
ORDER BY product_name DESC;

-- Linking SELECT with ORDER BY
-- Remember our dear friend, the SELECT statement? Well, it's back again. This time, however, we're going to pair it up with the ORDER BY clause. 
-- The general syntax looks like this:

SELECT column_name 
FROM table_name 
ORDER BY column_name ASC|DESC;

-- Interpreting Results
-- Let's break down our SQL query and the output:

-- SELECT product_name, product_id: This part of the command specifies the columns that we want to retrieve from the Products table.
-- FROM Products: Here we are specifying the table that we want to retrieve data from.
-- ORDER BY product_name ASC: The ORDER BY clause sorts the records based on the product name. The ASC part specifies that we want the sorting to be in ascending order. 
-- The ORDER BY keyword sorts the records in ascending order by default, so the ASC keyword is optional here.

-- Functional Dependency and ORDER BY
-- When using the ORDER BY clause, it’s important to understand functional dependency in SQL. A functional dependency exists when one column uniquely 
-- determines another column in a table.

-- If you use ORDER BY on a column that is not unique (e.g., product_name in the Products table), rows with duplicate values in that column might 
-- appear in a random or unpredictable order in the result set.

-- Consider this query:


SELECT product_name, product_price 
FROM Products 
ORDER BY product_name ASC;
-- If multiple products share the same product_name, the SQL engine may return these rows in a different order each time you run the query. 
-- This happens because there’s no explicit instruction on how to handle ties (rows with identical product_name values).

-- To prevent non-deterministic sorting:

-- Add a secondary column to the ORDER BY clause. This ensures a consistent sort order for rows with duplicate values in the primary sort column.
-- Choose a secondary column that uniquely identifies rows, such as a primary key or another distinct attribute.
-- Corrected example:


SELECT product_name, product_price 
FROM Products 
ORDER BY product_name ASC, product_id ASC;
-- In this case::

-- product_name is the primary sort column.
-- product_id is the secondary sort column, ensuring consistent order for rows with the same product_name.
-- Always include a secondary column in ORDER BY when sorting on non-unique columns. This ensures that your query results are deterministic and repeatable.

-- TODO: Select all products
SELECT * FROM products;


-- TODO: Select product name and product ID ordered by product name in descending order
SELECT product_name, product_id
FROM Products
ORDER BY product_name DESC;

-- TODO: Change the sorting of order dates to be from newest to oldest
SELECT order_id, order_date
FROM Orders
ORDER BY order_date DESC;


-- TOOD: Fill in the missing pieces of code based on the task description
SELECT order_id, order_date
FROM Orders
WHERE YEAR (order_date) > 2020 AND YEAR (order_date) < 2023
ORDER BY order_date DESC;

-- TODO: Filter by category using the WHERE clause
SELECT product_name, product_price, category_id
FROM Products
WHERE category_id = 1 
ORDER BY product_price ASC;
