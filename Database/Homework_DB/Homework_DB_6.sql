/* 10-04-2025, 13-04-2025
1 Выведите одним запросом с использованием UNION столбцы id, employee_id из таблицы orders и 
соответствующие им столбцы из таблицы purchase_orders. 
В таблице purchase_orders  created_by соответствует employee_id. */
#SELECT *  from orders;
#SELECT *  from purchase_orders;
#SELECT id, employee_id , 'von orders' as 'table name' FROM  orders 
#union 
#SELECT id, created_by, 'von purchase_orders' FROM purchase_orders
#ORDER BY 2;

SELECT 
    id, employee_id
FROM
    orders 
UNION SELECT 
    id, created_by
FROM
    purchase_orders;



/* 2 Из предыдущего запроса удалите записи, там где employee_id не имеет значения.
 Добавьте дополнительный столбец со сведениями из какой таблицы была взята запись. */
SELECT 
    id, employee_id, 'orders' AS table_name
FROM
    orders
WHERE
    employee_id IS NOT NULL 
UNION SELECT 
    id, created_by, 'purchase_orders'
FROM
    purchase_orders
WHERE
    created_by IS NOT NULL;
 
/* 3 Выведите все столбцы таблицы order_details, а также дополнительный столбец payment_method из таблицы purchase_orders.
 Оставьте только заказы, для которых известен payment_method. */
#SELECT  od.*, p.id, pod.product_id, po.id, pod.purchase_order_id, po.payment_method
# variant 1 
SELECT  od.*, po.payment_method
FROM
    order_details AS od
        JOIN
    products AS p ON od.product_id = p.id
        JOIN
    purchase_order_details AS pod ON p.id = pod.product_id
        JOIN
    purchase_orders AS po ON po.id = pod.purchase_order_id  # 139 rows
WHERE
   payment_method IS NOT NULL;		#3 rows


# variant 2 (связь через другую таблицу)
#SELECT  od.*, p.id, pod.product_id, pod.purchase_order_id, po.id, po.payment_method
SELECT  od.*, po.payment_method
FROM
    order_details AS od
    join products as p			# 58 rows
    on od.product_id=p.id
    join purchase_order_details as pod  # 139 rows
    on p.id=pod.product_id
	join purchase_orders as po
    on pod.purchase_order_id=po.id 	#139 rows
WHERE
   payment_method IS NOT NULL;	# 3 rows
   
/*SELECT * from purchase_orders
where payment_method is NOT null;		# 2 rows
SELECT * FROM order_details;
*/

/* 4 Выведите заказы (id?) orders и фамилии клиентов customers для тех заказов, по которым были инвойсы таблица invoices. */
/* variant 1 - alle Information */
SELECT c.last_name, o.*  from orders as o
#left join invoices as i 	# 48 rows
join invoices as i 			# 35 rows
on o.id=i.order_id
join customers as c		# 35 rows
on c.id=o.customer_id;

/* variant 2 - только номер заказа и фамилия*/
SELECT 
    i.order_id, c.last_name
FROM
    invoices AS i
        JOIN
    orders AS o ON i.order_id = o.id
        JOIN
    customers AS c ON o.customer_id = c.id;
    #ORDER BY last_name;

#SELECT * from invoices;  # 35 rows
#select * from orders;
#SELECT * from customers;


/* 5 Подсчитайте количество инвойсов для каждого клиента из предыдущего запроса. */
SELECT 
    o.customer_id, c.last_name, count(i.id) as 'количество инвойсов'
    #group_concat(i.id) as 'список id инвойсов',
    # group_concat(i.order_id) as 'список order_id'
FROM
    invoices AS i
        JOIN
    orders AS o ON i.order_id = o.id
        JOIN
    customers AS c ON o.customer_id = c.id
    GROUP BY o.customer_id,	c.last_name		# 14 rows (в GROUP BY нужно указывать ВСЕ столбы из SELECT, кроме тех, что испол. в агрегатной функции)
    ORDER BY last_name;