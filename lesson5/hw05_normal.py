# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import easy


menu_inp ='a'
while menu_inp != '0':
    print('Перейти в папку - выбрать 1')
    print('Просмотреть содержимое текущей папки - выбрать 2')
    print('Удалить папку - выбрать 3')
    print('Создать папку - выбрать 4')
    print('для выхода - выбрать 0')
    menu_inp = input('Выбрать: ' )
    print(menu_inp)
    if menu_inp == '1':
        dir_name = input ('наберите полный путь папки: ')
        easy.change_dir(dir_name)
    elif menu_inp == '2':
        dir_name = os.getcwd()
        easy.list_dir(dir_name)
    elif menu_inp == '3':
        dir_name = input('наберите полный путь папки: ')
        easy.delete_dir(dir_name)
    elif menu_inp == '4':
        dir_name = input('наберите полный путь папки: ')
        easy.make_dir(dir_name)
    elif menu_inp == '0':
        pass
    else:
        print('Такого пункта меню нет')