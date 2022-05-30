"""
Реализуйте алгоритм перемешивания списка.
"""

import random

my_list = [10, 9, 8, 7, 6]

print (f'Изначальный: {(my_list)}')
res = random.sample(my_list, len(my_list))
print (f'Перемешанный: {(res)}')