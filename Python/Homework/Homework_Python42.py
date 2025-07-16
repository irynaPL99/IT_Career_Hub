'''Task 1. Создание базы
Напишите программу, которая:
создаёт базу данных notes_app_<your_group>_<your_full_name>
выбирает эту базу через USE notes_app
выводит сообщение о результате

# Task2. Добавление заметок
# Продолжите предыдущую программу:
# создайте таблицу notes с полями: id, title, content
# вставьте одну заметку в таблицу
# выполните commit() после вставки
# выведите все заметки используя DictCursor
'''
print("\nTask 1. Создание базы notes_app_<your_group>_<your_full_name>")
from pymysql.cursors import DictCursor
import pymysql
from pymysql import Error

try:
    config = {
        'host': 'ich-edit.edu.itcareerhub.de',
        'user': 'ich1',
        'password': 'ich1_password_ilovedbs',
    }
    #connection = pymysql.connect(**config, cursorclass=DictCursor)
    with pymysql.connect(**config, cursorclass=DictCursor) as connection:  # автоматически закроет connection

        with connection.cursor() as cursor: # # автоматически закроет cursor
            cursor.execute("CREATE DATABASE IF NOT EXISTS notes_app_210225_Platonova")
            cursor.execute("USE notes_app_210225_Platonova")

            if connection:
                print("Database 'notes_app_210225_Platonova' created or alredy exists.")


            #Создание таблицы notes
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS notes (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            title VARCHAR(20),
                            content TEXT
                        )
                    """)
            insert_query = "INSERT INTO notes (title, content) VALUES (%s, %s)"
            cursor.execute(insert_query, ("first note", "Content for first note"))

            connection.commit()
            print("Заметка добавлена в таблицу 'notes'.")

            cursor.execute("SELECT * FROM notes")
            for row in cursor:
                #print(row)
                print(f"{row['title']}: {row['content']}")


except Error as e:
    print(f"Ошибка при работе с базой данных 'notes_app_210225_Platonova':", e)



