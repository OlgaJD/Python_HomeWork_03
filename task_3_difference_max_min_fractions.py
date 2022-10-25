# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def create_list():
    new_list = [float(input(f"Введите элемент {i+1} спика: ")) for i in range(int(input('Введите длину списка: ')))]
    return new_list

def fraction_max_min(user_list):
    temp_list = []
    for i in user_list:
        if i % 1 != 0:
            temp_list.append(i % 1)
    result = round(max(temp_list)-min(temp_list), 5)
    return result

try: print(f'Разница между максимальным и минимальным значением дробной части равна: {fraction_max_min(create_list())}')
except: print('Не используйте буквы и символы, длина списка должна быть целым числом.')