/* Homework 10
Таблица order_details
1 Для каждого product_id выведите inventory_id а также предыдущий и 
последующей inventory_id по убыванию quantity. */
select
od.product_id, od.inventory_id, od.quantity,
LAG(inventory_id) over (order by quantity DESC) as "предыдущий inventory_id по убыванию quantity" ,
LEAD(inventory_id) over (order by quantity DESC) as "последующей inventory_id по убыванию quantity" 
from order_details as od;

/* 2 Выведите максимальный и минимальный unit_price для каждого order_id 
с помощью функции FIRST_VALUE.  Вывести order_id и полученные значения. */
# variant 1 - mit Duble
select od.order_id,
FIRST_VALUE(unit_price) over (PARTITION BY order_id ORDER BY unit_price) as "min unit_price by order_id",
FIRST_VALUE(unit_price) over (PARTITION BY order_id ORDER BY unit_price DESC) as "max unit_price by order_id"
from order_details as od
ORDER BY order_id;	# 58 rows

# variant 2 - onhe Duble
select DISTINCT od.order_id,
FIRST_VALUE(unit_price) over (PARTITION BY order_id ORDER BY unit_price) as "min unit_price by order_id",
FIRST_VALUE(unit_price) over (PARTITION BY order_id ORDER BY unit_price DESC) as "max unit_price by order_id"
from order_details as od
ORDER BY order_id; # 40 rows

# variant 3 - onhe Duble, mit ROW_NUMBER und CTE
with cte as 
(
select 
ROW_NUMBER() over (PARTITION BY order_id) as rn,
od.order_id,
FIRST_VALUE(unit_price) over (PARTITION BY order_id ORDER BY unit_price) as "min unit_price by order_id",
FIRST_VALUE(unit_price) over (PARTITION BY order_id ORDER BY unit_price DESC) as "max unit_price by order_id"
from order_details as od
ORDER BY order_id
)
select * from cte
where rn=1;		# 40 rows


# variant 4 - onhe Duble, mit ROW_NUMBER; mit subquery
select * from
(select 
ROW_NUMBER() over (PARTITION BY order_id) as rn,
od.order_id,
FIRST_VALUE(unit_price) over (PARTITION BY order_id ORDER BY unit_price) as "min unit_price by order_id",
FIRST_VALUE(unit_price) over (PARTITION BY order_id ORDER BY unit_price DESC) as "max unit_price by order_id"
from order_details as od
ORDER BY order_id) as subquery
where rn=1;		# 40 rows

#select * from order_details
#where order_id=30;

/* 3 Выведите order_id и столбец с разнице между  unit_price для каждой заказа и
 минимальным unit_price в рамках одного заказа.
 Задачу решить двумя способами - с помощью First VAlue и MIN */
# variant 1 - mit FIRST_VALUE
select od.order_id, 
#od.unit_price,
#FIRST_VALUE(unit_price) over (PARTITION BY order_id ORDER BY unit_price) as "min unit_price by order_id",
(unit_price - FIRST_VALUE(unit_price) over (PARTITION BY order_id ORDER BY unit_price)) as "diff(unit_price, min unit_price"
from order_details as od
ORDER BY order_id;

#  variant 2 - mit MIN
with cte as (
select od.order_id,
MIN(unit_price) as min_unit_price_by_order_id
from order_details as od
group by 1
)
select od.order_id, 
#od.unit_price,
#cte.min_unit_price_by_order_id,
(od.unit_price - cte.min_unit_price_by_order_id) as "diff(unit_price, min unit_price"
from
order_details as od
join cte
on od.order_id=cte.order_id
ORDER BY od.order_id;

/* 4 Присвойте ранг каждой строке используя RANK по убыванию quantity */
select 
RANK() over (ORDER BY quantity DESC) as Rank_,
#DENSE_RANK() over (ORDER BY quantity DESC) as DENSE_RANK_,
od.* 
from order_details as od;

/* 5  Из предыдущего запроса выберите только строки с рангом до 10 включительно */
# variant 1 - mit subquery
select * from
(select 
RANK() over (ORDER BY quantity DESC) as Rank_,
#DENSE_RANK() over (ORDER BY quantity DESC) as DENSE_RANK_,
od.* from order_details as od) as subquery
where Rank_ <= 10;

# variant 1 - mit CTE
with cte as
(
select 
RANK() over (ORDER BY quantity DESC) as Rank_,
#DENSE_RANK() over (ORDER BY quantity DESC) as DENSE_RANK_,
od.* from order_details as od
)
select * from cte
where Rank_ <= 10;
