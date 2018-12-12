import os
import shutil
import sys


def change_dir(dir_path): # переход в заданую директорию для задания нормал
    try:
        os.chdir(dir_path)
        os.getcwd()
        print("Успешно перешел")
    except:
        print(dir_path + ' - Невозможно перейти! такой директории нет')


# Удаление заданой директории для задания нормал

def delete_dir(dir_path):
    try:
        dir_path = os.path.join(os.getcwd(), dir_path)
        os.rmdir(dir_path)
        print(dir_path + " - Успешно удалено")

    except:
        print(dir_path + ' - Невозможно удалить! такой директории нет')


# Создание директории для задания нормал

def make_dir(dir_path):
    try:
        dir_path = os.path.join(os.getcwd(), dir_path)
        os.mkdir(dir_path)
        print(dir_path + " - Успешно создал")

    except:

        print(dir_path + ' - Невозможно создать! такая директория уже есть')



# просмотр заданой директории для задания нормал

def list_dir(dir_path):
    list = os.listdir(dir_path)

    for i in list:
        print(i)