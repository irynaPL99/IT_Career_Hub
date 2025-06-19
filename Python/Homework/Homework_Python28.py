'''Task 1. План по дням недели
Напишите программу, которая помогает планировать дела.
Программа должна !!бесконечно!! выводить план на следующий день недели,
 пока пользователь нажимает 'Enter'.
Данные:
# Расписание дел на неделю
weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}
Пример ввода:
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана:
Tuesday: Meeting, Work, Study Python
...
Нажмите 'Enter' для получения плана:
Sunday: Family time, Rest
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана: q
...
'''
print("\nTask 1. План по дням недели")
def print_day_tasks() -> None:
    """
    This function shows one day of the weekly schedule each time you press Enter.
    When you press 'q', the program stops.
    It goes from Monday to Sunday and repeats.

    :return: 
    """
# Расписание дел на неделю
    weekly_schedule = {
        "Monday": ["Gym", "Work", "Read book"],
        "Tuesday": ["Meeting", "Work", "Study Python"],
        "Wednesday": ["Shopping", "Work", "Watch movie"],
        "Thursday": ["Work", "Call parents", "Play guitar"],
        "Friday": ["Work", "Dinner with friends"],
        "Saturday": ["Hiking", "Rest"],
        "Sunday": ["Family time", "Rest"]
    }
    # get the list of days = keys in dictionary
    days_list = list(weekly_schedule.keys())
    #print(days_list)

    # start with day index 0 (Monday)
    day_index = 0

    while True:
        user_input = input("\nНажмите 'Enter' для получения плана или q - для остановки программы:")

        if user_input == "":
            current_day = days_list[day_index]
            # print(current_day)
            tasks = ', '.join(weekly_schedule[current_day])
            print(f"{current_day}: {tasks}")

            # move to the next day
            # "modulo", остаток от деления.
            day_index = (day_index + 1) % len(days_list)


        elif user_input.lower() =='q':
            print ("Программа остановлена!")
            break

        else:
            print("Не верный ввод! Нажмите 'Enter' для получения плана или q - для остановки программы:")

# main code
print_day_tasks()


'''Task 2. Объединение списков продуктов
Напишите функцию, которая принимает несколько списков с названиями продуктов 
и возвращает !!!генератор!!!, содержащий все продукты в нижнем регистре.
Выведите содержимое генератора.
Данные:
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]
Пример вывода:
apple
banana
orange
carrot
tomato
cucumber
milk
cheese
yogurt
'''
print("\nTask 2. Объединение списков продуктов ")
def generate_products_lowercase(*product_lists) -> 'Generetor[str, None, None]':
    """
    This function takes multiple lists of product names.
    It returns a generator that yields all product names in lowercase.

    :param product_lists: one or more lists of product names
    :return: generator of lowercase product names
    """
    for item_sublist in product_lists:
        for item in item_sublist:
            yield item.lower() #отдаёт результат по одному, не загружая всё в память

#main code
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

for _ in generate_products_lowercase(fruits, vegetables, dairy):
    print(_)


'''Task 3. Комбинации одежды
Напишите функцию, которая принимает списки типов одежды, цветов и размеров, 
а затем генерирует все возможные комбинации
в формате "Clothe - Color - Size".
Данные:
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]
Пример вывода:
T-shirt - Red - S
T-shirt - Red - M
T-shirt - Red - L
T-shirt - Blue - S
...
Jacket - Black - L
'''
print("\nTask 3. Комбинации одежды")
import itertools

def generate_combinations(clothes: list, colors: list, sizes: list) -> 'Generator[str, None, None]':
    """
    Generates clothing combinations in format 'Clothe - Color - Size'.

    :param clothes: List of clothing items
    :param colors: List of colors
    :param sizes: List of sizes
    :yield: A string like "T-shirt - Red - S"
    """
    for clothe, color, size in itertools.product(clothes, colors, sizes):
        yield f"{clothe} - {color} - {size}"

# main code
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

#print("Комбинации одежды:")
for combo in generate_combinations(clothes, colors, sizes):
    print(combo)