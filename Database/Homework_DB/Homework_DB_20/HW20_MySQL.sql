/* Работаем с базой данных sakila.
1.Вывести названия фильмов с расшифровкой рейтинга для каждого. 
Рейтинги описаны здесь (Wikipedia: G – General Audiences, PG – Parental Guidance Suggested,...). 
В таблице film хранятся годы рейтингов. Нужно воспользоваться оператором case;
 чтобы определить для каждого кода условие, по которому будет выводится его развернутое описание (1 предложение). */
USE sakila;
# select * from film; # 300 rows
# select COUNT(*) from film; #1000 rows
# SELECT COUNT(DISTINCT film_id) FROM film; # 1000 rows
SELECT 
     film_id, title, 
     #rating,
CASE rating
	WHEN 'G' THEN 'General Audiences'
	WHEN 'PG' THEN 'Parental Guidance Suggested'
    WHEN 'PG-13' THEN 'Parents Strongly Cautioned'
    WHEN 'R' THEN 'Restricted'
    WHEN 'NC-17' THEN 'Adults Only'
    ELSE 'Unknown'
END AS rating_description
FROM film;	# 300 rows
#ORDER BY rating;


/* 2. Выведите количество фильмов в каждой категории рейтинга. Используем group by. */
SELECT 
     rating, 
     COUNT(film_id) AS "count of films in each rating category"
     FROM film
     GROUP BY 1;	# 5 rows
     
/* 3.Используя оконные функции и partition by, выведите список названий фильмов, рейтинг и количество фильмов в каждом рейтинге. 
Объясните, чем отличаются результаты предыдущего запроса и запроса в этой задаче. */

# count(film_id) OVER (PARTITION BY rating) - считает, сколько фильмов в каждой категории, но не агрегирует, 
# а просто добавляет это число к каждой строке.
SELECT 
     film_id, title, rating, 
     COUNT(film_id) OVER (PARTITION BY rating) AS "count of films in each rating category"
FROM film
ORDER BY film_id;	# 1000 rows
#select COUNT(*) from film; #1000 rows

/* 4.Изучите таблицы payment и customer. 
Выведите список всех платежей с указанием имени и фамилии каждого заказчика, датой платежа и суммой.*/
# select * from payment; # 300 rows
# select * from customer; # 300
SELECT 
	p.payment_id, p.amount, p.payment_date,
	c.first_name, c.last_name 
FROM payment AS p
LEFT JOIN  customer AS c
ON p.customer_id = c.customer_id;	# 300 rows


/* 5.Поменяйте предыдущий запрос так, чтобы дата выводилась в !!!! формате “число, название месяца, год” (без времени).*/
SELECT 
	p.payment_id, p.amount, 
    DATE_FORMAT(p.payment_date, '%e %M %Y') AS payment_date,
	c.first_name, c.last_name 
FROM payment AS p
LEFT JOIN  customer AS c
ON p.customer_id = c.customer_id;	# 300 rows
