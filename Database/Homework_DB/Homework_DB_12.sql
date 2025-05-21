/* HW12_ procedure */
USE 210225_Platonova;
CREATE TABLE employees 
( id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), age INT, salary INT, department_id INT );

# drop procedure add_employee
#delete  from employees;
DELIMITER $$
CREATE PROCEDURE add_employee(IN emp_name VARCHAR(100), IN emp_age INT, IN department_id INT)
BEGIN
	INSERT INTO employees (name, age, salary, department_id ) VALUES (emp_name, emp_age, rand()*100, department_id);
END $$
DELIMITER ;

call add_employee ('Ruslan', 26, 3);
/* 1 Вывести id департамента , в котором работает сотрудник, в зависимости от Id сотрудника */
#select department_id from employees where id=7;

# variant 1 ohne OUT
DELIMITER $$
CREATE PROCEDURE P_department_id(IN emp_id INT)
BEGIN
	SELECT department_id FROM employees WHERE id = emp_id;
END$$
DELIMITER ;

SELECT * from employees; # 7(id)	Ira	55	30	2(department_id)
call P_department_id(7); #2

# variant 2 mit OUT
DELIMITER $$
CREATE PROCEDURE P_get_department_id(IN emp_id INT, OUT department INT)
BEGIN
	SELECT department_id INTO department FROM employees WHERE id = emp_id;
END$$
DELIMITER ;

SELECT * from employees; # 7(id)	Ira	55	30	2(department_id)
call P_get_department_id(7,@department);
SELECT(@department); #2

/* 2 Создайте хранимую процедуру get_employee_age, которая принимает id сотрудника (IN-параметр) и возвращает его возраст через OUT-параметр.*/
DELIMITER $$
CREATE PROCEDURE get_employee_age(IN emp_id INT, OUT age_emp INT)
BEGIN
	SELECT age INTO age_emp FROM employees where id = emp_id;
END $$
DELIMITER ;

call get_employee_age(7,@age_emp);	# 7(id)	Ira	55(age)	30(salary)	2(department_id)
select(@age_emp);	#55

/* 3 Создайте хранимую процедуру increase_salary, которая принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%. */
DELIMITER $$
CREATE PROCEDURE increase_salary(INOUT salary_emp NUMERIC(10,2))
BEGIN
	 SET salary_emp = salary_emp * 0.9; 
END $$
DELIMITER ;
SET @salary_emp = 100;
call increase_salary(@salary_emp);
select(@salary_emp);	#90
