# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def create_list():
    new_list = [randint(0,10) for _ in range(int(input('Введите длину списка: ')))]
    return new_list

def summ_elements (user_list):
    sum = 0
    for i in range(len(user_list)):
        if i % 2 == 0:
            sum += user_list[i]
    return sum

try:
    you_list = create_list()
    print(you_list)
    print(f'Сумма элементов на нечетных позициях в списке равна: {summ_elements(you_list)}')
except:
    print('Вводите только целые числа')