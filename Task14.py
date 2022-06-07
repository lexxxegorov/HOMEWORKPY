"""
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
"""
from random import randint

def new_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def unic_value(new_list):
    return [i for i in set(new_list)]

size = 10
m = 1
n = 10

origin = new_list(size, m, n)
print(origin)
print(unic_value(origin))
