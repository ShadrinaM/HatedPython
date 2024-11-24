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
dancer_id = form.getvalue("dancer_id")
name = form.getvalue("name")
age = form.getvalue("age")
style = form.getvalue("style")
group_id = form.getvalue("group_id")

# Добавляем данные в таблицу Dancers, если все значения присутствуют
if dancer_id and name and age and style and group_id:
    try:
        cur.execute(
            "INSERT INTO Dancers (dancer_id, name, age, style, group_id) VALUES (?, ?, ?, ?, ?)",
            (dancer_id, name, age, style, group_id)
        )
        con.commit()
        print("<h2>Танцор успешно добавлен!</h2>")
    except sqlite3.IntegrityError:
        print("<h2>Ошибка: ID танцора уже существует или другая ошибка.</h2>")
else:
    print("<h2>Ошибка: Заполните все поля формы.</h2>")

# Закрываем соединение с базой данных
cur.close()
con.close()

# Кнопка возврата к форме
print('<a href="/AddDancersForm.html">Вернуться к форме</a>')
