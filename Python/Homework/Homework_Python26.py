'''Task 1. Список файлов и папок
Напишите программу, которая принимает путь к директории через аргумент
командной строки и выводит:
Отдельно список папок
Отдельно список файлов
Пример запуска
python script.py /home/user/documents
Пример вывода
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2
Файлы:
- file1.txt
- file2.txt
- notes.docx

print("\nTask 1. Список файлов и папок")
import os
import sys
from typing import List

def read_directory(path: str) -> List[str]:
    if not os.path.exists(path):
        print(f"This path: {path} is not exists")
        return

    dir_list = []
    file_list = []
    for item in os.listdir(path):
        path_full = os.path.join(path,item)
        if os.path.isdir(path_full):
            dir_list.append(item)
        elif os.path.isfile(path_full):
            file_list.append(item)
    print(f"Содержимое директории '{path}':")

    print("Папки:")
    for dir in sorted(dir_list):
        print(f"- {dir}")

    print("Файлы:")
    for file in sorted(file_list):
        print(f"- {file}")

if len(sys.argv) != 2:
    print("Использование: python Homework_Python26.py <путь_к_директории>")
    sys.exit(1)
else:
        path = sys.argv[1]
        read_directory(path)
'''

'''Task 2. Поиск и удаление файлов с указанным расширением
Напишите программу, которая:
Принимает путь к директории и расширение файлов через аргумент командной строки.
Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
Спрашивает у пользователя, хочет ли он удалить найденные файлы.
Если пользователь подтверждает, удаляет их.
Пример запуска:
python script.py /home/user/PycharmProjects/project1 .log
Пример вывода
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log
Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.
'''
print("\nTask 2. Поиск и удаление файлов с указанным расширением")
import os
import sys
from typing import List

#print("Текущая рабочая директория:", os.getcwd())
def filter_files(path: str, extension: str) -> List[str]:
    """
       Recursively searches for files with the specified extension 
       in the given directory and all its subdirectories.

       Args:
           path (str): Path to the directory to search in.
           extension (str): File extension to search for (e.g., ".log").

       Returns:
           List[str]: A list of full file paths matching the given extension.
    """
    list_files = []
    normalized_path = os.path.normpath(path)  # !! Нормализация пути (кросс-платформенно)
    for root, dirs, files in os.walk(normalized_path): # : root -Текущая директория, dirs - Поддиректории
        #print(f"[DEBUG] Текущая папка: {root}")  # Отладка
        for file in files:
            if file.endswith(extension):
                path_full = os.path.join(root, file)
                list_files.append(path_full) # ← для удаления
                # Получаем относительный путь от корневой директории path
                # os.path.relpath(path_full, path) - возвращает путь от path до path_full, то есть убирает начальный каталог.
                #relative_path = os.path.relpath(path_full, path)
                #list_files.append(relative_path)
    return list_files

def confirm_delete_files(list_files: List[str], extension: str, path_dir: str) -> None:
    """
        Asks the user for confirmation before deleting files.

        Args:
            list_files (List[str]): A list of file paths to be deleted.
    """

    if not list_files:
        print(f"No files with this extension: {extension}")
        sys.exit(0) # завершение без ошибки (0), если файлов нет

    print(f"Найдены файлы с расширением '{extension}':")
    for file in list_files:
        # print(f"- {file}") # не красивый вывод
        #normalized = os.path.normpath(file) # Приводит путь к стандартному виду для текущей ОС
        # print("-", normalized.replace("\\", "/"))

        # Показ относительного пути с нормализованными прямыми слешами
        # os.path.relpath - Получение пути относительно переданной директории
        relative_path = os.path.relpath(file, path_dir)
        print("-", relative_path.replace("\\", "/"))



    while True:
        input_user = input("Вы хотите удалить эти файлы? (y/n):").strip().lower()
        # strip() — удаляет пробелы и переходы строк
        if input_user == 'y':
            for file in list_files:
                try:
                    os.remove(file)
                except Exception as e:
                    print(f"Ошибка удаления {file}: {e}")
            print("Удаление завершено.")
            break
        elif input_user== 'n':
            print("Удаление не подтверждено.")
            break
        else:
            print("Пожалуйста, введите 'y' (да) или 'n' (нет).")

# main code
if len(sys.argv) != 3:
    print("Использование: python Homework_Python26.py <путь_к_директории> <.расширение файла>")
    #print("<путь_к_директории> - в Windows используй кавычки или / (прямой слэш)")
    sys.exit(1)

else:
    imput_path = sys.argv[1]
    path = os.path.normpath(imput_path)  # !! Нормализуем ввод с любыми слешами
    #print(f"Ищу в каталоге: {path}") # для отладки
    extension = sys.argv[2]
    if not os.path.isdir(path):
        print(f"This path is not a directory: {path}")
        sys.exit(1)

    list_files_to_delete = filter_files(path, extension)
    confirm_delete_files(list_files_to_delete,extension,path)
