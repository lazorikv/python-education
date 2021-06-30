/*Task 3*/

create or replace view clients_from_Town6 as
    select client.client_id, first_name, last_name, i.town, i.address from client
    join info i on client.client_id = i.client_id
where i.town = 'Town 6';

drop view clients_from_Town6;

create  or replace view clinets_inapril as
    select c.*, oc.order_id, oc.date_of_renting from client c
join order_car oc on c.client_id = oc.client_id
where oc.date_of_renting between '2021-04-01' and '2021-04-30';

drop view clinets_inapril;

--Hash Join  (cost=4026.01..6288.35 rows=10880 width=35)
create materialized view clients_br15 as
   select cl.client_id, cl.first_name, cl.last_name, c.car_number, c.branch_number from client cl
join order_car oc on cl.client_id = oc.client_id
join car c on c.car_number = oc.car_number
where c.branch_number = 15;

drop materialized view clients_br15;