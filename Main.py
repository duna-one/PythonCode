import os, pathlib, sys
import DBOperations

def DBChoiceMenu():
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
    work = True
    while work:
        print('Выберите пункт меню:')
        print('1. Отображение текущего содержимого БД на экране в виде таблицы')
        print('2. Сохранение таблицы в текстовый файл с задаваемым именем')
        print('3. Добавление строки БД')
        print('4. Операции с подмножеством строк')
        print('5. Отобразить доступные БД')
        print('0. Выйти назад')
        choice = input()
        if choice == '1':
            table = DBOperations.GetTable(dbName)
            print(table)
        elif choice == '2':
            table = DBOperations.GetTable(dbName)
            SaveToFile(table)
        elif choice == '3':
            DBOperations.AddRow(dbName)
        elif choice == '4':
            pass
        elif choice == '0':
            work = False
        else:
            print('Некорректный ввод')

def ShowAvalibleDB():
    dbfiles = GetDBFiles()
    if len(dbfiles) == 0:
        print('Нет доступных БД')
    else:
        print('Доступные БД:')
        for db in dbfiles:
          print(db)
            
def GetDBFiles():
    dbfiles = []
    for file in os.listdir( pathlib.Path().absolute() ):
        if file.endswith('.sqlite'):
           dbfiles.append(file)
    return dbfiles

def SaveToFile(table):
    fileName = input('Введите имя файла: ')
    txtFile = open(fileName, 'w+')
    for row in table:
        txtFile.write(str(row))
    txtFile.close()

DBChoiceMenu()