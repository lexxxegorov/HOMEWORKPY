import csv
def go_tofile():
    name = input ('Введите имя ').strip()
    surname = input ('Введите фамилию ').strip()
    tel = input ('Введите телефон ').strip()
    comment = input ('Введите коментарии ').strip()

    contactInfo = dict(name=name, surname=surname, tel=tel, comment=comment)

    with open('BD2.csv', 'a', newline='') as data:
        fieldnames = ['name', 'surname', 'tel', 'comment']
        writer = csv.DictWriter(data, fieldnames=fieldnames, delimiter="\n")
        writer.writerow(contactInfo)
