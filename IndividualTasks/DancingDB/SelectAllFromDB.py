import sqlite3 
from tabulate import tabulate

def SelectAll():
    con = sqlite3.connect('dbdance.db')  # Открываем соединение с базой данных
    cur = con.cursor()

    # Получение и вывод данных из таблицы Groups
    cur.execute('SELECT * FROM Groups')
    groups_data = cur.fetchall()
    print("Таблица: Groups")
    print(tabulate(groups_data, headers=["group_id", "name", "city"], tablefmt="grid"))

    print("\n")

    # Получение и вывод данных из таблицы Dancers
    cur.execute('SELECT * FROM Dancers')
    dancers_data = cur.fetchall()
    print("Таблица: Dancers")
    print(tabulate(dancers_data, headers=["dancer_id", "name", "age", "style", "group_id"], tablefmt="grid"))

    print("\n")

    # Получение и вывод данных из таблицы Festivals
    cur.execute('SELECT * FROM Festivals')
    festivals_data = cur.fetchall()
    print("Таблица: Festivals")
    print(tabulate(festivals_data, headers=["festival_id", "name", "date", "group_id"], tablefmt="grid"))

    cur.close()
    con.close()
