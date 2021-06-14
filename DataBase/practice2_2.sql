/*Task 2.1*/
/*1*/
SELECT * FROM users;
/*2*/
SELECT * FROM products;
/*3*/
SELECT * FROM order_status;
/*Task2.2*/
SELECT * FROM orders
WHERE order_status_order_status_id = 4;
/*Task2.3*/
/*1*/
SELECT * FROM products
WHERE price > 80.00 AND price <= 150.00;
/*1 2nd version*/
SELECT * FROM products
WHERE price BETWEEN 80.00 AND 150.00;
/*2*/
SELECT * FROM orders
WHERE created_at > '2020-10-01';
/*3*/
SELECT * FROM orders
WHERE created_at > '2020-01-01' AND created_at < '2020-06-01';
/*3 2nd version*/
SELECT * FROM orders
WHERE created_at BETWEEN '2020-01-01' AND '2020-06-01';
/*4*/
SELECT * FROM products
WHERE category_id IN (7, 11, 18);
/*5*/
SELECT * FROM orders
WHERE order_status_order_status_id IN (1,2,3) AND created_at < '2020-12-31';
/*6*/
SELECT cart_id FROM carts
EXCEPT
SELECT carts_cart_id FROM orders;
/*Task2.3*/
/*1*/
SELECT AVG(total) AS Average_Sum  FROM orders
WHERE order_status_order_status_id = 4;
/*2*/
SELECT MAX(total) AS max_total FROM orders
WHERE created_at BETWEEN '2020-06-01' AND '2020-09-01';