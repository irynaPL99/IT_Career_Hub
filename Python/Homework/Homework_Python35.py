'''Task 1. Счётчик экземпляров
Создайте класс User, представляющий пользователя.
При создании должны указываться логин (username) и пароль (password).
У класса должно быть поле total_users, хранящее общее количество
созданных пользователей.
При каждом создании нового объекта User, счётчик должен увеличиваться.
Добавьте метод get_total(), возвращающий количество пользователей.
Проверьте, что счётчик работает.
'''

'''Task 2. Проверка данных пользователя
Доработайте класс User.
Добавьте валидации полей при создании.
Имя должно быть непустой строкой.
Пароль должен быть строкой длиной не менее 5 символов.
Если данные некорректны — выбрасывайте ValueError.
Добавьте строковое представление объекта.
Проверьте работу класса с разными значениями.
'''
print("Task 1. Счётчик экземпляров. \nTask 2. Проверка данных пользователя")
class User:
    total_users = 0 #Класс-переменная: общее количество пользователей
    def __init__(self, username: str, password: str):
        # валидация полей при создании.
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Имя пользователя должно быть непустой строкой.")

        if not isinstance(password,str) or len(password) < 5:
            raise ValueError("Пароль должен быть строкой не менее 5 символов.")





        self.username = username
        self.password = password

        User.total_users += 1 # общее количество пользователей

    # метод get_total(), возвращающий количество пользователей
    def get_total(self):
        return User.total_users

 # Строковое представление: (username: Alice, password: 1234, num: 1)
    def __str__(self):
           # return f"User info: {self.username}, password: {self.password}, num: {self.get_total()}"
           return f"User: {self.username}"


# def __repr__(self):
    #     return f"User info_repr: {self.username}, password: {self.password}, num: {self.get_total()}"


user1 = User("alice","secret")
print(user1)
user2 = User("bob","qwe")
print(user2)
print(f"Total users: {user2.get_total()}")

