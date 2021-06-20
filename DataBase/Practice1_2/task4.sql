/*Task4*/

create or replace function get_clients(cl_town varchar)
   returns text as $$
declare
    last_names text default '';
	 rec_client record;
	 cur_client cursor(cl_town varchar)
		 for select last_name, town
		 from client
		 join info on client.client_id = info.client_id
		 where info.town = cl_town;
begin
   open cur_client(cl_town);
    last_names := 'Last_name: ';
   loop
      fetch cur_client into rec_client;
      exit when not found;
         last_names := last_names || rec_client.last_name || ' from ' || rec_client.town || '; ';
   end loop;
   close cur_client;
   return last_names;
end; $$
language plpgsql;


select get_clients('Town 10');



create or replace function some_update ()
returns table (
	brand_car varchar, model_car varchar
)
language plpgsql
as $$
declare
    var_r record;
begin
	for var_r in(
            select brand, model
            from car
	     where brand = 'Brand 1'
        ) loop
	    brand_car := upper(var_r.brand);
		model_car := var_r.model;
           return next;
	end loop;
end; $$;

select some_update();