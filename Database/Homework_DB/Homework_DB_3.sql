/* Homework 24-03-2025
1. Выведите Ваш возраст на текущий день в секундах */ 
#select curdate(), datediff(curdate(), '1980-12-01'), 60*60*24, datediff(curdate(), '1980-12-01')*60*60*24 AS "Мой возраст, sec";
SELECT DATEDIFF(CURDATE(), '1980-12-01') * 86400 AS "Мой возраст, sec";

/* 2. Выведите какая дата будет через 51 день */
#select curdate(), date_add(curdate(), interval 51 day) as "дата через 51 день";
SELECT DATE_ADD(CURDATE(), INTERVAL 51 DAY) AS 'дата через 51 день';

/* 3. Отформатируйте предыдущей запрос - выведите день недели для этой даты. Используйте документацию My SQL */
#select curdate(), date_add(curdate(), interval 51 day), date_format(date_add(curdate(), interval 51 day), '%W') as "день недели через 51 день";
#select ELT(DAYOFWEEK(date_add(curdate(), interval 51 day)), 'Воскресенье', 'Понедельник', 'Вторник', 'Среда', 
#'Четверг', 'Пятница', 'Суббота') as "день недели через 51 день";
#select date_format(date_add(curdate(), interval 51 day), '%W') as "день недели через 51 день";
SELECT DAYNAME(DATE_ADD(CURDATE(), INTERVAL 51 DAY)) AS 'день недели через 51 день';

/* 4.  Подключитесь к базе данных northwind Выведите столбец с исходной датой создания 
транзакции transaction_created_date из таблицы inventory_transactions, 
а также столбец полученный прибавлением 3 часов к этой дате */
USE northwind;
SELECT 
    transaction_created_date,
    DATE_ADD(transaction_created_date,
        INTERVAL 3 HOUR) AS 'transaction_created_date + 3 hours'
FROM
    inventory_transactions;

/* 5. Выведите столбец с текстом  'Клиент с id <customer_id> сделал заказ <order_date>' из таблицы orders.
 Запрос написать !!! двумя!!! способами - с использованием неявных преобразований а также с указанием 
изменения типа данных для столбца customer_id.
Внимание В MySQL функция CAST не принимает VARCHAR в качестве параметра для длины. 
Вместо этого, нужно использовать CHAR для указания длины.*/
#variant 1:
#select customer_id, order_date, 

SELECT 
	CONCAT('Клиент с id ',customer_id, ' сделал заказ ', order_date) 
	AS "Клиент с id <customer_id> сделал заказ <order_date>"
FROM 
	orders;

#variant 2:
#select cast(customer_id as char(2)) as "customer_id is char", order_date
SELECT
	CONCAT('Клиент с id ',CAST(customer_id AS CHAR(2)), ' сделал заказ ', order_date)
	AS "Клиент с id <customer_id> сделал заказ <order_date>"
FROM 
	orders;
#order by customer_id desc;
