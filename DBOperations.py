import sqlite3
import time

def CreateDB(dbName):
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
    if not str(dbName).endswith('.sqlite'):
        dbName = dbName + '.sqlite'

    code = input('Введите код дисциплины по учебному плану: ')
    
    subject = input('Введите название дисциплины: ')
    
    sem_number = int(input('Введите номер семестра с аттестацией по дисциплине: '))
    
    type_of_cert = input('Введите тип аттестации (экзамен/зачет): ')
    
    date_of_cert = input('Введите дату аттестации (в формате ДД-ММ-ГГГГ): ')    
    
    prof_fio = input('Введите ФИО преподавателя, проводившего аттестацию: ')
    
    prof_pos = input('Введите должность преподавателя: ')

    while True:
        mark = int(input('Введите полученную оценку: '))

        if (mark < 0 or mark > 5):
            print('Неверная оценка! Оценка должна находиться в диапазоне от 0 до 5!')
        else:
            break

    # Получение даты занесения записи
    dat = time.localtime()
    date_of_update = '{:0>2}-{:0>2}-{:0>4}'.format(str(dat.tm_mday), str(dat.tm_mon), str(dat.tm_year))

    # Создание кортежа с данными для занесения в таблицу
    new_data = (code, subject, sem_number, type_of_cert, date_of_cert, prof_fio, prof_pos, mark, date_of_update)

    # Открытие БД
    con = sqlite3.connect(dbName)

    # Создание курсора
    cur = con.cursor()

    # Формирование строки с SQL-запросом
    sql = """\
    INSERT INTO main 
    (code, subject, sem_number, type_of_cert, date_of_cert, prof_fio, prof_pos, mark, date_of_update) 
    VALUES (?,?,?,?,?,?,?,?,?)"""

    # Занесение полученного кортежа в таблицу
    cur.execute(sql, new_data)

    # Сохранение изменений
    con.commit()

    # Закрытие БД
    cur.close()
    con.close()

def GetTable(dbName):
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