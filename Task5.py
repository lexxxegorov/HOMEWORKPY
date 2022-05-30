"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

Пример:

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""

from msilib import sequence

n = int(input('Введите число: ')) 

def get_squerence(n):
    return [round((1 + 1 / n)**n, 5) for n in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))
