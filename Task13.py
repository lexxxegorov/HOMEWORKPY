"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""
n=50
div=2
primes = []

while n > 1:
    while n%div ==0:
        primes.append(div)
        n/=div
    div+=1

print (primes)