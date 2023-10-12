-- use your database inplace of demo
use demo;

-- creating two tables, orders and products
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

describe orders;


-- INSERT INTO products values ('any', 2233, 3, 1231.23);

 














