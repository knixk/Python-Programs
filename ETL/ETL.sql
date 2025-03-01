-- use your database inplace of demo
use demo;

-- Schema for orders table
CREATE TABLE `orders` (
	`Order ID` INT NOT NULL PRIMARY KEY,
    `Product` TEXT(256) NOT NULL,
    `Quantity Ordered` INT NOT NULL,
    `Price Each` FLOAT NOT NULL,
    `Order Date` DATETIME NOT NULL,
    `Purchase Address` TEXT NOT NULL,
    `total_sales` FLOAT,
    `Month` INT,
    `Year` INT
);

-- Schema for products table
CREATE TABLE `products` (
	`Product` TEXT(256) NOT NULL,
	`Year` INT,
	`Month` INT,
	`total_sales` FLOAT
);

-- After running the python script..
describe products;
describe orders;

SELECT * from orders;
SELECT * from products;

-- Don't drop tables, just for testing
-- DROP table products;
-- DROP table orders;


-- INSERT query example: INSERT INTO products values ('iPhone', 2019, 3, 1231.23);
-- INSERT query example: INSERT INTO orders values (174345, 'iPhone', 2, 11.95, '2019-04-19 08:46:00', '917 1st St, Dallas, TX 75001', 23.9, 4, 2019);

-- ------- x ------- x -------- x -------- x ----------- x ----------- x -----------------

-- 1. The total sales amount for each product in the last quarter (last 3 months).
-- explaination: Since the last month was 9 : (september) we can say if the month is greater or equal to 7, we can include in our sum

SELECT Product, CEIL (SUM(total_sales)) AS TotalSales
FROM orders
WHERE ((9 - 2) <= Month) 
GROUP BY Product
ORDER BY TotalSales DESC;


-- 2. Top 5 products by total sales amount 

SELECT Product, CEIL (SUM(total_sales)) AS TotalSales
FROM orders
GROUP BY Product
ORDER BY TotalSales DESC
LIMIT 5;

-- 3. Calculate the monthly average sales for each product over the entire dataset. 

SELECT Product, CEIL (SUM(total_sales) / (11 + 1)) AS MonthlyAvgSales
FROM orders
GROUP BY Product
ORDER BY MonthlyAvgSales DESC;





