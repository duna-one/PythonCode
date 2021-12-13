import sys
import DBFunctions as Db

def MainUI():    
    print("Меню:")
    print("1. Отобразить таблицу")
    print("0. Завершить программу")

    work = True
    while work:
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            Db.ShowTable()
        elif choice == "0":
            sys.exit();

MainUI()