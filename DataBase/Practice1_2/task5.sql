/*task5*/

create or replace procedure insert_car(cost_car int)
language plpgsql
as
    $$
    begin
        savepoint sp1;
        if cost_car = 250 then
            insert into car(branch_number,brand, model,price_per_day)
            values (15, 'Brand 4', 'Model 21', 250);
        else
            delete from car
            where brand = 'Brand 4' and model = 'Model 20';
        end if;
       commit;
    end;
    $$;


call insert_car(250);
drop procedure insert_car();



create or replace procedure update_branch()
language plpgsql
as $$
    begin
    savepoint sp1;
        update car
        set brand = 'Mersedes'
        where branch_number in
        (select branch_number from order_car o
        left join car c on o.car_number=c.car_number
        where date_of_renting between '2021-05-01' and '2021-06-01');
        rollback to savepoint sp1;
    end;
    $$;

call update_branch();
drop procedure update_branch();