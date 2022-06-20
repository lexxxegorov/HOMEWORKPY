from Search import get_fromfile
from Write import go_tofile

user_request =  input('Записать контакт ? ')
if user_request == 'yes':
    go_tofile()
elif user_request == 'no':
    user_request = input('Поиск контакта ? ')
    if user_request == 'yes':
        get_fromfile()
    elif user_request == 'no':
        input('Записать контакт ? ')