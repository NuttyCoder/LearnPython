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


-- TODO: Write an SQL query to select product name, product price, and category ID for specific categories, ordered by price in ascending order
SELECT product_name, product_price, category_id
FROM products
WHERE category_id IN (1,2,3)
ORDER BY product_price ASC;

-- SQL JOINs, linking tables together in complex but meaningful ways, much like a skilled craftsman intricately assembles different parts into a cohesive masterpiece.

-- Our tool of choice for this course is MySQL, a standard in database management systems. 
-- However, if you plan to use a different SQL-based system, rest assured — the concept of JOINs is universal across all platforms.

-- Brief Dataset Description
-- Let’s get acquainted with our dataset, inspired by the dynamics of an online shopping platform, which contains five primary tables. 
-- Below are some sample rows to give you an idea about the structure starting from the simplest table:

-- Categories Table

category_id	category_name
1	Flashcards
2	Worksheets
3	Guides
4	Podcasts
5	Courses
-- This table lists the five product categories available on the platform.

-- Customers Table

customer_id	customer_name
1	John Doe
2	Jane Smith
-- This table provides details about the customers using the platform.

-- Products Table

product_id	product_name	product_price	category_id
1	Vocabulary Flashcards	9.34	1
2	Math Problems Flashcards	12.84	1
-- The Products table contains detailed information about the products offered, including names, prices, and categories.

-- Orders Table

order_id	customer_id	order_date	order_status
1	41	2021-08-17	Delivered
2	16	2022-04-03	Processed
-- This table displays the orders made on the platform, along with their status and associated customers.

-- OrderItems Table:

order_item_id	order_id	product_id	extended_support
1	1	25	0
2	2	12	0
-- The OrderItems table includes information about each item in an order, such as the order it belongs to, the product, and whether it has support.

-- What are SQL JOINs?
-- SQL JOINs are techniques to combine data from two or more tables based on a shared column between them. 
-- They help in extracting valuable information that might be distributed across multiple tables. 
-- Several types of JOINs provide flexibility in how we choose to connect and derive insights from this data.

-- Mastering JOIN Relationships
-- When performing a JOIN between two tables, it’s essential to understand the relationship between the columns involved. 
-- Functional dependencies arise when one column in a table uniquely determines another column. If these dependencies are not considered, 
-- it can lead to incorrect data interpretation or unnecessary duplication in the result set. We must ensure that the columns used in the 
-- ON clause of the JOIN define a clear relationship between the tables. In the Products table, category_id uniquely determines the 
-- category_name from the Categories table. A JOIN between these tables should respect this dependency to avoid redundant or conflicting data.

-- Without a valid ON condition, a JOIN can result in a Cartesian product, where every row from one table is paired with every row from another table. 
-- This can lead to an exponential increase in the result set size. For instance:


SELECT * FROM Customers, Orders;
-- This query retrieves all possible combinations of rows from Customers and Orders, potentially resulting in millions of rows for large tables. 
-- Proper use of the ON condition helps prevent such excessive results by ensuring meaningful connections between tables.

-- INNER JOIN
-- Before we deep-dive into the world of SQL JOINs, it's crucial to understand the variety of joins available. 
-- Each type serves a unique purpose, allowing us to adjust our queries to retrieve the exact data we need.

-- An INNER JOIN, often referred to as just JOIN, is the most common type. It fetches records with matching values in both participating tables. 
-- Unmatched rows are not included in the result. By default, an INNER JOIN is assumed if no specific type of JOIN is mentioned.

-- Example:


SELECT Orders.order_id, Orders.order_date, Orders.order_status, Customers.customer_name AS Customer
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Orders.order_status = 'Canceled'
ORDER BY Orders.order_date DESC;
-- In this example, we use INNER JOIN to combine the Orders and Customers tables. 
-- The query retrieves the order ID, date, and customer name for orders that have been canceled, ordered by the date of the order in descending order.

-- LEFT, RIGHT, and FULL JOIN
-- A LEFT JOIN (also known as LEFT OUTER JOIN) provides all records from the left table and the matched records from the right table. 
-- If there's no match, the result set will include NULL values for the right table's columns. This JOIN is advantageous when you want 
-- to include all records of one table (the left one) regardless of matching rows in the other table.

-- Alternatively, a RIGHT JOIN (or RIGHT OUTER JOIN) offers all records from the right table and the matched records from the left table. 
-- If there's no match, the result set will include NULL values for unmatched left table's columns.

-- A FULL JOIN (or FULL OUTER JOIN) yields all records when a match exists in either of the participating tables. 
-- It combines the effects of both LEFT JOIN and RIGHT JOIN. If there's no match, the result set will have NULL values for every 
-- column of the table lacking a matching row. FULL JOIN is not directly supported in MySQL but can be emulated with a combination 
-- of LEFT JOIN, RIGHT JOIN, and UNION, which we'll explore later in this course.

-- Wrapping Up and Looking Ahead
-- As we conclude this introductory module on SQL JOINs, think of yourself as an artisan learning a new craft. 
-- Remember, understanding SQL JOINs theoretically sets the stage, but applying them hands-on is the real key to mastery.

-- Moving forward, we'll begin by delving into each table — Categories, Customers, Products, Orders, and OrderItems — individually. 
-- This approach will not only familiarize you with the data but also build a solid foundation for when we start interlinking these tables using JOINs. 
-- From simple data retrieval to intricate queries, you'll learn to weave the story of an online shopping platform using SQL.


Example : 1

SELECT Orders.order_id, Orders.order_date, Orders.order_status, Customers.customer_name AS Customer
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Orders.order_status = 'Canceled'
ORDER BY Orders.order_date DESC;

Example : 2 -- Cange Example 1 to finding all delivered orders:
SELECT Orders.order_id, Orders.order_date, Orders.order_status, Customers.customer_name AS Customer
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Orders.order_status = 'Delivered'
ORDER BY Orders.order_date DESC;


Example 3:
SELECT Orders.order_id, Orders.order_date, Orders.order_status, Customers.customer_name AS Customer
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Orders.order_status = 'Canceled'
ORDER BY Orders.order_date DESC;

-- Exploring INNER JOIN
-- In this session, we'll focus on the INNER JOIN. Essentially, the INNER JOIN in SQL is a clause that merges rows from two tables based on a shared column between them. The result is a dataset that includes only the rows that satisfy the joining condition.

-- Before diving into examples, let's review the standard syntax for executing an INNER JOIN:

SELECT column1, column2, ...
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
-- This syntax serves as the foundation of our queries whenever we desire to merge data from two related tables. 
-- In this lesson, we'll see how this structure is practically used to join Products and OrderItems tables.

-- By the end of this lesson, you'll be adept at retrieving data from the OrderItems and Products tables using INNER JOIN. 
-- The key product_id will serve as the common link between these tables.

-- INNER JOIN in Action

-- Suppose we have an OrderItems table showcasing the extended_support option for orders. This can be linked to the Products table, where we want to retrieve product details. We can use an INNER JOIN to unify these two tables:

SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
INNER JOIN OrderItems
ON Products.product_id = OrderItems.product_id;

-- Sneak peek of the output:
-- | product_name                   | product_price | extended_support |
-- |--------------------------------|---------------|------------------|
-- | Critical Thinking Guide        |         16.15 |                0 |
-- | Grammar Exercises Worksheets   |         10.70 |                0 |

-- In this SQL statement:

-- SELECT Products.product_name, Products.product_price, OrderItems.extended_support specifies the data we want — product_name and product_price from the 
-- Products table and extended_support from the OrderItems table.
-- FROM Products indicates the primary table from which we start our query.
-- INNER JOIN OrderItems indicates that we wish to connect the Products table with the OrderItems table.
-- ON Products.product_id = OrderItems.product_id is the key condition that joins these tables. It ensures that the join happens through the product_id column, 
-- common to both tables. This condition aligns the rows from Products and OrderItems accurately.
-- Executing this INNER JOIN query on the Products and OrderItems tables generates a comprehensive list that associates each product with its respective 
-- ordering details, showcasing the utility of INNER JOIN to proficiently merge related data from two tables.

-- Note: If a product is ordered multiple times, the INNER JOIN will duplicate the product details for each matching row in the OrderItems table.
-- For example, when retrieving product names and details, you might see the same product listed multiple times if it appears in several order 
-- entries with different support options. To handle this, you can use aggregation with GROUP BY to summarize the data and eliminate duplicates, 
-- grouping the results by product and providing a count of the order items. This allows for an effective summary of the data without repetition.

-- Handling NULL Values in INNER JOIN
-- The INNER JOIN only includes rows where the join condition is satisfied. If a row in one table has a NULL value in the join column, 
-- it will not appear in the result set. For instance, if a product_id in the OrderItems table is NULL, that row will not match any row in the 
-- Products table and will be excluded from the results.

-- To find rows with NULL values that are excluded by the INNER JOIN, you can use a LEFT JOIN and filter for NULL in the right table’s column:


SELECT OrderItems.order_item_id, OrderItems.product_id
FROM OrderItems
LEFT JOIN Products ON OrderItems.product_id = Products.product_id
WHERE Products.product_id IS NULL;
-- This query retrieves OrderItems that do not have a matching product_id in the Products table.

-- Reversing the Order
-- Let's refine our example by arranging all products along with their order support status in descending order of product price. Here's how the query is structured:

--  To solve this, we can use aggregation (GROUP BY) to summarize data and eliminate duplicates:

--  This approach leverages GROUP BY to group the results by product-wise, providing a count of the order items, thereby summarizing the data effectively.


SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
INNER JOIN OrderItems
ON Products.product_id = OrderItems.product_id
ORDER BY Products.product_price DESC;

-- Example output:
-- | product_name                   | product_price | extended_support |
-- |--------------------------------|---------------|------------------|
-- | Project Management Course      |        149.26 |                0 |
-- | Project Management Course      |        149.26 |                0 |
-- In this scenario, the ORDER BY Products.product_price DESC condition arranges the results in descending order by product price.


SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
INNER JOIN OrderItems
ON Products.product_id = OrderItems.product_id
WHERE OrderItems.extended_support = 1
ORDER BY Products.product_price DESC;

+--------------------------------+---------------+------------------+
| product_name                   | product_price | extended_support |
+--------------------------------+---------------+------------------+
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Graphic Design Course          |         52.96 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Business Trends Podcast        |         30.02 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Vocabulary Practice Worksheets |         18.45 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
| Chemistry Elements Flashcards  |          5.43 |                1 |
+--------------------------------+---------------+------------------+

SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
INNER JOIN OrderItems ON Products.product_id = OrderItems.product_id
WHERE Products.product_name IN ("Graphic Design Course", "Business Trends Podcast")

SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
INNER JOIN OrderItems ON Products.product_id = OrderItems.product_id
-- TODO: Filter products that have extended warranty and have a 'category_id' 2 ('Worksheets')
WHERE OrderItems.extended_support = 1 AND Products.category_id = 2
ORDER BY Products.product_price DESC;

ORDER BY Products.product_price DESC


-- TODO: Select product name, product price, and extended support for products in the Worksheets category.
-- TODO: Join Products table with OrderItems table on product_id.
-- TODO: Filter results to extended support equals 1 and limit to Worksheets (2nd) category.
-- TODO: Order the results by the product price in descending order.
SELECT Products.product_name, Products.product_price, OrderItems.extended_Support
FROM Products
INNER JOIN OrderItems ON Products.product_id = OrderItems.product_id
WHERE OrderItems.extended_support = 1 and Products.category_id = 2
ORDER BY Products.product_price DESC;

-- Recap of SQL Joins
-- Before we start, keep in mind that SQL JOINs allow us to combine data from two or more tables based on a related column. 
-- Previously, we've worked with INNER JOIN, which selects rows that have matching values in both tables. 
-- In this lesson, we'll explore how LEFT JOIN and RIGHT JOIN can help us manipulate our data further.

-- Sample Tables Overview
-- To understand these JOIN types better, consider two simple tables: Orders and OrderItems.

Orders Table:

order_id	customer_id	order_date	order_status
1	41	2021-08-17	Delivered
2	16	2022-04-03	Processed
-- The Orders table provides detailed information about each order, including the order_id, date, status, and the customer who placed the order. This is useful for tracking order specifics.

OrderItems Table:

order_item_id	order_id	product_id	extended_support
1	1	25	0
2	2	12	0
-- The OrderItems table connects each order to the specific items within it using corresponding order_id values.

-- INNER JOIN Explained
-- INNER JOIN returns rows when there's a match in both tables. If there's no match, those rows are not included in the output.

Example:

SELECT Orders.order_date, Orders.order_status, OrderItems.product_id
FROM Orders
INNER JOIN OrderItems ON Orders.order_id = OrderItems.order_id;

-- Sneak peek of the output:
-- | order_date | order_status | product_id |
-- |------------|--------------|------------|
-- | 2021-08-17 | Delivered    | 25         |
-- | 2022-04-03 | Processed    | 12         |

-- Understanding the LEFT JOIN
-- LEFT JOIN includes all rows from the left table, along with any matches from the right table. If there's no match, the output displays NULL for the right table's columns.

Example:


SELECT Orders.order_date, Orders.order_status, OrderItems.product_id
FROM Orders
LEFT JOIN OrderItems ON Orders.order_id = OrderItems.order_id;

-- Sneak peek of the output:
-- | order_date | order_status | product_id |
-- |------------|--------------|------------|
-- | 2021-08-17 | Delivered    | 25         |
-- | 2022-04-03 | Processed    | 12         |

-- Diving into the RIGHT JOIN
-- RIGHT JOIN ensures that every row from the right table is included in the output, with matched rows from the left table.

Example:

SELECT Orders.order_date, Orders.order_status, OrderItems.product_id
FROM Orders
RIGHT JOIN OrderItems ON Orders.order_id = OrderItems.order_id;

-- Sneak peek of the output:
-- | order_date | order_status | product_id |
-- |------------|--------------|------------|
-- | 2021-08-17 | Delivered    | 25         |
-- | 2022-04-03 | Processed    | 12         |


-- Note: With the provided sample tables, there currently seems to be no visible difference due to the limited number of rows and the 
-- fact that each order has a corresponding order item. However, generally, there is a difference: RIGHT JOIN includes all rows from 
-- the right table (OrderItems) and any corresponding rows from the left table (Orders). It's advisable to try this on tables with 
-- more rows and different cases where some rows in the right table do not have corresponding rows in the left table to see the full effect.


--Understanding Differences Between LEFT JOIN and RIGHT JOIN
-- To better highlight the distinctions between LEFT JOIN and RIGHT JOIN, let's expand the sample tables:

-- Orders Table:

order_id	customer_id	order_date	order_status
1	41	2021-08-17	Delivered
2	16	2022-04-03	Processed
3	12	NULL	Canceled
OrderItems Table:

order_item_id	order_id	product_id	extended_support
1	1	25	0
2	2	12	0
3	4	18	1
LEFT JOIN Example:
  
SELECT Orders.order_id, Orders.order_date, OrderItems.product_id
FROM Orders
LEFT JOIN OrderItems ON Orders.order_id = OrderItems.order_id;

-- Result:
-- | order_id | order_date | product_id |
-- |----------|------------|------------|
-- | 1        | 2021-08-17 | 25         |
-- | 2        | 2022-04-03 | 12         |
-- | 3        | NULL       | NULL       |
RIGHT JOIN Example:

SELECT Orders.order_id, Orders.order_date, OrderItems.product_id
FROM Orders
RIGHT JOIN OrderItems ON Orders.order_id = OrderItems.order_id;

-- Result:
-- | order_id | order_date | product_id |
-- |----------|------------|------------|
-- | 1        | 2021-08-17 | 25         |
-- | 2        | 2022-04-03 | 12         |
-- | NULL     | NULL       | 18         |

--Key Difference:

LEFT JOIN includes all rows from Orders, showing NULL for OrderItems columns when there’s no match.
RIGHT JOIN includes all rows from OrderItems, showing NULL for Orders columns when there’s no match.


-- Select order date, order status, and product ID from the Orders and OrderItems tables respectively
-- Execute a left join on both tables using `order_id` as the joining key
SELECT Orders.order_date, Orders.order_status, OrderItems.product_id
FROM Orders
LEFT JOIN OrderItems ON Orders.order_id = OrderItems.order_id;


-- Select Order date, Order status and Product ID from the Orders and OrderItems tables respectively
-- Undertake a right join on both tables based on order_id
SELECT Orders.order_date, Orders.order_status, OrderItems.product_id
FROM Orders
RIGHT JOIN OrderItems ON Orders.order_id = OrderItems.order_id;

-- TODO: Select order date and order status from the Orders table and product_id from OrderItems
-- TODO: Undertake a right join on both tables based on order_id
SELECT Orders.order_date, Orders.order_status, OrderItems.product_id
FROM Orders
RIGHT JOIN OrderItems ON Orders.order_id = OrderItems.order_id;

-- Select order date, order status from Orders and product_id from OrderItems
-- Undertake a left join on both tables based on order_id
SELECT Orders.order_date, Orders.order_status, OrderItems.product_id
FROM Orders
LEFT JOIN OrderItems ON Orders.order_id = OrderItems.order_id


-- Select Product name, Product price, and Extended Support status from the Products and OrderItems tables respectively
-- Undertake a left join on both tables based on product_id
SELECT Products.product_name, Products.product_price, OrderItems.extended_support 
FROM Products 
LEFT JOIN OrderItems ON OrderItems.product_id = Products.product_id


-- SQL JOINs are essential when it comes to processing data, and having a command over FULL JOINs can help you effectively analyze intricate data relations. 
-- For this lesson, we will be continuing with MySQL, but remember, the understanding of SQL you garner here is transferable to other relational database 
-- management systems (RDBMS) such as PostgreSQL, SQL Server, and SQLite, with just slight differences in their syntax.

-- Traversing Through JOINs and Understanding FULL JOIN
-- Before we plunge into FULL JOIN, let's reinforce our knowledge of JOINs. SQL JOINs enable us to merge rows from two or more tables based on a common  
-- column among them. An INNER JOIN returns rows where there is a match in both tables. A LEFT JOIN gives all records from the left table and the matched 
-- records from the right one. A RIGHT JOIN, conversely, returns all records from the right table and the matched records from the left one.

-- FULL JOIN in SQL straddles the territory between LEFT JOIN and RIGHT JOIN. It provides all records where there is a match in either the left table or the right one, 
-- essentially unifying the results of LEFT JOIN and RIGHT JOIN to offer a comprehensive view of your data.

-- This simple visual aid below can help make sense of it, where A and B are the tables we are joining and the green areas depict the results of different JOINs.

-- Practical Implementation Of SQL FULL JOIN in MySQL
-- Let's put our concepts into practice using FULL JOIN to merge relevant data from Products and OrderItems:


-- First part: Fetch all products, product prices, and their associated supports from order items
SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
LEFT JOIN OrderItems ON Products.product_id = OrderItems.product_id

UNION ALL

-- Second part: Retrieve order items with no matching products, ensuring we aren't omitting any data
SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
RIGHT JOIN OrderItems ON Products.product_id = OrderItems.product_id
WHERE Products.product_id IS NULL;

-- Sneak peek of the output:
-- | product_name                     | product_price | extended_support |
-- |----------------------------------|---------------|------------------|
-- | Vocabulary Flashcards            |          9.34 |                0 |
-- | Vocabulary Flashcards            |          9.34 |                0 |
-- In this query, we adopt a bifurcated strategy. The first section applies a LEFT JOIN to list all products, product prices, along with their corresponding support 
-- selection from order items. The latter section, which is essential for simulating a FULL JOIN, uses a RIGHT JOIN to cover those rows from the OrderItems table 
-- that fail to find a match in the Products table (we ensure this by checking WHERE Products.product_id IS NULL).

-- By joining these two parts through UNION ALL, we effectively simulate a FULL JOIN, yielding a complete view that includes all matched and unmatched records 
-- from both tables.

-- Note: In our scenario, no order items are linked to non-existent products, so the LEFT JOIN captures everything. However, in more complex scenarios where 
-- mismatches exist, this method of combining LEFT JOIN and RIGHT JOIN is necessary to simulate a FULL JOIN.

-- Managing NULL Values in FULL JOIN Operations
-- In the query we've just dissected, the condition WHERE Products.product_id IS NULL in the second select statement plays a crucial role. 
-- This ensures that only those records from the OrderItems table are added that are not in the Products table. By handling NULL values in this way, 
-- we ensure that our dataset is complete, which is extremely valuable for data analysts who want to cover all possible angles in their exploration.
-- TODO: Retrieve all products, product prices and their corresponding extended support from order items
SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
RIGHT JOIN OrderItems ON Products.product_id = OrderItems.product_id;


-- TODO: Fetch product name, product price, and extended support from Products and OrderItems tables
SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products 
LEFT JOIN OrderItems ON Products.product_id = OrderItems.product_id

UNION ALL

SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products 
RIGHT JOIN OrderItems ON Products.product_id = OrderItems.product_id
WHERE Products.product_id IS NULL;


-- Fetch all products, their prices, and associated support status using FULL JOIN equivalent
SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
LEFT JOIN OrderItems ON Products.product_id = OrderItems.product_id

UNION ALL

-- Retrieve order items with no matching products (Hint: User RIGHT JOIN and filter NULL product_ids with WHERE)
SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM OrderItems
RIGHT JOIN Products ON Products.product_id = OrderItems.product_id
WHERE Products.product_id IS NULL;

-- TODO 1: Extract all products, product prices, and their associated supports using a LEFT JOIN to obtain all records from the Products table whether there's an associated record in the OrderItems table or not.

-- TODO 2: Retrieve order items with no matching products. Implement a RIGHT JOIN to obtain all records from the OrderItems table whether there's an associated record in the Products table or not. Ensure you include only records where Products.product_id is NULL.

-- TODO 3: Apply the UNION ALL clause to merge the findings of your previous tasks, ensuring a complete dataset that encompasses both associated and non-associated records from both tables.

SELECT Products.product_name, Products.product_price, OrderItems.extended_support
From Products
LEFT JOIN  OrderItems on Products.product_id = OrderItems.product_id
UNION ALL
SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
RIGHT JOIN OrderItems ON  Products.product_id = OrderItems.product_id
WHERE Products.product_id IS NULL; 

-- TODO: Add to the query filtering specifically for products in the category "Flashcards" (category_id = 1)
SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
LEFT JOIN OrderItems ON Products.product_id = OrderItems.product_id

UNION ALL

SELECT Products.product_name, Products.product_price, OrderItems.extended_support
FROM Products
RIGHT JOIN OrderItems ON Products.product_id = OrderItems.product_id
WHERE Products.product_id IS NULL AND Products.category_id = 1;


Understand what the COUNT function does.
Learn the basic syntax of the COUNT function.
See an example of counting rows in a table.
Apply the COUNT function in a real-world context, using online shopping analytics as an example.
By the end of this lesson, you will be able to use the COUNT function to obtain quantitative insights from a dataset


--Understand the count function
--learn the basic syntax of the count function

--Dataset Introduction
--In case you haven't done any of our other courses using this dataset, here is a quick overview for you. 
  -- Below are some sample rows to give you an idea of the structure starting from the simplest table:

Categories Table

category_id	category_name
1	Flashcards
2	Worksheets
3	Guides
4	Podcasts
5	Courses
--This table lists the five product categories available on the platform.

--Customers Table

customer_id	customer_name
1	John Doe
2	Jane Smith
--This table provides details about the customers using the platform.

--Products Table:

product_id	product_name	product_price	category_id
1	Vocabulary Flashcards	9.34	1
2	Math Problems Flashcards	12.84	1
--The Products table lists products available in the online store.

--Orders Table:

order_id	customer_id	order_date	order_status
1	41	2021-08-17	Delivered
2	16	2022-04-03	Processed
--The Orders table contains details of customer orders, including the order date and status.

--OrderItems Table:

order_item_id	order_id	product_id	extended_support
1	1	25	0
2	2	12	0
--The OrderItems table includes information about each item in an order, such as the order it belongs to, the product, and whether 

  it has support.
-- Introduction to COUNT Function
-- The COUNT function in SQL is used to return the number of rows that match a specified condition. 
-- It can also be used without any condition to count all rows in a table. It is a simple yet powerful tool for performing 
--quantitative analysis on data.

--Common Use Cases
--The COUNT function is commonly used in the following scenarios:

--Counting the total number of rows in a table.
--Counting the number of unique entries.
--Counting the number of entries that satisfy a particular condition.
--Understanding how to use the COUNT function helps you derive quick summary statistics from your data, 
  --making it essential for tasks ranging from basic reporting to complex data analysis.

  
  -- Basic Syntax of the COUNT Function
-- The basic syntax of the COUNT function in SQL is as follows:


SELECT COUNT(column_name) FROM table_name WHERE condition;
-- Let's break this down:

SELECT: The command used to retrieve data from the database.
COUNT(column_name): The COUNT function, which takes a column name as an argument.
FROM table_name: Specifies the table from which to retrieve the data.
WHERE condition: An optional clause to filter the rows counted.
For example, if you want to count all rows in a table without any condition, you can use the * symbol:


SELECT COUNT(*) FROM table_name;
Difference Between COUNT(*) and COUNT(column_name):

COUNT(*): Counts all rows in the table, including rows with NULL values in any column.
COUNT(column_name): Counts only non-NULL values in the specified column.

  
-- Example: Counting Total Rows in a Table
-- Let's walk through an example to demonstrate how to count the total number of rows in a table. \
  -- Recall the table named Orders that stores information about customer orders.

-- To count the total number of rows in the Orders table, we use the following SQL query:

SELECT COUNT(*) FROM Orders;

-- Output:
-- COUNT(*)
-- ---------
-- 600
-- Explanation:

SELECT COUNT(*): This command tells the database to count all rows.
FROM Orders: This specifies the table from which to count the rows.
In this example, the COUNT function returns 600, which is the total number of rows in the Orders table. 

--Real-world Application: Online Shopping Analytics
-- Counting rows in a table is not just a theoretical exercise; it has practical applications in real-world scenarios. 
  -- For instance, in online shopping analytics, you might want to count how many orders have a specific status like "Processed" or "Delivered."

-- Imagine a dataset that includes information about various orders and their statuses. Here, the COUNT function can help you quickly determine 
  -- meaningful statistics related to order processing or customer interactions.

-- For example, if we wanted to count the number of orders that have been processed, we would use the following query:


SELECT COUNT(*) FROM Orders WHERE order_status = 'Processed';

-- Output:
-- COUNT(*)
-- ---------
-- 156
-- This query would count the total number of rows in the Orders table where the order_status is 'Processed'.


SELECT COUNT(*) FROM Orders;


-- TODO: Count the number of orders that have the status Processed
SELECT COUNT(*) FROM Orders WHERE order_status = 'Processed';

-- TODO: Calculate the number of orders placed after the year 2021
SELECT COUNT(*) FROM Orders WHERE YEAR(order_date) > 2021 ;

-- TODO: Write the SQL query to count all orders for customer_id 1

SELECT COUNT(*) AS OrderCount
FROM orders
WHERE customer_id = 1

--The Need for DISTINCT in Our Database
-- Given the diverse range of products in online shopping, utilizing DISTINCT is quite handy. We can use it to identify unique categories, 
  -- and much more. It will broaden our understanding of the products data.

-- Let's first learn the format of a basic SQL query that uses DISTINCT.

SELECT DISTINCT column_name FROM table_name;
--It is time to apply this format to our online shopping dataset. Consider the following statement:

SELECT DISTINCT category_id FROM Products;

-- Output:
--  category_id
-- ------------
--           1
--           2
--           3
--           4
--           5
-- This query will fetch all the distinct or unique category_id from the Products table. We use DISTINCT to avoid getting repeated category IDs in the output.

-- More Applications of DISTINCT
-- Let's look at a few more examples using the DISTINCT keyword.

-- What if we want to know all the unique products that have been ordered from our online shop? Simple, we would run:

SELECT DISTINCT product_id FROM OrderItems;

-- Sneak peek of the output:
--  product_id
-- ------------
--           1
--           6
--           7
--          10

  -- The DISTINCT keyword can be applied to multiple columns to find unique combinations of values. For example, let's suppose you want to find all unique combinations of customer_id and order_status in the Orders table:


SELECT DISTINCT customer_id, order_status 
FROM Orders;

-- Sneak peek of the output:
-- | customer_id | order_status |
-- |-------------|--------------|
-- |          41 | Delivered    |
-- |          16 | Processed    |
-- |          44 | Refunded     |
-- |           6 | Processed    |

-- This query returns unique pairs of customer_id and order_status. Rows with identical customer_id values but different order_status values will be treated as distinct.

-- When using DISTINCT, it's important to remember that fetching unique values from large datasets can be time-consuming and slow down your queries. 
-- Therefore, always consider the performance implications and use DISTINCT only when necessary.

-- TODO: Select all distinct category IDs from Products
SELECT DISTINCT category_id
FROM Products;

