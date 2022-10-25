# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def to_binary_system(number):
    result = ''
    while number > 0:
        result += str(number % 2)
        number = number // 2
    return result[::-1]

try:
    x = int(input('Введите число: '))
    print(f'В двоичной системе: {to_binary_system(x)}')
except:
    print('Вводите только целые числа')