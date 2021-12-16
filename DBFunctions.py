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

    print("Доступные таблицы:")
    for i in range(0, len(tabelNames)):
        print("{}. {}".format(i+1, tabelNames[i]))

    while True:
        try:
            table = int(input("Введите номер таблицы: "))
            if table in range(1, len(tabelNames) + 1):
                break
            else:
                print("Таблицы с таким номером не существует!")
        except:
            print("Введите число!")

    sql = """\
    select * from {}
    """.format(tabelNames[table-1])

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
    for i in range(0, len(FedOkr)):
        print("{}. {}".format(i+1, FedOkr[i]))

    while True:
        try:
            SelectedOkr = int(input("Введите номер округа (или несколько через пробел): "))
            if SelectedOkr in range(1, len(FedOkr) + 1):
                break;
            else:
                print("Некорректный ввод!")
        except:
            print("Введите число")

    #Выбор статуса
    print("Доступные статусы: ")
    for i in range(0, len(Status)):
        print("{}. {}".format(i+1, Status[i]))

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

def GetOnPost():

    while True:
        print("Доступные варианты выборки по должности: ")
        print("1. Профессор")
        print("2. Доцент")
        print("3. Прочие")
        print("4. Все")
        choice = input("Выберите вариант выборки: ")
        if choice == "1":
           columnName = "pr"
           break
        elif choice == "2":
           columnName = "dc"
           break
        elif choice == "3":
           columnName = "dn + kn"
           break
        else:
           print("Такого варианта выборки нет.")

    sql = """\
    SELECT ROW_NUMBER () OVER (ORDER BY fedokr) №, 
			fedokr as 'Федеральный округ', SUM({0}) as 'Число преподавателей'
        FROM 
        	vuz_rf JOIN vuzstat on vuz_rf.cod = vuzstat.codvuz GROUP BY fedokr
    UNION SELECT '', 'Все', SUM({0}) FROM vuzstat
    """.format(columnName)

    con = sqlite3.connect("vuz.sqlite")
    cur = con.cursor()

    cur = cur.execute(sql)

    columnNames = []
    result = cur.fetchall()

    for name in cur.description:
        columnNames.append(name[0])
    print(columnNames)
    for row in result:
        print(row)