import sys
import DBFunctions as Db

def MainUI():
    while True:
        print("Меню:")
        print("1. Отобразить таблицу")
        print("2. Отбор по статусу и федеральному округу")
        print("0. Завершить программу")

        choice = input("Выберите пункт меню: ")
        if choice == "1":
            Db.ShowTable()
        elif choice == "2":
            Db.GetByStatusAndArea()
        elif choice == "0":
            sys.exit();

MainUI()