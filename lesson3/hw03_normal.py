# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print(40*'=','\nЗадание-1:\n')

from math import*

def fibonacci(n, m):
    if n <=0: return "N должно быть больше 0!"
    if n > m: return
    if m < 4 and n < 3: return [1, 1, 2]

    fib = list()
    while n <= m:
        phi = (sqrt(5) + 1) / 2
        fib.append(int(phi ** n / sqrt(5) + 0.5))
        n += 1

    return fib


print(fibonacci(3, 20))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print(40*'=','\nЗадание-2:\n')

def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(len(origin_list) - 1, i, -1):
            if origin_list[j] < origin_list[j - 1]:
                origin_list[j], origin_list[j - 1] = origin_list[j - 1], origin_list[j]

    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


def sort_to_max(origin_list):
    result = list()
    while origin_list:
        result.append(min(origin_list))
        origin_list.remove(min(origin_list))

    return result

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print(40*'=','\nЗадание-3:\n')

def filter_function(x):
    result = list()
    for i in range(len(x)):
        if x[i] % 2 == 0: result.append(x[i])

    return result
'''функция фильтрует только четные числа'''

print(filter_function([162, 32, 43, 2, 15, -42]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


print(40*'=','\nЗадание-4:\n')

from math import*
A1, A2, A3, A4 = (2, 3), (0, 2), (4, 1), (6, 2)


def parall(a, b, c, d):

    p1 = False
    p2 = False

    ab = sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    cb = sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    if ab == cd and cb == ad:
        print('Равенство сторон: верно')
        p1 = True
    else:
        print('Противоположные стороны НЕ равны')

    hO1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    hO2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)
    if hO1 == hO2:
        print('Равенство половин диагоналей: верно')
        p2 = True
    else:
        print('Половины диагоналей НЕ равны')

    if p1 and p2:
        print('Вершины A1%s, A2%s, A3%s, A4%s\nобразуют параллелограмм' % (a, b, c, d))
    else:
        print('Вершины не образуют параллелограмм')

parall(A1, A2, A3, A4)