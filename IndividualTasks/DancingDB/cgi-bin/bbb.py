# # # #!/usr/bin/env python3

# # # import cgi
# # # import cgitb
# # # import sqlite3
# # # import os

# # # print("Content-Type: text/html\n")
# # # cgitb.enable()

# # # db_path = os.path.join(os.getcwd(), './dbdance.db')

# # # def get_dancers_info():
# # #     conn = sqlite3.connect(db_path)
# # #     cursor = conn.cursor()
# # #     cursor.execute('''SELECT
# # #                         dancer_id, name, age, style, group_id
# # #                         FROM
# # #                         Dancers''')
# # #     results = cursor.fetchall()
# # #     cursor.close()
# # #     conn.close()
# # #     return results

# # # def get_groups_info():
# # #     conn = sqlite3.connect(db_path)
# # #     cursor = conn.cursor()
# # #     cursor.execute("SELECT group_id, name, city FROM Groups")
# # #     results = cursor.fetchall()
# # #     cursor.close()
# # #     conn.close()
# # #     return results

# # # def get_festivals_info():
# # #     conn = sqlite3.connect(db_path)
# # #     cursor = conn.cursor()
# # #     cursor.execute('''SELECT
# # #                         festival_id, name, date, group_id
# # #                         FROM
# # #                         Festivals''')
# # #     results = cursor.fetchall()
# # #     cursor.close()
# # #     conn.close()
# # #     return results

# # # # Функция для генерации HTML-страницы
# # # def generate_html(groups, dancers, festivals):
# # #     print()
# # #     print("<html>")
# # #     print("<head><title>Данные таблиц</title></head>")
# # #     print("<body>")
    
# # #     # Таблица групп
# # #     print("<h1>Группы</h1>")
# # #     print("<table border='1'>")
# # #     print("<tr><th>ID группы</th><th>Название</th><th>Город</th></tr>")
# # #     for group in groups:
# # #         print(f"<tr><td>{group[0]}</td><td>{group[1]}</td><td>{group[2]}</td></tr>")
# # #     print("</table>")
    
# # #     # Таблица танцоров
# # #     print("<h1>Танцоры</h1>")
# # #     print("<table border='1'>")
# # #     print("<tr><th>ID танцора</th><th>Имя</th><th>Возраст</th><th>Стиль</th><th>ID группы</th></tr>")
# # #     for dancer in dancers:
# # #         print(f"<tr><td>{dancer[0]}</td><td>{dancer[1]}</td><td>{dancer[2]}</td><td>{dancer[3]}</td><td>{dancer[4]}</td></tr>")
# # #     print("</table>")
    
# # #     # Таблица фестивалей
# # #     print("<h1>Фестивали</h1>")
# # #     print("<table border='1'>")
# # #     print("<tr><th>ID фестиваля</th><th>Название</th><th>Дата</th><th>ID группы</th></tr>")
# # #     for festival in festivals:
# # #         print(f"<tr><td>{festival[0]}</td><td>{festival[1]}</td><td>{festival[2]}</td><td>{festival[3]}</td></tr>")
# # #     print("</table>")
    
# # #     print("</body>")
# # #     print("</html>")

# # # if __name__ == "__main__":
# # #     groups = get_groups_info()
# # #     dancers = get_dancers_info()
# # #     festivals = get_festivals_info()
# # #     generate_html(groups, dancers, festivals)






# # #!/usr/bin/env python3

# # import cgi
# # import cgitb
# # import sqlite3
# # import os

# # print("Content-Type: text/html\n")
# # cgitb.enable()

# # db_path = os.path.join(os.getcwd(), './dbdance.db')

# # def get_dancers_table_html():
# #     conn = sqlite3.connect(db_path)
# #     cursor = conn.cursor()
# #     cursor.execute('''SELECT dancer_id, name, age, style, group_id FROM Dancers''')
# #     dancers = cursor.fetchall()
# #     cursor.close()
# #     conn.close()

# #     html = "<h1>Танцоры</h1>"
# #     html += "<table border='1'>"
# #     html += "<tr><th>ID танцора</th><th>Имя</th><th>Возраст</th><th>Стиль</th><th>ID группы</th></tr>"
# #     for dancer in dancers:
# #         html += f"<tr><td>{dancer[0]}</td><td>{dancer[1]}</td><td>{dancer[2]}</td><td>{dancer[3]}</td><td>{dancer[4]}</td></tr>"
# #     html += "</table>"
# #     return html

# # def get_groups_table_html():
# #     conn = sqlite3.connect(db_path)
# #     cursor = conn.cursor()
# #     cursor.execute("SELECT group_id, name, city FROM Groups")
# #     groups = cursor.fetchall()
# #     cursor.close()
# #     conn.close()

# #     html = "<h1>Группы</h1>"
# #     html += "<table border='1'>"
# #     html += "<tr><th>ID группы</th><th>Название</th><th>Город</th></tr>"
# #     for group in groups:
# #         html += f"<tr><td>{group[0]}</td><td>{group[1]}</td><td>{group[2]}</td></tr>"
# #     html += "</table>"
# #     return html

# # def get_festivals_table_html():
# #     conn = sqlite3.connect(db_path)
# #     cursor = conn.cursor()
# #     cursor.execute('''SELECT festival_id, name, date, group_id FROM Festivals''')
# #     festivals = cursor.fetchall()
# #     cursor.close()
# #     conn.close()

# #     html = "<h1>Фестивали</h1>"
# #     html += "<table border='1'>"
# #     html += "<tr><th>ID фестиваля</th><th>Название</th><th>Дата</th><th>ID группы</th></tr>"
# #     for festival in festivals:
# #         html += f"<tr><td>{festival[0]}</td><td>{festival[1]}</td><td>{festival[2]}</td><td>{festival[3]}</td></tr>"
# #     html += "</table>"
# #     return html

# # # Функция для генерации HTML-страницы с таблицами
# # def generate_html():
# #     groups_html = get_groups_table_html()
# #     dancers_html = get_dancers_table_html()
# #     festivals_html = get_festivals_table_html()

# #     html = "<html>"
# #     html += "<head><title>Данные таблиц</title></head>"
# #     html += "<body>"
# #     html += groups_html
# #     html += dancers_html
# #     html += festivals_html
# #     html += "</body>"
# #     html += "</html>"

# #     return html

# # if __name__ == "__main__":
# #     html_page = generate_html()
# #     print(html_page)





# #!/usr/bin/env python3

# import cgi
# import cgitb
# import sqlite3
# import os

# print("Content-Type: text/html\n")
# cgitb.enable()

# db_path = os.path.join(os.getcwd(), './dbdance.db')

# def get_dancers_table_html():
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute('''SELECT dancer_id, name, age, style, group_id FROM Dancers''')
#     dancers = cursor.fetchall()
#     cursor.close()
#     conn.close()

#     html = "<h1>Танцоры</h1>"
#     html += "<table border='1'>"
#     html += "<tr><th>ID танцора</th><th>Имя</th><th>Возраст</th><th>Стиль</th><th>ID группы</th></tr>"
#     for dancer in dancers:
#         html += f"<tr><td>{dancer[0]}</td><td>{dancer[1]}</td><td>{dancer[2]}</td><td>{dancer[3]}</td><td>{dancer[4]}</td></tr>"
#     html += "</table>"
#     return html

# def get_groups_table_html():
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute("SELECT group_id, name, city FROM Groups")
#     groups = cursor.fetchall()
#     cursor.close()
#     conn.close()

#     html = "<h1>Группы</h1>"
#     html += "<table border='1'>"
#     html += "<tr><th>ID группы</th><th>Название</th><th>Город</th></tr>"
#     for group in groups:
#         html += f"<tr><td>{group[0]}</td><td>{group[1]}</td><td>{group[2]}</td></tr>"
#     html += "</table>"
#     return html

# def get_festivals_table_html():
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute('''SELECT festival_id, name, date, group_id FROM Festivals''')
#     festivals = cursor.fetchall()
#     cursor.close()
#     conn.close()

#     html = "<h1>Фестивали</h1>"
#     html += "<table border='1'>"
#     html += "<tr><th>ID фестиваля</th><th>Название</th><th>Дата</th><th>ID группы</th></tr>"
#     for festival in festivals:
#         html += f"<tr><td>{festival[0]}</td><td>{festival[1]}</td><td>{festival[2]}</td><td>{festival[3]}</td></tr>"
#     html += "</table>"
#     return html

# # Обработка запроса
# form = cgi.FieldStorage()
# action = form.getvalue("action")

# if action == "groups":
#     print(get_groups_table_html())
# elif action == "festivals":
#     print(get_festivals_table_html())
# elif action == "dancers":
#     print(get_dancers_table_html())
# else:
#     print("<p>Ошибка: неизвестное действие.</p>")





#!/usr/bin/env python3

import cgi
import cgitb
import sqlite3
import os

print("Content-Type: text/html; charset=Windows-1251\n")  # Устанавливаем кодировку UTF-8
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
