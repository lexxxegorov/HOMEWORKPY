"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""


from random import uniform
rand_list = []
for i in range(5):
    rand_list.append(round(uniform(1, 10), 2))
print(rand_list)


def drob_part(my_list):
    numbers = [round(x - int(x), 2) for x in (my_list)]
    return max(numbers) - min(numbers)

new_list = drob_part(rand_list)
print(new_list)
