-- use your database inplace of demo
use demo;

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

CREATE TABLE `products` (
	`Product` TEXT(256) NOT NULL,
	`Year` INT,
	`Month` INT,
	`total_sales` FLOAT
);

SELECT * from orders;

SELECT * from products;

DROP table products;

DROP table orders;

describe products;

-- INSERT INTO products values ('any', 2233, 3, 1231.23);

-- 1. The total sales amount for each product in the last quarter (last 3 months)? - s
-- Since the last month was 9 : (september) we can say if the month is greater or equal to 7, we can include in our sum

SELECT Product, CEIL (SUM(total_sales)) AS TotalSales
FROM orders
WHERE ((7) <= Month) 
GROUP BY Product
ORDER BY TotalSales DESC;

-- 2. Top 5 products by total sales amount - c

SELECT Product, CEIL (SUM(total_sales)) AS TotalSales
FROM orders
GROUP BY Product
ORDER BY TotalSales DESC
LIMIT 5;

-- 3. Calculate the monthly average sales for each product over the entire dataset. - s
SELECT Product, CEIL (SUM(total_sales) / (11 + 1)) AS MonthlyAvgSales
FROM orders
GROUP BY Product
ORDER BY MonthlyAvgSales DESC;






