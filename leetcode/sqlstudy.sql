/*
Author: Sarah Kam
Description: Exercises from Sql Essential Training course on LinkedIn:
  https://www.linkedin.com/learning/sql-essential-training-20685933
*/

--This is a comment

/*
Author: Sarah Kam
Date: 03/24/2024

SELECT, FROM, AS, ORDER BY (ASC, DESC), LIMIT

Use Customer table: FirstName, LastName, Email are all in there
Browse table to confirm that information is what we want

After running a query, at bottom we can see total row count = 60, how long it took, etc

SELECT 
	FirstName AS [Customer First Name],	-- writes the column name more human-readable; "alias"
	LastName AS "Customer Last Name", -- both [] and "" work for aliasing
	Email AS EMAIL -- if just 1 word, no [] or "" needed
FROM 	-- keyword: what table are we getting info from
	Customer 	-- not CustomerId, which is a field; we want a table
ORDER BY
	--LastName ASC: sort by alphabetical last name; ascending (A-Z) default, or keyword ASC/DESC specific
	FirstName ASC,
	LastName DESC -- sorts by first names asc first, then within same first names, sorts by last name desc
LIMIT 10 -- only displays top 10 records after previous query code is run	
*/


/*
Date: 03/25/2024

WHERE, BETWEEN, IN, AND, strings in comparisons; LIKE, % operator; DATE, OR;
if/then logic with CASE, WHEN/THEN, ELSE, END (AS)

SELECT
	InvoiceDate,
	BillingCity,
	BillingAddress,
	Total
FROM
	Invoice

WHERE  -- conditional statement!
	--Total=1.98		 --where total price spent equals 1.98; 111 rows
	--Total BETWEEN 1.98 AND 5.00		 --where the price is between 1.98 and 5.00; 178 rows
	--Total IN (1.98, 3.96) 		-- where the price is exactly 1.98 or 3.96; 168 rows
	--BillingCity = "Brussels" 		-- where the BillingCity = Brussels; str data needs ""; 7 rows
	BillingCity IN ("Brussels", "Orlando", "Paris") 		-- 28 rows

-- % symbol is wild card!

	--BillingCity LIKE "B%" -- all cities starting with B and wildcard after; 62 rows
	BillingCity LIKE "%B%" -- all cities with a B anywhere in it, case insensitive; 83 rows!

	-- DATE funct only uses InvoiceDate dates (datetime obj);
	-- match "YYYY-MM-DD" exactly to the way the data is stored
	-- DATE(InvoiceDate) > "2010-05-22" AND Total < 3 -- AND operator: multiple conditions for WHERE; 124 rows
	BillingCity LIKE "P%" OR BillingCity LIKE "D%" -- billing city starts with "P" OR "D"; 56 rows


IF THEN logic with CASE

-- if then / else statements: CASE, WHEN/THEN, ELSE, END (AS)
-- no commas between the WHEN lines!

SELECT 
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total,
	CASE
		WHEN Total < 2.00 THEN "Baseline Purchase"
		WHEN Total BETWEEN 2.00 AND 6.99 THEN "Low Purchase"
		WHEN Total BETWEEN 7.00 AND 15.00 THEN "Target Purchase"
		ELSE "Top Performer"
	END AS "Purchase Type" -- names the field we just created using this if/then
FROM
	Invoice
*/


/*
Date: 03/26/2024

JOIN

Invoice has InvoiceID and CustomerID - CustomerID can join with Customer;
SupportRepID in CustomerID links with EmployeeID
Invoice.CustomerID is a "foreign key" - primary key of Invoice is InvoiceID

SYMBOL * means all (e.g. SELECT * = select all columns)

discrepancies between tables are handled w/ different kinds of joins
if customer deletes their acc, financial records must still be kept, but might be missing from customer table

 */
	
SELECT 		-- select certain cols from each table
	c.LastName, c.FirstName, i.InvoiceId , i.CustomerId , i.InvoiceDate , i.total
FROM 
	Invoice AS i
INNER JOIN
	Customer AS c 		-- the two tables we're joining: Invoice, Customer
ON		-- declare what keys we're using to join
	i.CustomerId = c.CustomerId		-- tablename.columnname to pull specific column
ORDER BY c.CustomerId		-- some customers have multiple invoices!


