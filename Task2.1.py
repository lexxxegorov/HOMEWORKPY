"""
Напишите программу для. 
проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""
table = [
    [False, False, False],
    [False, False, True],
    [False, True, False],
    [True, False, False],
    [False, True, True],
    [True, True, True],
    [True, False, True],
    [True, True, False],
]



result = True
for i in table:
    if not(not(i[0] or i[1] or i[2])) == (not i[0] and not i[1] and not i[2]):
        result = False
print (result)