def get_fromfile():
    with open('BD1.txt', 'r', encoding='utf-8') as file:
        name = input('Поиск >> ')
        for line in file:
            if name in line:
                print (line)

