import sqlite3

def ShowTable():

    con = sqlite3.connect("vuz.sqlite")
    cur = con.cursor()

    sql = """\
    select name from sqlite_master where type = 'table'
    """
    tabelNames = []
    for name in cur.execute(sql).fetchall():
        tabelNames.append(name[0])

    print("Доступные таблицы:\n")
    for i in range(1, len(tabelNames)):
        print("{}. {}".format(in tabelNames[i])

    while True:
        try:
            tabel = int(input("Введите номер таблицы: "))
            if tabel in range(1, len(tabelNames)):
                break
            else:
                print("Таблицы с таким номером не существует!")
        except:
            print("Введите число!")

    sql = """\
    select * from {}
    """.format(tabelNames[tabel-1])

    columnNames = []
    for name in cur.execute(sql).description:
        columnNames.append(name[0])

    table = cur.execute(sql).fetchall()

    print(columnNames)
    for row in table:
        print(row)

    cur.close()
    con.close()

def GetByStatusAndArea():
    con = sqlite3.connect("vuz.sqlite")
    cur = con.cursor()

    sql = """\
    select distinct FedOkr FROM vuz_rf
    """

    FedOkr = []
    for okr in cur.execute(sql).fetchall():
        FedOkr.append(okr[0])

    sql = """\
    select distinct Status FROM vuz_rf
    """

    Status = []
    for stat in cur.execute(sql).fetchall():
        Status.append(stat[0])

    #Выбор округа
    print("Доступные федеральные округа: ")
    for i in range(1, len(FedOkr)):
        print("{}. {}".format(i, FedOkr[i-1]))

    while True:
        try:
            SelectedOkr = int(input("Введите номер округа (или несколько через пробел): "))
            if SelectedOkr in range(1, len(FedOkr)):
                break;
            else:
                print("Некорректный ввод!")
        except:
            print("Введите число")

    #Выбор статуса
    print("Доступные статусы: ")
    for i in range(1, len(Status)):
        print("{}. {}".format(i, Status[i-1]))

    while True:
        try:
            SelectedStatus = int(input("Введите номер округа: "))
            if SelectedStatus in range(1, len(Status)):
                break;
            else:
                print("Некорректный ввод!")
        except:
            print("Введите число")

    sql = """\
    SELECT z1full FROM vuz_rf JOIN vuzkart on vuz_rf.cod = vuzkart.codvuz
    WHERE vuz_rf.status = '{}' AND vuz_rf.FedOkr = '{}'
    """.format(Status[SelectedStatus-1], FedOkr[SelectedOkr-1])
    
    print("Результат:")
    for resItem in cur.execute(sql).fetchall():
        print(" - {}".format(resItem[0]))