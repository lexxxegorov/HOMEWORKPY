import csv

def get_fromfile():
    with open('BD2.csv', newline='') as file:
        reader = list(csv.DictReader(file))
        search = input('Поиск >> ')
        result = ' '
        for i in range(0, len(reader)):
            if search in reader[i].values():
                result = reader[i].items()
            print(result)