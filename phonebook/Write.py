
def go_tofile():
    name = input ('Введите имя ')
    surname = input ('Введите фамилию ')
    tel = input ('Введите телефон ')
    comment = input ('Введите коментарии ') 
    with open ('BD1.txt', 'a+', encoding='utf-8') as file:
        file.write(', '.join([name, surname, tel, comment])+ '\n')
