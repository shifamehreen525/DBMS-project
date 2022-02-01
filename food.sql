create database onlinefood;

use onlinefood;

create table STARTERS(Fid int PRIMARY KEY, Fname varchar(30), Fprice int);

describe STARTERS;

insert into STARTERS values
(1,'Manchuria', 120), 
(2,'Crispy Corn',110), 
(3,'Chicken 65', 150), 
(4,'Panner Tikka',80), 
(5,'Fish Chips', 90), 
(6,'Aloo Tikka', 80), 
(7,'Veg Spring Rolls', 120), 
(8, 'Majestic Chicken', 130), 
(9, 'Pepper Chicken', 110), 
(10,'Kebab', 150);

select * from starters;


create table MAINCOURSE(Fid int PRIMARY KEY, Fname varchar(30), Fprice int);

describe MAINCOURSE;

insert into MAINCOURSE values
(1,'Butter Chicken', 170), 
(2,'Veg Biryani',120), 
(3,'Mughlai Biryani', 160), 
(4,'Veg Fried Rice',80), 
(5,'Chicken Fried Rice', 90), 
(6,'Chana Dal', 80), 
(7,'Cashew Curry', 110), 
(8, 'Palak Paneer', 130), 
(9, 'Chicken Mandi', 150), 
(10,'Lamb Curry', 180);

select * from maincourse;


create table DESSERTS(Fid int PRIMARY KEY, Fname varchar(30), Fprice int);

describe DESSERTS;

insert into DESSERTS values
(1,'Apricort Delight', 110), 
(2,'Gajar ka halwa',80), 
(3,'Gulab Jamun', 90), 
(4,'Chocolate Fudge',150), 
(5,'Choco Lava Cake', 130);

select * from desserts;

create table DRINKS(Fid int PRIMARY KEY, Fname varchar(30), Fprice int);

describe DRINKS;

insert into DRINKS values
(1,'Lemonade', 50), 
(2,'Coke', 60), 
(3,'Chocolate Milkshake', 130), 
(4,'Strawberry Juice',110), 
(5,'Iced Berry Tea', 120),
(6, 'Iced Matcha Latte', 140),
(7, 'Mineral Water', 45);

select * from drinks;


 create table cust_details(cust_id int primary key, cust_name varchar(30), cust_ph varchar(10), location varchar(30));
 
 describe cust_details;
 
 select * from cust_details;


create table orders(cust_id varchar(10), fid varchar(10), fname varchar(30), price int, quantity int, cost int);

select * from orders;

create table tableDates(date varchar(10), time varchar(10), capacity int);

select * from tableDates;

create table tableReservation(date varchar(10), time varchar(10), name varchar(30), phone varchar(10), b_id int);

select * from tableReservation;

