"""
Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
степени пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0
"""
import random
from functools import reduce
import re

def get_polynom(degree):
    polynom_str = ''
    for n in range(degree, 0, -1):
        a = random.randit(0, 100)
        if a != 0:
            if n == degree and n != 1:
                polynom_str += str(a) + 'x^'+ str(n)
            elif n == degree and n == 1:
                polynom_str += str(a) + 'x'
            elif n == 1:
                polynom_str += ' + ' + str(a) + 'x'
            else:
                polynom_str += ' + ' + str(a) + 'x^' + str(n)
    return polynom_str + ' = 0'

def normalize_polynom(polynom_str):
    polynom_str = re.sub(r'\b0x\^\d+ \+ ', r'', polynom_str)
    polynom_str = re.sub(r'\b1x\^(\d+)', r'x\^1', polynom_str)
    polynom_str = re.sub(r'(\d+)x\^1', r'\1x', polynom_str)
    polynom_str = re.sub(r'(\d+)x\^0', r'\1', polynom_str)
    return polynom_str

def get_polynom_x(degree):
    polynom_list = [str(random.randint(0,100)) + 'x^' + str(n) + ' + ' for n in range(degree, -1, -1)]
    polynom_str = reduce(lambda x, y: x + y, polynom_list)
    polynom_str = normalize_polynom(polynom_str)
    return polynom_str[: -3] + ' = 0'

k = 4
polynom = get_polynom_x(k)
print(f'Полином степени {k}: {polynom}')

with open('Task15.txt', 'w') as data:
    data.write(polynom)
