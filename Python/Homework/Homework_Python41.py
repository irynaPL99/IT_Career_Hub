'''Task 1. Список всех стран
Используя базу данных world, выведи названия всех стран из таблицы country.
Каждое название должно отображаться с новой строки и иметь номер.
Пример вывода:
1. Aruba
2. ...
...
239. Zimbabwe
'''

print("\nTask 1. Список всех стран")
import pymysql

config = {
    "host": "ich-db.edu.itcareerhub.de",
    "user": "ich1",
    "password": "password",
    "database": "world",
}
query_sql = """SELECT Name FROM country"""

with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute(query_sql)

        #rows = cursor.fetchall()  # получить все строки (ВСЕ столбцы)
        #print(cursor.rownumber) # last number
        #for i, name in enumerate(rows, start=1):
        #    print(f"{i}. {name[0]}")
        countries = [row[0] for row in cursor] # list: только первый столбец из каждой строки
        #print(countries)   #['Afghanistan', 'Albania', ...]
        for i, name in enumerate(countries, start=1):
            print(f"{i}. {name}")

'''Task 2. Города выбранной страны
Добавьте к предыдущей программе возможность выбора страны. 
Пользователь введёт название !!!или!!! номер из выведенного списка. 
Далее выведите все города этой страны и их численность населения, 
также с нумерацией.
'''
print("\nTask 2. Города выбранной страны")
import pymysql

config = {
    "host": "ich-db.edu.itcareerhub.de",
    "user": "ich1",
    "password": "password",
    "database": "world",
}
with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute("""SELECT Name FROM country""")
        countries = [row[0] for row in cursor]  # list: только первый столбец из каждой строки
        # print(countries)
        for i, name in enumerate(countries, start=1):
            print(f"{i}. {name}")          # 239. Zimbabwe


        user_choice = input("\nВведите страну: ").strip()

        # Определяем страну:
        selected_country = None
        if user_choice.isdigit():   # номер
            index_list = int(user_choice) - 1
            if 0 <= index_list < len(countries):
                selected_country = countries[index_list]

        else:
            for name in countries:          # name
                if name.lower() == user_choice.lower():
                    selected_country = name
                    break   # находит первое совпадение и выходим
        #print(f"selected_country: {selected_country}")

        # Если страна найдена — ищем города, else - вывод ошибки
        if selected_country:
            pass
        else:
            print(f"Country '{user_choice}' is not found!")

        cursor.execute("""
                SELECT city.Name, city.Population 
                FROM city 
                JOIN country 
                ON city.CountryCode = country.Code 
                WHERE country.Name = %s """,
                       (selected_country,))
        cities = cursor.fetchall()
        # print(cities)
        # Введите страну: Germany
        # (('Berlin', 3386667), ('Hamburg', 1704735), ('Munich [München]', 1194560),...)

        for i, (city_name, population) in enumerate(cities, start=1):
            print(f"{i}. {city_name} - {population}")