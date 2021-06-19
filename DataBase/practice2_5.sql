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

explain select * from orders o
join carts c on o.carts_cart_id = c.cart_id
join order_status os on os.order_status_id = o.order_status_order_status_id
join cart_product cp on o.carts_cart_id = cp.carts_cart_id
where o.total = 336.33;

create index idx_ord on orders(total);
create index idx_ord1 on cart_product(carts_cart_id);