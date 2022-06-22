import csv
def go_toPupil():
    id = input ('Введите уникальный номер ')
    name = input ('Введите имя ')
    surname = input ('Введите фамилию ')
    clas = input ('Введите класс ученика ')
    performance = input ('Введите степень успеваимости ')

    pupilInfo = dict(id=id, name=name, surname=surname, clas=clas, performance=performance)

    with open('PupilBD.csv', 'a') as data:
        fieldnames = ['id', 'name', 'surname', 'clas', 'performance']
        writer = csv.DictWriter(data, fieldnames=fieldnames)
        writer.writerow(pupilInfo)