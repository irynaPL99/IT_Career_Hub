'''Task 1. Класс Person
Создайте класс Person, представляющий человека.
Каждый человек должен иметь имя.
Добавьте метод introduce(), который выводит приветствие с именем.

Task 2. Класс Student
На основе класса Person создайте класс Student.
Студент должен иметь имя и номер курса.
Метод introduce() должен сначала выводить базовое приветствие, а затем строку: I'm on course <номер_курса>.


Task 3. Класс Teacher и список людей
На основе класса Person создайте класс Teacher.
У преподавателя есть имя и предмет.

Метод introduce() должен выводить имя и предмет.
Метод introduce() должен выводить строку: Hello, I am professor <имя>. My subject is <предмет>.

Создайте список, в котором будут Student и Teacher,
и вызовите у всех метод introduce().
'''

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hallo, my name is {self.name}.")


    def __str__(self):
        return f"Person info: name: {self.name}"

# Подкласс Student
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)  # наследовать свойство от родителя
        self.course = course

    def introduce(self):
        super().introduce()     # наследовать metod от родителя
        print(f"I'm on course {self.course}.")

    def __str__(self):
        return f"Person info: name {self.name}, course {self.course} "

# Подкласс Teacher
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # наследовать свойство от родителя
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}.")
        print(f"My subject is {self.subject}.")

    def __str__(self):
        return f"Person info: name {self.name}, subject {self.subject} "

#persons = [Person("Alica"), Person("Bob")]
#for person in persons:
#    print(person)

#students = [Student("Alica", 2), Student("Bob", 3)]
#for student in students:
#    print(student)
#    student.introduce()
#    print()

#teacher = Teacher("Mike", "Mathematics")
#print(teacher)

people = [
    Student("Alice", 2),
    Teacher("Dr. Smith", "Mathematics"),
    Student("Bob", 3),
    Teacher("Ms. Green", "Biology")
]

for p in people:
    p.introduce()
