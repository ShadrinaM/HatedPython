import cgi
import cgitb
import sqlite3
import os

print("Content-Type: text/html; charset=Windows-1251\n") 
cgitb.enable()

db_path = os.path.join(os.getcwd(), './dbdance.db')

# Функция для получения таблицы танцоров
def get_dancers_table_html():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''SELECT dancer_id, name, age, style, group_id FROM Dancers''')
    dancers = cursor.fetchall()
    cursor.close()
    conn.close()

    html = "<h1>Танцоры</h1>"
    html += "<table border='1'>"
    html += "<tr><th>ID танцора</th><th>Имя</th><th>Возраст</th><th>Стиль</th><th>ID группы</th></tr>"
    for dancer in dancers:
        # Явно кодируем строки в utf-8
        name = dancer[1].encode('utf-8').decode('utf-8')
        style = dancer[3].encode('utf-8').decode('utf-8')
        html += f"<tr><td>{dancer[0]}</td><td>{name}</td><td>{dancer[2]}</td><td>{style}</td><td>{dancer[4]}</td></tr>"
    html += "</table>"
    return html

# Функция для получения таблицы групп
def get_groups_table_html():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT group_id, name, city FROM Groups")
    groups = cursor.fetchall()
    cursor.close()
    conn.close()

    html = "<h1>Группы</h1>"
    html += "<table border='1'>"
    html += "<tr><th>ID группы</th><th>Название</th><th>Город</th></tr>"
    for group in groups:
        # Явно кодируем строки в utf-8
        group_name = group[1].encode('utf-8').decode('utf-8')
        city = group[2].encode('utf-8').decode('utf-8')
        html += f"<tr><td>{group[0]}</td><td>{group_name}</td><td>{city}</td></tr>"
    html += "</table>"
    return html

# Функция для получения таблицы фестивалей
def get_festivals_table_html():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''SELECT festival_id, name, date, group_id FROM Festivals''')
    festivals = cursor.fetchall()
    cursor.close()
    conn.close()

    html = "<h1>Фестивали</h1>"
    html += "<table border='1'>"
    html += "<tr><th>ID фестиваля</th><th>Название</th><th>Дата</th><th>ID группы</th></tr>"
    for festival in festivals:
        # Явно кодируем строки в utf-8
        festival_name = festival[1].encode('utf-8').decode('utf-8')
        html += f"<tr><td>{festival[0]}</td><td>{festival_name}</td><td>{festival[2]}</td><td>{festival[3]}</td></tr>"
    html += "</table>"
    return html

# Обработка запроса
form = cgi.FieldStorage()
action = form.getvalue("action")

if action == "groups":
    print(get_groups_table_html())
elif action == "festivals":
    print(get_festivals_table_html())
elif action == "dancers":
    print(get_dancers_table_html())
else:
    print("<p>Ошибка: неизвестное действие.</p>")
