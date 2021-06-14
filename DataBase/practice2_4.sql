
BEGIN;
UPDATE users
SET first_name = 'VLAD'
WHERE first_name = 'first_name 1';
COMMIT;

BEGIN;
UPDATE categories
SET category_title = 'WATER'
WHERE category_title = 'Category 10';
SELECT category_title FROM categories;
ROLLBACK;

BEGIN;
SAVEPOINT SP1;
UPDATE carts
SET subtotal = 432.5
WHERE users_user_id = 10;
SELECT subtotal FROM carts
    WHERE users_user_id = 10;
ROLLBACK TO SAVEPOINT SP1;


BEGIN;
DELETE FROM orders
    WHERE carts_cart_id = 4;
SELECT * FROM orders;
COMMIT;

BEGIN;
DELETE FROM orders
WHERE order_status_order_status_id = 3;
SELECT * FROM orders;
ROLLBACK;

BEGIN;
SAVEPOINT SP1;
DELETE FROM users
WHERE  last_name = 'last_name 6';
SAVEPOINT SP2;
DELETE FROM categories
    WHERE category_title = 'Category 1';
RELEASE SAVEPOINT SP2;
ROLLBACK TO SAVEPOINT SP1;

BEGIN;
INSERT INTO orders(shipping_total, total)
VALUES (34, 14.5);
SELECT shipping_total, total FROM orders
    WHERE shipping_total = '34';
ROLLBACK;

BEGIN;
INSERT INTO carts(subtotal, total)
VALUES (34, 14.5);
SELECT cart_id, subtotal, total FROM carts
    WHERE subtotal= '34';
COMMIT;

BEGIN;
SAVEPOINT SP3;
INSERT INTO users(email, password)
VALUES ('VLAD_WINNER', '12345');
SELECT user_id, email, password FROM users
    WHERE password= '12345';
ROLLBACK TO SAVEPOINT SP3;


CREATE SEQUENCE code_seq;
ALTER TABLE orders ALTER COLUMN order_id SET DEFAULT nextval('code_seq');
ALTER SEQUENCE code_seq RESTART WITH 1501;

CREATE SEQUENCE code_seq1;
ALTER TABLE carts ALTER COLUMN cart_id SET DEFAULT nextval('code_seq1');
ALTER SEQUENCE code_seq1 RESTART WITH 2001;


CREATE SEQUENCE code_seq2;
ALTER TABLE users ALTER COLUMN user_id SET DEFAULT nextval('code_seq2');
ALTER SEQUENCE code_seq2 RESTART WITH 3001;