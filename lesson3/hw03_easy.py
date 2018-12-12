# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

from math import *


def my_round(number, ndigits):
    return round(number, ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):

    lst_numbers = tuple(str(ticket_number))

    if len(lst_numbers) != 6:
        return False

    left_part = rigth_part = 0

    for i in range(len(lst_numbers)):
        if int(i) < 3:
            left_part += int(lst_numbers[i])
        else:
            rigth_part += int(lst_numbers[i])

    if left_part == rigth_part:
        return True
    else:
        return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436753))
