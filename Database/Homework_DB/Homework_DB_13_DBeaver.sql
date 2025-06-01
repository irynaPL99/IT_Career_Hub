# HW_13 in DBeaver
#1 Выберите только те строки из таблицы suppliers где company имеет значение Supplier A
select * from suppliers
where company = "Supplier A" ;

#2 Вывести все строки там, где purchase_order_id не указано. 
#При этом дополнительно создать столбец total_price как произведение quantity * unit_price
select (quantity * unit_price) as total_price,
od.* 
FROM  order_details as od
where purchase_order_id is NULL;

#select * from order_details od 

#3 Выведите какая дата будет через 51 день
select CURDATE() as Heute,
DATE_ADD(CURDATE(), INTERVAL 51 DAY) as Zukunft;

#4  Посчитайте количество уникальных заказов purchase_order_id
select COUNT(DISTINCT purchase_order_id)
from order_details; 

#5 Выведите все столбцы таблицы order_details, а также дополнительный столбец payment_method из таблицы purchase_orders.
# Оставьте только заказы для которых известен payment_method
select od.*, po.payment_method 
from order_details od
join purchase_orders po 
on od.purchase_order_id = po.id
where po.payment_method is not NULL;



#select * from purchase_orders po 
