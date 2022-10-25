# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(number):
    if number in (1, 2):
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

def fibonacci_list(number):
    result = [0,]
    for i in range(1, n + 1):
        result.append(fibonacci(i))
        result.insert(0,(-1)**(i + 1)*(fibonacci(i)))
    return result


n = int(input('Введите число: '))
print(fibonacci_list(fibonacci(n)))