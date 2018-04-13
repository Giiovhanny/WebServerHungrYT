--modelo de base de datos 09/04/18
create database "YachayFood"
	with
	owner seraquive
	encoding = 'UFT8'
	connection limit = -1;
	
create table product(	id_product 			int, 
						id_seller 			int, 
						name 				varchar(30), 
						description 		varchar(255), 
						precio_unitario 	numeric(5,2),
						stock 				int,
						image 				bytea, 
						delivery_date 		timestamp,
						limit_date 			timestamp,
						register_date 		date,
						id_category 		int);

create table customer (		id_customer 	int,
						name 		varchar(30),
						last_name 	varchar(30),
						email 	 	varchar(50),
						customer_name 	varchar(15),
						password	varchar(10),
						cellphone 	varchar(10),
						is_seller	bool,
						direction	varchar(255));
						
create table shopping_cart(	id_cart 		int, 
							id_buyer 	int,
							direction	varchar(255));
	
create table transactions(	id_transactions		int,
							id_buyer 			int,
							direction			varchar(255));
				
create table indent (		id_indent 		int,
							id_cart			int,
							id_product		int,
							quantity		int);

create table delivery_product(	id_delivery int,
								id_product 	int,
								id_transactions 	int,
								quantity		int,
								state			bool,
								date 			timestamp);
								
create table calification(	id_calification int,
							id_delivery		int,
							score			int,
							comment			varchar(400));
					
create table category(	id_category int,
						name 		varchar(30),
						description varchar(255));
						
--Restricciones 
alter table category add primary key(id_category);
alter table calification add primary key (id_calification);
alter table customer add primary key (id_customer);
alter table shopping_cart add primary key (id_cart);
alter table transactions add primary key(id_transactions);
alter table indent add primary key (id_indent);
alter table delivery_product add primary key(id_delivery);
alter table product add primary key (id_product);
--foreing key
alter table shopping_cart add constraint fk_customer foreign key (id_buyer) references customer(id_customer) on delete cascade;

alter table transactions add constraint fk_customer foreign key(id_buyer) references customer(id_customer) on delete cascade;

alter table product add constraint fk_customer foreign key (id_seller) references customer(id_customer) on delete cascade;
alter table product add constraint fk_category foreign key (id_seller) references customer(id_customer) on delete cascade;

alter table indent add constraint fk_product foreign key (id_product) references product(id_product) on delete cascade;
alter table indent add constraint fk_shopping_cart foreign key (id_cart) references shopping_cart(id_cart) on delete cascade;

alter table calification add constraint fk_delivery_product foreign key(id_delivery) references delivery_product(id_delivery) on delete cascade;

alter table delivery_product add constraint fk_product foreign key(id_product) references product(id_product) on delete cascade;
alter table delivery_product add constraint fk_transactions foreign key(id_transactions) references transactions(id_transactions) on delete cascade;

