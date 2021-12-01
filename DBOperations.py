import sqlite3
from sqlite3.dbapi2 import Row
import time

def CreateDB(dbName):
    """Создание БД"""
    if not str(dbName).endswith('.sqlite'):
        dbName = dbName + '.sqlite'

    con = sqlite3.connect(dbName)
    cur = con.cursor()

    sql = """\
    CREATE TABLE main (code TEXT,
    subject TEXT,
    sem_number INTEGER,
    type_of_cert TEXT,
    date_of_cert DATE,
    prof_fio TEXT,
    prof_pos TEXT,
    mark INTEGER,
    date_of_update DATE);
    """
    cur.execute(sql)

    cur.close()
    con.close()


def AddRow(dbName):
    """Добавление строки в БД"""
    if not str(dbName).endswith('.sqlite'):
        dbName = dbName + '.sqlite'

    code = input('Введите код дисциплины по учебному плану: ')
    
    subject = input('Введите название дисциплины: ')
    
    while True:
        try:
            sem_number = int(input('Введите номер семестра с аттестацией по дисциплине: '))
            break
        except:
            print('Номер семестра должен быть числом')
    
    while True:
        type_of_cert = input('Введите тип аттестации (экзамен/зачет): ')
        if str(type_of_cert).lower() == 'экзамен' or str(type_of_cert).lower() == 'зачет':
            break
        else:
            print('Тип аттестации может быть либо экзамен, либо зачет') 
            
    while True:
        try:
            date_of_cert = input('Введите дату аттестации (в формате ДД-ММ-ГГГГ): ')
            time.strptime(date_of_cert, '%d-%m-%Y')
            break
        except:
            print('Некорректный ввод')
    
    prof_fio = input('Введите ФИО преподавателя, проводившего аттестацию: ')
    
    prof_pos = input('Введите должность преподавателя: ')

    while True:
        try:
            mark = int(input('Введите полученную оценку: '))

            if (mark < 0 or mark > 5):
                print('Неверная оценка! Оценка должна находиться в диапазоне от 0 до 5!')
            else:
                break
       except:
            print('Оценка должна быть числом')
        
    dat = time.localtime()
    date_of_update = '{:0>2}-{:0>2}-{:0>4}'.format(str(dat.tm_mday), str(dat.tm_mon), str(dat.tm_year))

    new_data = (code, subject, sem_number, type_of_cert, date_of_cert, prof_fio, prof_pos, mark, date_of_update)

    con = sqlite3.connect(dbName)
    cur = con.cursor()

    sql = """\
    INSERT INTO main 
    (code, subject, sem_number, type_of_cert, date_of_cert, prof_fio, prof_pos, mark, date_of_update) 
    VALUES (?,?,?,?,?,?,?,?,?)"""

    cur.execute(sql, new_data)

    con.commit()

    cur.close()
    con.close()


def GetTable(dbName):
    """Получение таблицы(содержимого) из бд"""
    if not str(dbName).endswith('.sqlite'):
        dbName = dbName + '.sqlite'

    con = sqlite3.connect(dbName)
    cur = con.cursor()

    sql = """\
    SELECT * FROM main
    """
    tableData = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    return tableData


def GetColumsNames(dbName):
    """Получение имен столбцов таблицы из бд"""
    if not str(dbName).endswith('.sqlite'):
        dbName = dbName + '.sqlite'

    con = sqlite3.connect(dbName)
    cur = con.cursor()

    sql = """\
    SELECT * FROM main
    """
    columns = cur.execute(sql).description

    columnNames = []
    for column in columns:
        columnNames.append(column[0])

    cur.close()
    con.close()

    return columnNames

def DelRows(dbName, rule):
    """Удаляет строки по указанному условию"""
    if not str(dbName).endswith('.sqlite'):
        dbName = dbName + '.sqlite'

    con = sqlite3.connect(dbName)
    cur = con.cursor()

    sql = """\
    DELETE FROM main WHERE {0}
    """.format(rule)
    cur.execute(sql)

    con.commit()
    cur.close()
    con.close()

def ChangeValue(dbName, value, rule):
    """Изменяет значения в указанном столбце по указанному правилу"""
    if not str(dbName).endswith('.sqlite'):
        dbName = dbName + '.sqlite'

    con = sqlite3.connect(dbName)
    cur = con.cursor()

    sql = """\
    UPDATE main SET {0} WHERE {1}
    """.format(value, rule)
    cur.execute(sql)

    con.commit()
    cur.close()
    con.close()


def GetRowsByRule(dbName, rule):
    """Выводит строки по указанному правилу(фильтру)"""
    if not str(dbName).endswith('.sqlite'):
        dbName = dbName + '.sqlite'

    con = sqlite3.connect(dbName)
    cur = con.cursor()

    sql = """\
    SELECT * FROM main WHERE {0}
    """.format(rule)
    rows =  cur.execute(sql).fetchall()

    cur.close()
    con.close()

    return rows
