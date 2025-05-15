# Homework DB 11, 15-05-2025
/*Создать кастомные функции
1. Функция для расчета площади круга*/
DELIMITER //
CREATE FUNCTION circle_squere(radius FLOAT)
RETURNS FLOAT
BEGIN 
	RETURN PI() * POWER(radius,2);
END //
DELIMITER ;
SELECT circle_squere(2);


/* 2. Функция для расчета гипотенузы треугольника */
DELIMITER //
CREATE FUNCTION gipotenuza(a FLOAT, b FLOAT)
RETURNS FLOAT
BEGIN
	RETURN sqrt (a*a + b*b);
END //
DELIMITER ;
SELECT gipotenuza(3,4);



