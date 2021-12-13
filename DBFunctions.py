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
    print(tabelNames)

    while True:
        tabelName = input("Введите имя таблицы: ")
        if tabelName in tabelNames:
            break
        else:
            print("Такой таблицы не существует!")

    sql = """\
    select * from {}
    """.format(tabelName)

    columnNames = []
    for name in cur.execute(sql).description:
        columnNames.append(name[0])

    table = cur.execute(sql).fetchall()

    print(columnNames)
    for row in table:
        print(row)

    cur.close()
    con.close()