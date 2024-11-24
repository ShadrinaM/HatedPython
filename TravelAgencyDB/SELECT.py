import sqlite3 
from tabulate import tabulate

def selectProc():
    con = sqlite3.connect('db01.db')
    cur = con.cursor()

    # Получение и вывод данных из таблицы Country
    cur.execute('SELECT * FROM Country')
    country_data = cur.fetchall()
    print("Таблица: Country")
    print(tabulate(country_data, headers=["country_id", "name", "country_description"], tablefmt="grid"))

    print("\n")

    # Получение и вывод данных из таблицы TravelAgency
    cur.execute('SELECT * FROM TravelAgency')
    agency_data = cur.fetchall()
    print("Таблица: TravelAgency")
    print(tabulate(agency_data, headers=["agency_id", "name", "country_id"], tablefmt="grid"))

    cur.close()
    con.close()
selectProc()

# & "C:\Users\Марина\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\Марина\Desktop\TravelAgencyDB\SELECT.py"