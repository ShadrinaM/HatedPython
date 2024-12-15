import sqlite3 # подключение встроенной библиотеки Python - SQLite
from SelectAllFromDB import *

con = sqlite3.connect('dbdance.db') # открывает файл БД dbdance.db если он есть, если нет создаёт
cur = con.cursor() # Создаёт объект курсор, который позволяет взаимодействать в БД

# Удаление остатков старой базы
cur.execute('DROP TABLE IF EXISTS Dancers') 
cur.execute('DROP TABLE IF EXISTS Groups') 
cur.execute('DROP TABLE IF EXISTS Festivals') 
con.commit()

# Создание новых таблиц
cur.execute('''
CREATE TABLE Dancers (
    dancer_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    style TEXT,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES Groups(group_id)
);
''')
cur.execute('''
CREATE TABLE Groups (
    group_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
);
''')
cur.execute('''
CREATE TABLE Festivals (
    festival_id INTEGER PRIMARY KEY,
    name TEXT,
    date TEXT, -- В SQLite DATE хранится как TEXT, INTEGER или REAL
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES Groups(group_id)
);
''')


# Вставка данных в таблицу Groups
groups_data = [
    ('The Rhythm', 'New York'),
    ('Dance Masters', 'Los Angeles'),
    ('Groove Crew', 'Chicago'),
    ('Step Up', 'Miami'),
    ('Hip Hop Legends', 'Dallas')
]
cur.executemany('''INSERT INTO Groups (name, city) VALUES (?, ?)''', groups_data)

# Вставка данных в таблицу Dancers
dancers_data = [
    ('Alice', 25, 'Hip Hop', 1),
    ('Bob', 28, 'Contemporary', 2),
    ('Charlie', 30, 'Ballet', 3),
    ('David', 22, 'Jazz', 4),
    ('Eva', 27, 'Salsa', 5),
    ('Frank', 24, 'Tango', 2),
    ('Grace', 26, 'Breakdance', 1),
    ('Hannah', 29, 'Swing', 3),
    ('Ivy', 23, 'Hip Hop', 4),
    ('Jack', 31, 'Ballet', 5)
]
cur.executemany('''INSERT INTO Dancers (name, age, style, group_id) VALUES (?, ?, ?, ?)''', dancers_data)

# Вставка данных в таблицу Festivals
festivals_data = [
    ('Global Dance Fest', '2024-05-10', 1),
    ('World Dance Championship', '2024-06-15', 2),
    ('Chicago Dance Show', '2024-07-20', 3),
    ('Miami Dance Celebration', '2024-08-05', 4),
    ('Dallas Dance Contest', '2024-09-12', 5),
    ('Hip Hop Dance Fest', '2024-10-25', 1),
    ('Jazz Dance Battle', '2024-11-15', 2),
    ('Ballet Extravaganza', '2024-12-01', 3),
    ('Breakdance World Cup', '2025-01-10', 4),
    ('Salsa World Festival', '2025-02-25', 5)
]
cur.executemany('''INSERT INTO Festivals (name, date, group_id) VALUES (?, ?, ?)''', festivals_data)

# Сохранение изменений
con.commit()
cur.close()
con.close()