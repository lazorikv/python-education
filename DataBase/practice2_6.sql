create or replace view cheap_product as
    select * from products
where price < 50
with local check option;

drop view cheap_product;


create or replace view inform_view as
    select * from orders
join order_status on order_status_order_status_id = order_status.order_status_id;

drop view cheap_product;

create or replace view view3 as
    select * from products
join categories  using (category_id)
    where in_stock > 9;

drop view view3;


create materialized view heavy_view as
   select subtotal, shipping_total from orders o
    join carts c on c.cart_id = o.carts_cart_id
   cross join users
where order_id = user_id;


drop materialized view total_view;