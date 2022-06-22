from WriteFIOAGEClass import go_toPupil
from ParentData import go_toParent
from CombineSearch import combineSearch


print(  'Выберите 1,2,3: \n' +
        '1 - Ввести данные ученика \n' +
        '2 - Ввести контакт родителя \n' +
        '3 - Поиск \n')

choice = input ('==>>')
if choice == "1":
    go_toPupil()
elif choice == "2":
    go_toParent()
elif choice == "3":
    combineSearch()
