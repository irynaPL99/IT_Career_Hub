/* 1   Вывести названия продуктов таблица products, включая количество заказанных единиц quantity 
для каждого продукта таблица order_details.
Решить задачу с помощью cte и подзапроса */
# variant 1.0 - mit CTE
with cte as (
SELECT product_id, sum(quantity) as sum_quantity
from order_details as od
GROUP BY 1		#24 rows
)
#SELECT od.product_id, od.quantity from order_details as od; 
select p.id, p.product_name,
COALESCE(										# Синтаксис COALESCE(..., 0) 
(SELECT cte.sum_quantity 
from cte 
where cte.product_id=p.id), 0
) as 'количество заказанных единиц quantity'
from products as p;	 	# 45 rows


# variant 2 - onhe CTE
select  p.product_name,
(
SELECT  sum(od.quantity) 
from order_details as od
where p.id=od.product_id
) as sum_quantity
from products as p
ORDER BY sum_quantity DESC;	# 45 rows



# variant 3 - join
select  p.id, p.product_name, 
sum(od.quantity) as sum_quantity
#group_concat(od.order_id) as list_von_order_id
from products as p
#join order_details as od   # 24 rows (только продукты, по которым есть заказы)
left join order_details as od   # 45 rows (все продукты)
on p.id=od.product_id
GROUP BY 1 # 
ORDER BY 1;

#select * from products ORDER BY id;  # 45 rows
#select * from order_details; #58 rows


/* 2  Найти все заказы таблица orders, сделанные !после даты самого первого! заказа клиента Lee таблица customers. */
with cte as
(
SELECT min(order_date) as min_order_date
from orders
where customer_id in (SELECT id from customers
where last_name='Lee')  	# '2006-01-20 00:00:00'
)
SELECT * from orders
where order_date > (select cte.min_order_date from cte)
ORDER BY order_date;	


#SELECT * from orders;
#SELECT id from customers
#where last_name='Lee';		# id=4, 29

/* 3 Найти все продукты таблицы  products c максимальным target_level */
#SELECT max(target_level) as max_target_level		# 200
#from products;

# variant 1
SELECT * from products
where target_level = 
(SELECT max(target_level) as max_target_level		
from products);			# 4 rows

# variant 2 - mit CTE
with cte as
(
SELECT max(target_level) as max_target_level		# 200
from products
)
select * from products
where target_level = (SELECT max_target_level from cte);  # 4 rows