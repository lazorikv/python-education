explain select * from products
cross join cart_product
where product_title = '%5';

CREATE unique index ind_1 ON products using btree(product_title);
DROP INDEX ind_1;


explain select * from orders
cross join order_status
where  orders.order_status_order_status_id = 3;

create index ind_2 on orders(order_status_order_status_id);
drop index ind_2;


explain select * from cart_product
WHERE products_product_id = 4;

CREATE INDEX ind_3 ON cart_product(products_product_id);
drop index ind_3;
