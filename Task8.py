"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый 
и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

from random import randint

rand_list = []
for i in range(5):
    rand_list.append(randint(0, 10))
print(rand_list)


def multiply(new_list):
    for i in range (len(new_list)):
        return (new_list[i]*new_list[len(new_list)-1], 
                new_list[i+1]*new_list[len(new_list)-2],
                new_list[i+2]*new_list[len(new_list)-3]
                )

multi_list = multiply(rand_list)
print(multi_list)




