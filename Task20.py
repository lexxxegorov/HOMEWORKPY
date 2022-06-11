"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.

"""
"""
with open('Task20.txt', 'r') as data:
    new_text = data.read()
print(new_text)


def encode_rle(n_text):
    str_code = ''
    prev_letter = ''
    count = 1
    if not n_text:
        return ('')
    for letter in n_text:
        if letter != prev_letter:
            if prev_letter:
                str_code += str(count) + prev_letter
            count = 1
            prev_letter = letter
        else:
            count+=1
    else:
        str_code += str(count) + prev_letter
        
    return str_code


str_code = encode_rle(new_text)
print(str_code)

with open('Task20RLE.txt', 'w') as data:
    data.write(str_code)

"""

with open ('Task20RLE.txt', 'r') as data:
    new_text2 = data.read()

def decoding_rle(n_text:str):
    count = ''
    str_decode = ''
    for letter in n_text:
        if letter.isdigit():
            count += letter
        else:
            str_decode += letter * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(new_text2)
print(str_decode)

with open('Task20.txt', 'a') as data:
    data.write(f'\n{str_decode}')