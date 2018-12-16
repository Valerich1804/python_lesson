# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
import sys

path_dir = [('dir_' + str(i + 1)) for i in range(9)]

# Создание пустых директорий
def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)

    except:
        print(dir_path + ' - такая директория уже есть')

for i in path_dir:
    make_dir(i)
    print(i + " - Создал")


# Удаление созданых пустых поддиректорий
path_dir = [('dir_' + str(i + 1)) for i in range(9)]


def dell_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - Директория не пуста')

for i in path_dir:
    dell_dir(i)
    print(i + " - удалил")





# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

list = os.listdir()
for i in list:
    print(i)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(first_file, backup_file):
    shutil.copy(first_file, backup_file)

first_file = sys.argv[0]
backup_file = first_file + '.copy'
copy_file(first_file,backup_file)




