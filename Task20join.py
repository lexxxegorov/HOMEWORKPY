

from itertools import groupby
with open('Task20.txt', 'r') as data:
    new_text = data.read()
print(new_text)

def encode_rle(n_text):
    str_code = ''.join(['{}{}'.format(sum(1 for _ in k), g) for g, k in groupby(n_text)])
    return str_code

str_code = encode_rle(new_text)
print(str_code)

with open('Task20RLE.txt', 'w') as data:
    data.write(str_code)


