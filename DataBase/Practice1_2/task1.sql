create table branch(
    branch_number serial4,
    info_id int,
    primary key (branch_number)
);
ALTER TABLE branch ADD FOREIGN KEY (info_id) REFERENCES info(info_id) on delete cascade;


/*insert branch*/
do
$$
declare counter int := 0;

begin
     loop
         counter:= counter + 1;
         exit when counter = 21;
     insert into branch(branch_number, info_id)
         values (counter, counter);
     end loop;
end;
$$;




drop table branch cascade;


create table client(
    client_id serial4,
    info_id int,
    first_name varchar(100),
    last_name varchar(100),
    primary key (client_id),
    foreign key (info_id)
                   references info(info_id) on delete cascade
);

drop table client cascade;


/*insert clients*/
do
$$
declare counter int := 0;

begin
     loop
         counter:= counter + 1;
         exit when counter = 99980;
     insert into client(info_id, first_name, last_name)
         values (counter + 20, concat('Name ', counter), concat('Surname ', counter));
     end loop;
end;
$$;



create table info(
    info_id serial4,
    client_id int,
    branch_id int,
    town varchar(100),
    address varchar(100),
    telephone int,
    primary key (info_id),

    foreign key (branch_id)
                 references branch(branch_number) on delete cascade
);

ALTER TABLE info ADD FOREIGN KEY (client_id) REFERENCES client(client_id) on delete cascade;


/*insert info*/
do
$$
declare counter int := 0;

begin
     loop
         counter:= counter + 1;
         exit when counter = 100000;
     insert into info(client_id, branch_id, town, address, telephone)
         values (random()*(50000-1)+1, random()*(20-1)+1, concat('Town ', counter), concat('Address ', counter), counter + 1000);
     end loop;
end;
$$;




create table car(
    car_number int,
    branch_number int,
    brand varchar not null,
    model varchar not null,
    price_per_day int not null,
    primary key (car_number)

);

ALTER TABLE car ADD FOREIGN KEY (branch_number) REFERENCES branch(branch_number) on delete cascade;


/*insert car*/
create or replace function insert_cars()
returns void
language plpgsql
as $$
declare counter int := 0;
    declare counter1 int := 0;
    declare counter2 int := 100;
    declare counter3 int := 0;
begin
        loop
            exit when counter = 15;
            counter:= counter + 1;
            counter1:= 0;
            loop
                exit when counter1 = 20;
                counter1:= counter1 + 1;
                counter3 := counter3 + 1;
                insert into car(car_number, branch_number, brand, model, price_per_day)
                values (counter3, random()*(20-1)+1, concat('Brand ', counter), concat('Model ', counter1), counter2);
            end loop;
            counter2:= counter2 + 50;
        end loop;
end;
$$;
drop table car cascade;

select insert_cars();

create table order_car(
    order_id serial,
    car_number int,
    client_id int,
    date_of_renting date,
    period_of_renting int,
    primary key (order_id),
    foreign key (car_number)
                   references car(car_number) on delete cascade
);

ALTER TABLE order_car ADD FOREIGN KEY (client_id) REFERENCES client(client_id) on delete cascade;

/*insert into orders*/
do
$$
declare counter int := 0;
    counter1 int := 0;
begin
        <<first>>
        loop
            exit when counter = 1700;
            counter:= counter + 1;
            counter1:= 0;
            <<second>>
            loop
                exit when counter1 = 120;
                counter1:= counter1 + 1;

                insert into order_car(car_number, client_id, date_of_renting, period_of_renting)
                values (random()*(300-1)+1, random()*(99979-1)+1, date '01-01-2021' + counter1, random()*(10-1)+1);
            end loop second;
        end loop first;
end;
$$;


drop table order_car cascade;

