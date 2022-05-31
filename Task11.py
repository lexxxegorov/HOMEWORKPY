"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

def fib(n: int) -> list:
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    elif n == 2:
        return[0, 1, 1]

    li = fib(n-1)
    li.append(li[-1] + li[-2])
    return li

def recurcive_fib(n):
    fib_list = fib(n)
    negative_fib_list = []
    for i in range (1, len(fib_list)):
        if i % 2 == 0:
            negative_fib_list.append(fib_list[i] * -1)
        else:
            negative_fib_list.append(fib_list[i])
    return negative_fib_list[::-1] + fib_list

print(recurcive_fib(8))