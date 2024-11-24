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
festival_id = form.getvalue("festival_id")
name = form.getvalue("name")
date = form.getvalue("date")
group_id = form.getvalue("group_id")

# Добавляем данные в таблицу Festivals, если все значения присутствуют
if festival_id and name and date and group_id:
    try:
        cur.execute(
            "INSERT INTO Festivals (festival_id, name, date, group_id) VALUES (?, ?, ?, ?)",
            (festival_id, name, date, group_id)
        )
        con.commit()
        print("<h2>Фестиваль успешно добавлен!</h2>")
    except sqlite3.IntegrityError:
        print("<h2>Ошибка: ID фестиваля уже существует или другая ошибка.</h2>")
else:
    print("<h2>Ошибка: Заполните все поля формы.</h2>")

# Закрываем соединение с базой данных
cur.close()
con.close()

# Кнопка возврата к форме
print('<a href="/AddFestivalsForm.html">Вернуться к форме</a>')
