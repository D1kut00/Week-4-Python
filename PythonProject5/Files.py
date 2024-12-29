# Задача 1 и 2
file = open("Task3/Mirzanov_Temirlan.txt", "w+")
file.write("Mirzanov Temirlan")
file.seek(0)
print(file.read())

# Задача 3
import os


def categorize_files(directory):
    text_files = []
    other_files = []

    # Итерация по файлам в директории
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Проверка, является ли объект файлом (а не директорией)
        if os.path.isfile(file_path):
            if filename.endswith(".txt"):
                text_files.append(filename)
            else:
                other_files.append(filename)

    return text_files, other_files


# Указание директории для поиска
directory = "Task3"

# Убедиться, что директория существует
if not os.path.exists(directory):
    os.makedirs(directory)

# Создание текстового файла для демонстрации
sample_file_path = os.path.join(directory, "Mirzanov_Temirlan.txt")
with open(sample_file_path, "w") as sample_file:
    sample_file.write("Mirzanov Temirlan")

# Классификация файлов
text_files, other_files = categorize_files(directory)

# Печать классифицированных файлов
print("Text Files:", text_files)
print("Other Files:", other_files)


# Задача 4
# Функция для чтения данных из CSV-файла
def read_csv(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()

    # Разделение на заголовок и данные
    header = lines[0].strip().split(",")
    data = [line.strip().split(",") for line in lines[1:]]

    return header, data


# Путь к файлу AAPL.csv
file_path = r"C:\Users\mrzte\Downloads\AAPL.csv"

# Чтение данных из AAPL.csv
header, data = read_csv(file_path)

# Печать заголовка и первых 5 строк данных
print("Header:", header)
print("First 5 rows of data:")
for row in data[:5]:
    print(row)

# Задача 5
print("Column Date: ")
for i in range(5):
    for j in range(1):
        print(data[i][j])

# Задача 6
# Функция для поиска записи по дате
import csv


def search_record_by_date(file_path, search_date):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"] == search_date:
                return row
    return None


# Ввод пользователем даты для поиска
search_date = input("Enter the date (YYYY-MM-DD) to search: ")

# Поиск и отображение записи
record = search_record_by_date(file_path, search_date)
if record:
    print("Record found:")
    print(record)
else:
    print("No record found for the given date.")

# Задача 7
for i in range(5):
    for j in range(1):
        print(data[i][j])
    print(i)

# Задача 8
# Запрос ввода данных для CSV-файла
filename = "Student.csv"
data = []

# Сбор заголовка и записей от пользователя
header = input("Enter the header (comma-separated): ").split(",")
data.append(header)

while True:
    record = input("Enter a record (comma-separated) or type 'done' to finish: ")
    if record.lower() == 'done':
        break
    data.append(record.split(","))

# Запись данных в CSV-файл
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully.")

# Задача 9
# Преобразование JSON-данных в Python-объект
import json

json_string = '''
    {
        "students": [
        {
        "name": "Alice",
            "age": 25,
            "city": "London"
        },
        {
            "name": "Bob",
            "age": 30,
            "city": "New York"
        }
        ]
    }
'''

# Пример JSON-данных
example_json = '''
    {
        "students": [
        {
        "name": "Alice",
            "age": 25,
            "city": "London"
        },
        {
            "name": "Bob",
            "age": 30,
            "city": "New York"
        }
        ]
    }
'''
example_python_obj = {"name": "Alice", "age": 25, "city": "London"}


def json_to_python(json_data):
    return json.loads(json_data)


python_obj = json_to_python(example_json)
print("Task 9 - Python Object:", python_obj)


# Задача 10
# Преобразование Python-объекта в JSON-данные
def python_to_json(py_obj):
    return json.dumps(py_obj)


json_data = python_to_json(example_python_obj)
print("Task 10 - JSON Data:", json_data)


# Задача 11
# Преобразование Python-объектов в JSON-строки и их печать
def python_objects_to_json(py_objs):
    json_strings = [json.dumps(obj) for obj in py_objs]
    print("JSON Strings:")
    for json_str in json_strings:
        print(json_str)


print("Task 11 - JSON Strings:")
python_objects_to_json([example_python_obj, python_obj])


# Задача 12
# Преобразование словаря Python в отсортированные JSON-данные с отступами
def dict_to_sorted_json(py_dict):
    return json.dumps(py_dict, indent=4, sort_keys=True)


sorted_json = dict_to_sorted_json(example_python_obj)
print("Task 12 - Sorted JSON with Indentation:")
print(sorted_json)