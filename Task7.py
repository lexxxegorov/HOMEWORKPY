"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

"""

from random import randint

rand_list = []
for i in range(5):
    rand_list.append(randint(0, 10))
print(rand_list)


def sum_odd(new_list):
    Summa=0 
    for i in range(len(new_list)): 
        if i % 2!= 0: 
            Summa=Summa+new_list[i] 
    return Summa
print(sum_odd(rand_list))