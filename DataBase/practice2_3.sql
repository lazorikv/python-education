/*Task1*/
/*1*/
CREATE TABLE potential_customers(
    id_potential_customers SERIAL,
    email VARCHAR(100),
    name VARCHAR(100),
    surname VARCHAR(100),
    second_name VARCHAR(100),
    city VARCHAR(100)
);

/*2*/
INSERT INTO potential_customers (email, name, surname, second_name, city)
VALUES ('1@gmail.com', 'name1', 'surname1', 'second_name1', 'city 1'),

('2@gmail.com', 'name2', 'surname2', 'second_name2', 'city 2'),

('3@gmail.com', 'name3', 'surname3', 'second_name3', 'city 3'),

('4@gmail.com', 'name4', 'surname4', 'second_name4', 'city 4'),

('5@gmail.com', 'name5', 'surname5', 'second_name5', 'city 5'),

('6@gmail.com', 'name6', 'surname6', 'second_name6', 'city 6'),

('7@gmail.com', 'name7', 'surname7', 'second_name7', 'city 7'),

('8@gmail.com', 'name8', 'surname8', 'second_name8', 'city 8'),

('9@gmail.com', 'name9', 'surname9', 'second_name9', 'city 9'),

('10@gmail.com', 'name10', 'surname10', 'second_name10', 'city 10'),

('11@gmail.com', 'name11', 'surname11', 'second_name11', 'city 11'),

('12@gmail.com', 'name12', 'surname12', 'second_name12', 'city 12'),

('13@gmail.com', 'name13', 'surname13', 'second_name13', 'city 13'),

('14@gmail.com', 'name14', 'surname14', 'second_name14', 'city 14'),

('15@gmail.com', 'name15', 'surname15', 'second_name15', 'city 15');

/*3*/
SELECT first_name, email, city
FROM
	(SELECT email, first_name, middle_name, last_name, city
	FROM users
	UNION
	SELECT email, name, surname, second_name, city
	FROM potential_customers pc) AS all_users
WHERE city = 'city 17';

/*Task2*/
SELECT first_name, email FROM users
ORDER BY city, first_name;

/*Task3*/
SELECT category_title, COUNT(*) FROM categories c
JOIN products p ON p.category_id = c.category_id
GROUP BY category_title
ORDER BY COUNT(*) DESC;

/*TASk4*/
/*4.1*/
SELECT product_title FROM products
EXCEPT
     (SELECT product_title
	FROM products p JOIN cart_product c
	ON p.product_id = c.products_product_id );

/*4.2*/
SELECT product_title
FROM products
EXCEPT
     (SELECT p.product_title FROM products p
		JOIN cart_product cp ON p.product_id = cp.products_product_id
		JOIN carts c ON c.cart_id = cp.carts_cart_id
		JOIN orders o ON o.carts_cart_id = c.cart_id);

/*4.3*/
SELECT p.product_title, COUNT(*) FROM products p
JOIN cart_product cp ON p.product_id = cp.products_product_id
GROUP BY p.product_title
ORDER BY COUNT(*) DESC
LIMIT 10;

/*4.4*/
SELECT p.product_title, COUNT(o.order_id) FROM products p
JOIN cart_product cp ON p.product_id = cp.products_product_id
JOIN carts c ON c.cart_id = cp.carts_cart_id
JOIN orders o ON o.carts_cart_id = c.cart_id
GROUP BY p.product_title
ORDER BY count(o.order_id) DESC
LIMIT 10;

/*4.5*/
SELECT user_id, SUM(o.total) FROM users u
JOIN carts c ON u.user_id = c.cart_id
JOIN orders o ON o.carts_cart_id = c.cart_id
JOIN order_status os ON os.order_status_id = o.order_status_order_status_id
WHERE os.order_status_id IN (1, 2, 3)
GROUP BY user_id
ORDER BY sum(o.total) DESC
LIMIT 5;

/*4.6*/
SELECT user_id, COUNT(o.order_id) FROM users u
JOIN carts c ON u.user_id = c.cart_id
JOIN orders o ON o.carts_cart_id = c.cart_id
GROUP BY user_id;

/*4.7*/
SELECT user_id, SUM(o.total) FROM users u
JOIN carts c ON u.user_id = c.cart_id
JOIN orders o ON o.carts_cart_id = c.cart_id
JOIN order_status os ON os.order_status_id = o.order_status_order_status_id
WHERE os.order_status_id = 4
GROUP BY user_id
ORDER BY SUM(o.total) DESC
LIMIT 5;