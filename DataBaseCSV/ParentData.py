import csv

def go_toParent():
    id = input ('Введите уникальный номер ученика ')
    parentName = input ('Введите имя родителя ')
    parentTel = input ('Введите телефон родителя ')


    parentInfo = dict(id=id, parentName=parentName, parentTel = parentTel )

    with open('ParantBD.csv', 'a') as data:
        fieldnames = ['id', 'parentName', 'parentTel']
        writer = csv.DictWriter(data, fieldnames=fieldnames)
        writer.writerow(parentInfo)