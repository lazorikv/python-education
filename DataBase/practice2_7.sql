

create or replace function set_zero(x varchar)
returns void
language plpgsql
as $$

begin
  update orders
  set shipping_total = 0
  where carts_cart_id in
  (select cart_id from carts c
            join users u on c.users_user_id = u.user_id
            where u.city = x);

    if not found then
        raise 'City % not found', x;
    end if;
end;$$;


select set_zero('city 4');

select * from orders
    where shipping_total = 0;


/*task2*/
create procedure add_ord(ship numeric, tot numeric)
language plpgsql
as $$
begin
    if ship > 10 and tot < 60 then
    insert into orders(shipping_total, total)
    values (ship, tot);
    end if;
commit;
end;$$;

call add_ord(20, 40);


create procedure loop_insert(f_name varchar, countr varchar)
language plpgsql
as $$
    declare count int := 0;
        begin
        loop
            exit when count = 5;
            count:= count + 1;
            insert into users(first_name, country)
            VALUES (f_name, countr);
        end loop;
    end;
    $$;
drop procedure loop_insert(f_name varchar, countr varchar);

call loop_insert('vlad', 'ukraine');


/*task3*/
SELECT product_title, price, avg(price) OVER (PARTITION BY category_title)
      FROM products p JOIN categories c
	ON p.category_id = c.category_id;


/*task4*/
/*Function for trigger*/
create or replace function total_check()
returns trigger
language plpgsql
as
    $$
    begin
        if new.total = 0 then
            raise 'Final price is 0, add something to cart';
        end if;
        return new;
    end;
    $$;
/*trigger*/
create trigger check_total
  before insert or update
  on orders
  for each row
  execute procedure total_check();

drop trigger check_total on orders;

/*test trigger*/
update orders
set total = 0
where order_id = 1;


create or replace function cart_check()
returns trigger
language plpgsql
as
    $$
    begin
        if new.subtotal > new.total then
            raise 'Subtotal more than total, smth wrong';
        end if;
        return new;
    end;
    $$;

create trigger cart_check
  before insert or update
  on carts
  for each row
  execute procedure cart_check();

drop trigger cart_check on carts;

insert into carts(subtotal, total)
values (1000, 100);