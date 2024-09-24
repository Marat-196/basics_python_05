# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def path_to_file(txt: str):
    *path, other = txt.split("/")
    name, ext = other.split(".")
    return path, name, ext


link = 'C:/Users/admin/Documents/GeekBrains/II год обучения Data Engineer/Основы Python/seminar_05/task_02.py'

result = path_to_file(link)

print(f'path = {"/".join(result[0])}\nname = {result[1]}\next = {result[2]}')
