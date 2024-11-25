import sqlite3
from tabulate import tabulate

def SelectSpecial():
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

    # Статические SELECT запросы

    # 1. Танцоры, их стиль и группа
    print("\nТанцоры, их стиль и группа:")
    cur.execute('''
    SELECT Dancers.name AS dancer_name, Dancers.style, Groups.name AS group_name
    FROM Dancers
    JOIN Groups ON Dancers.group_id = Groups.group_id;
    ''')
    dancers_groups_data = cur.fetchall()
    print(tabulate(dancers_groups_data, headers=["dancer_name", "style", "group_name"], tablefmt="grid"))

    # 2. Фестивали для группы "The Rhythm"
    print("\nФестивали для группы 'The Rhythm':")
    cur.execute('''
    SELECT Festivals.name AS festival_name, Festivals.date
    FROM Festivals
    JOIN Groups ON Festivals.group_id = Groups.group_id
    WHERE Groups.name = 'The Rhythm';
    ''')
    rhythm_festivals_data = cur.fetchall()
    print(tabulate(rhythm_festivals_data, headers=["festival_name", "date"], tablefmt="grid"))

    # 3. Танцоры старше 25 лет, танцующие в стиле "Ballet"
    print("\nТанцоры старше 25 лет, танцующие в стиле 'Ballet':")
    cur.execute('''
    SELECT name, age
    FROM Dancers
    WHERE age > 25 AND style = 'Ballet';
    ''')
    ballet_dancers_data = cur.fetchall()
    print(tabulate(ballet_dancers_data, headers=["name", "age"], tablefmt="grid"))
    cur.close()
    con.close()


