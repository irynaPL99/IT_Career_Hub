/* HW 9
1. Таблица purchase_order_details
 Для каждого заказа order_id выведите минимальный, максмальный и средний unit_cost */
# variant 1 mit partition
select min(unit_cost)over (partition by purchase_order_id) as min_unit_cost,
 max(unit_cost) over (partition by purchase_order_id) max_unit_cost,
 avg(unit_cost) over (partition by purchase_order_id) avg_unit_cost,
# ROW_NUMBER() over (partition by purchase_order_id) as rn,
 pod.*
from purchase_order_details as pod
# ORDER BY purchase_order_id, rn;
ORDER BY purchase_order_id;	# 55 rows

# variant 2 mit cte
WITH cte as (
select min(unit_cost)over (partition by purchase_order_id) as min_unit_cost,
 max(unit_cost) over (partition by purchase_order_id) max_unit_cost,
 avg(unit_cost) over (partition by purchase_order_id) avg_unit_cost,
# ROW_NUMBER() over (partition by purchase_order_id) as rn,
 pod.*
from purchase_order_details as pod
# ORDER BY purchase_order_id, rn;
ORDER BY purchase_order_id
)
select min_unit_cost, max_unit_cost, avg_unit_cost, purchase_order_id, product_id from cte;	

# variant 3 mit group by
select purchase_order_id, 
group_concat(product_id) as "List von product_id",
min(unit_cost) as min_uni_cost,
max(unit_cost) as min_uni_cost,
avg(unit_cost) as min_uni_cost
from purchase_order_details as pod
group by 1
order by 1;		# 28 rows

/* 2  Оставьте только уникальные строки из предыдущего запроса */
# variant 1 mit CTE
with cte as (
select 
min(unit_cost)over (partition by purchase_order_id) as min_unit_cost,
 max(unit_cost) over (partition by purchase_order_id) max_unit_cost,
 avg(unit_cost) over (partition by purchase_order_id) avg_unit_cost,
# ROW_NUMBER() over (partition by purchase_order_id) as rn,
 pod.*
from purchase_order_details as pod
# ORDER BY purchase_order_id, rn;
ORDER BY purchase_order_id
)
select  DISTINCT(cte.purchase_order_id), min_unit_cost, max_unit_cost, avg_unit_cost
from cte;	# 28 rows

# variant 3 mit union
with cte as (
select 
min(unit_cost)over (partition by purchase_order_id) as min_unit_cost,
 max(unit_cost) over (partition by purchase_order_id) max_unit_cost,
 avg(unit_cost) over (partition by purchase_order_id) avg_unit_cost,
# ROW_NUMBER() over (partition by purchase_order_id) as rn,
 pod.*
from purchase_order_details as pod
# ORDER BY purchase_order_id, rn;
ORDER BY purchase_order_id
)
select min_unit_cost, max_unit_cost, avg_unit_cost, purchase_order_id from cte
union
select min_unit_cost, max_unit_cost, avg_unit_cost, purchase_order_id from cte; # 28 rows


# variant 4 mit cte2 und ROW_NUMBER
with cte as (
select 
min(unit_cost)over (partition by purchase_order_id) as min_unit_cost,
max(unit_cost) over (partition by purchase_order_id) max_unit_cost,
avg(unit_cost) over (partition by purchase_order_id) avg_unit_cost,
#ROW_NUMBER() over (partition by purchase_order_id) as rn,
pod.*
from purchase_order_details as pod
#where rn = 1
#ORDER BY purchase_order_id, rn;
ORDER BY purchase_order_id
),
cte2 as (
select min_unit_cost, max_unit_cost, avg_unit_cost, purchase_order_id,
ROW_NUMBER() over (partition by purchase_order_id order by product_id) as rn
from cte
)
select * from cte2
where rn = 1;  # 28 rows

/* 3 Посчитайте стоимость продукта в заказе как quantity*unit_cost.
 Выведите суммарную стоимость продуктов с помощью оконной функции
 Сделайте то же самое с помощью GROUP BY */
 # variant 1 mit partition
 select round((quantity*unit_cost),2) as kost_product_id, 
 round(sum(quantity*unit_cost) over (PARTITION BY purchase_order_id),2) as sum_kost_order_id,
 pod.* 
 from purchase_order_details as pod
 order by purchase_order_id, product_id; # 90 - 5370, 91 - 4800,...
 
 # variant 1 mit GROUP BY
 select pod.purchase_order_id,
# group_concat(product_id) as "List von product_id",
 #round((quantity*unit_cost),2) as kost_product_id, 
 round(sum(quantity*unit_cost),2) as sum_kost_order_id,
 round((quantity*unit_cost),2) as kost_product_id
 from purchase_order_details as pod
 group by 1	# 28 rows,  90 - 5370, 91 - 4800,...
#group by 1, 2 # 49 rows, !! группировка по kost_product_id НЕ подходит
 order by purchase_order_id; 	# 28 rows, 90 - 5370, 91 - 4800,...
 
 /* 4 Посчитайте количество заказов по дате получения и 
posted_to_inventory (!!!! как это поле использовать?!!!).
 Если оно превышает 1 то выведите '>1' в противном случае '=1'
Выведите purchase_order_id, date_received и вычисленный столбец */
# variant 1 mit partition
SELECT 
#count(purchase_order_id) over (PARTITION BY cast(date_received as date) order by date_received DESC) as count_orders,
pod.purchase_order_id, pod.date_received,
CASE
	when count(purchase_order_id) over (PARTITION BY cast(date_received as date)) > 1 then '>1'
    else '=1' 
    end  as "count_orders превышает 1" 
FROM purchase_order_details as pod
order by purchase_order_id;		# 55 rows

# variant 2 mit group by
SELECT cast(date_received as date),
pod.purchase_order_id, pod.date_received,
#count(purchase_order_id)  as count_orders,
group_concat(purchase_order_id) as "Listen von orders" ,
CASE
	when count(purchase_order_id) > 1 then '>1'
    else '=1' 
    end  as "count_orders превышает 1" 
   # cast(date_received as date),
FROM purchase_order_details as pod
GROUP BY cast(date_received as date)	# если я добавляю сюда еще столбцы, то меянется результат,который мне не пододит!!
order by purchase_order_id;		# 7 rows





