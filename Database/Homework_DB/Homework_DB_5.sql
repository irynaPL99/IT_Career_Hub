/*База данных northwind.
Работаем с таблицей purchase_order_details
1 Посчитайте основные статистики - среднее, сумму, минимум, максимум столбца unit_cost.*/
use northwind;
SELECT 
    AVG(unit_cost),
    SUM(unit_cost),
    MIN(unit_cost),
    MAX(unit_cost)
FROM
    purchase_order_details;
    
/* 2 Посчитайте количество уникальных заказов purchase_order_id. */
SELECT count(DISTINCT purchase_order_id)  
as 'количество уникальных заказов purchase_order_id'
from purchase_order_details;

/* 3 Посчитайте количество продуктов product_id в каждом заказе purchase_order_id.
 Отсортируйте полученные данные по убыванию количества. 
 
 НЕ очевидно задание, поэтому два решения.
 variant 1: кол.во типов продуктов (product_id) для каждого заказа */
SELECT 
    purchase_order_id, COUNT(product_id)
FROM
    purchase_order_details
GROUP BY purchase_order_id
ORDER BY 2 DESC;
  
 /*variant 2: кол.во продуктов (quantity) для каждого заказа  */
 SELECT 
    purchase_order_id, COUNT(product_id), SUM(quantity)
FROM
    purchase_order_details
GROUP BY purchase_order_id
ORDER BY SUM(quantity) DESC;
 
 /* 4 Посчитайте заказы по дате доставки date_received. Считаем только те продукты, 
количество quantity, которых больше 30. */
SELECT 
	date_received, quantity,
	count(product_id) as 'кол-во заказов по дате доставки date_received и quantity>30'
	# group_concat(product_id) as 'list von product_id'
FROM
	purchase_order_details
WHERE quantity>30 
# AND date_received is not null  # (если это нужно) исключаем НЕ выполненый заказ (дата пустая)
GROUP BY date_received;

/* 5 Посчитайте суммарную стоимость заказов в каждую из дат. Стоимость заказа - 
произведение quantity на unit_cost. */
SELECT 
	date_received,
	sum(quantity*unit_cost) 
FROM 
	purchase_order_details
# where date_received is not null  # (если это нужно) исключаем НЕ выполненый заказ (дата пустая)
GROUP BY date_received;

/* 6 Сгруппируйте товары по unit_cost и вычислите среднее и максимальное значение quantity 
только для товаров, где purchase_order_id не больше 100. */
SELECT 
    unit_cost,
    AVG(quantity),
    MAX(quantity)
    # GROUP_CONCAT(quantity) AS 'list von quantity',
    # COUNT(unit_cost) AS 'count unit_cost'
FROM
    purchase_order_details
WHERE
    purchase_order_id <= 100
GROUP BY unit_cost;

/* 7 Выберите только строки, где есть значения в столбце inventory_id.
 Создайте столбец category - если unit_cost > 20 то 'Expensive', в остальных случаях 'others'. 
Посчитайте количество продуктов в каждой категории.*/
SELECT  
sum(quantity) as 'количество продуктов (quantity) в каждой категории (category)', 
# sum(product_id) as 'количество типов продуктов (product_id) в каждой категории (category)', 
# group_concat(product_id) as 'list von product_id',
case
	when  unit_cost > 20 then 'Expensive'
	else 'others'
end as category
FROM purchase_order_details
WHERE inventory_id is not null
GROUP BY category;




