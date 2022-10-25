# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

def create_list():
    new_list = [int(input(f"Введите элемент {i+1} списка: ")) for i in range(int(input('Введите длину списка: ')))]
    return new_list

def elements_summ (user_list):
    prod_list = []
    l = len(user_list)
    for i in range(l//2):
        prod_list.append(user_list[i]*user_list[-i-1])
    if l % 2 != 0:
        prod_list.append(user_list[l//2]**2)
    return prod_list

try:
    new_list = create_list()
    print(f'Список: {new_list}')
    print(f'Произведение пар чисел: {elements_summ(new_list)}')
except:
    print('Вводите только целые числа')

