#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import cgi
import cgitb

# Включаем отладчик CGI (поможет при возникновении ошибок)
cgitb.enable()

# Заголовок для вывода HTML
print("Content-Type: text/html\n")

# Подключаемся к базе данных
con = sqlite3.connect('C:/Users/Marina/Documents/GitHub/HatedPython/IndividualTasks/DancingDB/dbdance.db')  # Убедитесь, что путь правильный
cur = con.cursor()

# Получаем данные из формы
form = cgi.FieldStorage()
group_id = form.getvalue("group_id")
name = form.getvalue("name")
city = form.getvalue("city")

# Добавляем данные в таблицу Groups, если все значения присутствуют
if group_id and name and city:
    try:
        cur.execute(
            "INSERT INTO Groups (group_id, name, city) VALUES (?, ?, ?)",
            (group_id, name, city)
        )
        con.commit()
        print("<h2>Группа успешно добавлена!</h2>")
    except sqlite3.IntegrityError:
        print("<h2>Ошибка: ID уже существует или другая ошибка.</h2>")
else:
    print("<h2>Ошибка: Заполните все поля формы.</h2>")

# Закрываем соединение с базой данных
cur.close()
con.close()

# Кнопка возврата к форме
print('<a href="/AddGroupsForm.html">Вернуться к форме</a>')
