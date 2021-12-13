import os, pathlib, sys
import DBOperations


def DBChoiceMenu():
    """Меню выбора базы данных"""
    while True:
        print('Выберите пункт меню:')
        print('1. Создать новую БД')
        print('2. Выбрать существующюю БД')
        print('3. Отобразить доступные БД')
        print('0. Закрыть программу')
        choice = input()
        if choice == '1':
            dbName = input('Введите имя БД: ')
            DBOperations.CreateDB(dbName)
            print('База данных создана')
        elif choice == '2':
            dbName = input('Введите имя БД: ')
            if not dbName.endswith('.sqlite'):
                dbName = dbName + '.sqlite'
            if not os.path.exists(dbName):
                print('Указанной БД не существует!')
            else:
                WorkWithDBMenu(dbName)
        elif choice == '3':
            ShowAvalibleDB()
        elif choice == '0':
            sys.exit()
        else:
            print('Некорректный ввод')

def WorkWithDBMenu(dbName):
    """Меню работы с базой данных"""
    work = True
    while work:
        print('Выберите пункт меню:')
        print('1. Отображение текущего содержимого БД на экране в виде таблицы')
        print('2. Сохранение таблицы в текстовый файл с задаваемым именем')
        print('3. Добавление строки БД')
        print('4. Операции с подмножеством строк')
        print('5. Отобразить строки по определенному условию')
        print('0. Выйти назад')
        choice = input()
        if choice == '1':
             ShowRows(DBOperations.GetTable(dbName))
        elif choice == '2':            
            SaveToFile(dbName)
        elif choice == '3':
            DBOperations.AddRow(dbName)
        elif choice == '4':
            RowOperationsMenu(dbName)
        elif choice == '5':
            print('Столбцы таблицы:', DBOperations.GetColumsNames(dbName))
            rule = input('Введите условие отбора строк(например <имястолбца> = \'13\'): ')
            ShowRows(DBOperations.GetRowsByRule(dbName, rule))
        elif choice == '0':
            work = False
        else:
            print('Некорректный ввод')

def RowOperationsMenu(dbName):
    """Операции со строками"""
    work = True
    while work:
        print('Выберите пункт меню:')
        print('1. Удалить строку из БД')
        print('2. Заменить значение на заданное')
        print('0. Выйти назад')
        choice = input()
        if choice == '1':
            print('Столбцы таблицы:', DBOperations.GetColumsNames(dbName))
            rule = input('Введите условие удаления строки: ')
            DBOperations.DelRows(dbName, rule)
            ShowRows(DBOperations.GetTable(dbName))
        elif choice == '2':            
            print('Столбцы таблицы:', DBOperations.GetColumsNames(dbName))
            value = input('Введите новое значение <имя столбца> = <значение>: ')
            rule = input('Введите условие для замены: ')
            DBOperations.ChangeValue(dbName, value, rule)
            ShowRows(DBOperations.GetTable(dbName))
        elif choice == '0':
            work = False
        else:
            print('Некорректный ввод')


def ShowAvalibleDB():
    """Вывод всех доступных баз данных на экран"""
    dbfiles = GetDBFiles()
    if len(dbfiles) == 0:
        print('Нет доступных БД')
    else:
        print('Доступные БД:') 
        for db in dbfiles:
          print(db)
  

def GetDBFiles():
    """Возвращает список всех доступных баз данных"""
    dbfiles = []
    for file in os.listdir( pathlib.Path().absolute() ):
        if file.endswith('.sqlite'):
           dbfiles.append(file)
    return dbfiles


def SaveToFile(dbName):
    """Сохраняет таблицу из БД в текстовый файл"""
    table = DBOperations.GetTable(dbName)
    fileName = input('Введите имя файла: ')
    txtFile = open(fileName, 'w+')
    for row in table:
        txtFile.write(str(row))
    txtFile.close()


def ShowRows(rows):
    """Выводит полученные строки на экран"""
    for row in rows:
        print(row)

DBChoiceMenu()
