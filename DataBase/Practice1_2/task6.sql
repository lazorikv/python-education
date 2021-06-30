/*task6*/



create or replace function check_pay()
returns trigger
language plpgsql
as $$
    begin
        if new.price_per_day > 1000 then
            raise 'Any car rental costs less than $ 1,000';
        end if;
        return new.price_per_day;
    end;
    $$;

create trigger check_pay
    before insert or update
  on car
  for each row
  execute procedure check_pay();

insert into car
values (34523,13, 'asdf', 'asdfa', 1200);

create or replace function check_period()
returns trigger
language plpgsql
as $$
    begin
        if new.period_of_renting > 10 then
            raise 'Any car rental lasts less than 10 days, check the details';
        end if;
        return new.period_of_renting;
    end;
    $$;

create trigger check_pay
    after insert or update
  on order_car
  for each row
  execute procedure check_period();

update order_car
set period_of_renting = 11
where order_id = 1;