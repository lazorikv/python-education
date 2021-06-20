/*Task2*/

/*clients who made an order and live in the same city*/
explain select o.order_id, o.client_id, i.town
FROM order_car o
join info i
on o.client_id = i.client_id
  where i.town = 'Town 15';
--before indexing Gather  (cost=3312.50..8543.40 rows=6098 width=15)
--after indexing Merge Join  (cost=1826.54..7221.97 rows=6098 width=15)
create index idx_sort on info(town);
create index idx_sort1 on order_car(client_id);
drop index idx_sort;
drop index idx_sort1;

/*information about customers who rented a car for 1, 3 or 6 days between March 1 and May 1*/
explain select order_id, c.client_id, first_name, last_name from client c
join order_car oc on c.client_id = oc.client_id
where date_of_renting between '2021-03-01' and '2021-05-01' and period_of_renting in (3, 6, 1);
--before indexing Hash Join  (cost=5503.05..8203.85 rows=30244 width=31)
--after indexing Hash Join  (cost=3384.53..6085.38 rows=30249 width=31)
create index idx_ident on order_car(date_of_renting);
create index idx_ident1 on order_car(period_of_renting);
drop index idx_ident;
drop index idx_ident1;

/*what cars were rented by client with number 1456*/
explain select c.client_id, car.brand, car.model, car.car_number from client c
 join order_car oc on c.client_id = oc.client_id
left join car on oc.car_number = car.car_number
join info on c.client_id = info.client_id
where info.telephone = 1453;

--before indexing Hash  (cost=2412.75..2412.75 rows=29 width=8)
--after indexing  Hash  (cost=204.34..204.34 rows=29 width=8)
create index idx_1 on info(telephone);
drop index idx_1;