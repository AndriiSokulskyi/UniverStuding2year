from Collection import *
from Validation import *


def rid_writ(txt, mode):
    f = Validation.file_existing(txt, mode)
    return f

menu = ''
cl = Collection()
MeM = Caretaker(cl)
MeM.backup()
while menu!= '0':
    print('0 - Завершити програму.', '\n',
          '1 - Додати до колекції.', '\n',
          '2 - Додати до колекції з файлу.', '\n',
          '3 - Додати колекцію до файлу.', '\n',
          '4 - Видалити з колекції.', '\n',
          '5 - Видалити з файлу.', '\n',
          '6 - Змінити в колекції.', '\n',
          '7 - Змінити у файлі.', '\n',
          '8 - Пошук.', '\n',
          '9 - Сортувати.', '\n',
          '10 - Назад.', '\n',
          '11 - Вперед.', '\n',
          )
    oper = input('Enter from 0 to 11: ')
    menu = ''
    if oper == '0':
        menu = oper
    while (menu != 'menu') & (menu !='0'):
        if oper == '1':
            idd = ForeignID()
            for i in range(8):
                idd.get(dictio1[i])(input(dictio[i] + ': '))
            cl.add_to_collec(idd)
            MeM.backup()
            print(cl)
        elif oper == '2':
            file = rid_writ("Text.txt", "r")
            cl.add_from_file(file)
            MeM.backup()
            file.close()
            print(cl)
        elif oper == '3':
            file = rid_writ("Text.txt", "w")
            cl.add_to_file(file)
            MeM.backup()
            file.close()
        elif oper == '4':
            iDn = input('Введіть ідентифікатор по якому треба видалити: ')
            cl.delete_from_collec(iDn)
            MeM.backup()
            print(cl)
        elif oper == '5':
            iDn = input('Введіть ідентифікатор по якому треба видалити з файлу: ')
            file = rid_writ("Text.txt", "w")
            cl.delete_from_file(file, iDn)
            MeM.backup()
            file.close()
        elif oper == '6':
            iDn = input('Введіть ідентифікатор по якому треба змінити: ')
            ed = input('Введіть значення на яке треба змінити: ')
            cl.edit_collec(iDn, ed)
            MeM.backup()
            print(cl)
        elif oper == '7':
            iDn = input('Введіть ідентифікатор по якому треба змінити: ')
            ed = input('Введіть значення на яке треба змінити: ')
            txt = input('Введіть назву файлу який треба змінити: ')
            file = rid_writ(txt, "w")
            cl.edit_file(file, iDn, ed)
            MeM.backup()
            file.close()
        elif oper == '8':
            s = input('Введіть те, що хочете знайти: ')
            print(cl.find_in_collec(s))
            MeM.backup()
        elif oper == '9':
            print(' 0 : id', '\n',
                  '1 : country_code', '\n',
                  '2 : passport_no', '\n',
                  '3 : fname','\n',
                  '4 : lname', '\n',
                  '5 : date_of_birth', '\n',
                  '6 : date_of_issue', '\n',
                  '7 : date_of_expire', '\n')
            atrb = input('Введіть атрибут за яким сортувати:')
            cl.sort_of_collec(atrb)
            MeM.backup()
            print(cl)
        elif oper == '10':
            MeM.undo()
            print(cl)
        elif oper == '11':
            MeM.redo()
            print(cl)
        menu = input('If you want to exit to menu, print "menu", if you want to continue print anything and press Enter: ')