''' Task 1.  Анализ курсов студентов
Реализовать программу, которая должна:
Прочитать файл student_courses.json, содержащий:
имя,
дату рождения (birth_date) в формате дд.мм.гггг,
дату поступления (enrollment_date) в том же формате,
список курсов.
Вычислить:
Общее количество студентов.
Средний возраст на момент поступления.
Количество студентов на каждом курсе.
Сохранить отчёт в JSON-файл student_courses_report.json.
Данные:
[ {"name": "Diana Williams", "birth_date": "12.06.1983", "enrollment_date": "29.04.2023", "courses": ["Physics", "Chemistry"]},
  {"name": "Tina Miller", "birth_date": "06.07.2004", "enrollment_date": "18.04.2020", "courses": ["Biology", "Business"]},
  {"name": "Kevin Miller", "birth_date": "20.12.2004", "enrollment_date": "16.12.2020", "courses": ["Linguistics", "Math", "History"]},
  {"name": "Fiona Brown", "birth_date": "05.07.1999", "enrollment_date": "02.09.2022", "courses": ["Art", "Philosophy"]},
  {"name": "Charlie Davis", "birth_date": "17.07.1998", "enrollment_date": "17.05.2023", "courses": ["Chemistry", "Physics", "Business"]},
  {"name": "Diana Jones", "birth_date": "24.12.1980", "enrollment_date": "26.11.2021", "courses": ["Economics", "Linguistics"]},
  {"name": "Alice Johnson", "birth_date": "22.09.1981", "enrollment_date": "23.12.2020", "courses": ["Chemistry", "Economics", "Math"]},
  {"name": "Ian Lopez", "birth_date": "23.11.2001", "enrollment_date": "07.05.2020", "courses": ["Philosophy", "Art", "Physics"]},
  {"name": "Kevin Davis", "birth_date": "30.01.1997", "enrollment_date": "20.03.2021", "courses": ["Math", "Economics"]},
  ...
]

Пример вывода (student_courses_report.json):
{    "total_students": 100,
    "average_enrollment_age": 27.9,
    "students_per_course": {
        "Art": 21,
        "Biology": 18,
        "Business": 28,
        "Chemistry": 16,
        "Economics": 23,
        "History": 9,
        "Linguistics": 23,
        "Math": 23,
        "Philosophy": 19,
        "Physics": 19
    }
}
'''
import json
from datetime import  datetime
from collections import defaultdict

def calculate_age(birth_date_str: str, enrollment_day_str: str) -> int:
    """
    This function calculates a person's age at the time of enrollment.
    It checks if the birthday has already happened in the enrollment year.
    :param birth_date_str: Birth date as a string in format "dd.mm.yyyy"
    :param enrollment_day_str: Enrollment date as a string in format "dd.mm.yyyy"
    :return: Age in full years
    """
    birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")
    enrollment_day_date = datetime.strptime(enrollment_day_str, "%d.%m.%Y")
    age = enrollment_day_date.year - birth_date.year
    if (enrollment_day_date.month, enrollment_day_date.day) < (birth_date.month, birth_date.day):
       age -= 1
    return age

def analyze_students(filename: str, report_filename: str) -> None:
    """
     This function reads student data from a file, calculates:
    - total number of students,
    - average age at enrollment,
    - number of students per course.
    Then it saves the results to a new JSON file.
    :param filename: Name of the input JSON file with student data
    :param report_filename: Name of the output JSON file for the report

    :return: None
    """
    with open(filename, "r", encoding="utf-8") as file:
        students_data = json.load(file)

        total_students = len(students_data)
        #print(total_students)
        total_age = 0
        course_counts = defaultdict(int)

        for student in students_data:       # for 1 Person (student)
            #pass
            #print(student)
            age_enrollment = calculate_age(student["birth_date"], student["enrollment_date"])
            #print(age_enrollment)
            total_age += age_enrollment
            #print(total_age)

            for course in student["courses"]:
                course_counts[course] += 1  # dic
                #print(course_counts)

    avarage_age = round(total_age / total_students, 1)
    #print(avarage_age) # 27.9

    report = {
        "total_students": total_students,
        "average_enrollment_age": avarage_age,
        "students_per_course": dict(sorted(course_counts.items())) #sorted subjects
    }
    #print(report)

    with open(report_filename, "w", encoding = "utf-8") as file:
        json.dump(report, file, indent = 4, ensure_ascii = False)
    print("Analysis completed. The report has been saved to the file", report_filename)

# main cod
analyze_students("student_courses.json", "student_courses_report.json")
