import csv
from collections import defaultdict
from itertools import chain

def combineSearch():
    with open('PupilBD.csv') as filePupil:
        reader1 = list(csv.DictReader(filePupil))
    with open('ParantBD.csv') as fileParant:
        reader2 = list(csv.DictReader(fileParant))

    data = defaultdict(dict)
    for item in chain(reader1, reader2):
        data[item['id']].update(item)
        combi = list(data.values())

    a = input('Поиск >> ')
    result = ' '
    for i in range(0, len(combi)):
        if a in combi[i].values():
            result = combi[i].items()
        print(result)