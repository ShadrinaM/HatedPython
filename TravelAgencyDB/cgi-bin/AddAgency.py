#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import cgi
import cgitb

# Включаем отладчик CGI для отладки ошибок
cgitb.enable()

# Заголовок для вывода HTML
print("Content-Type: text/html\n")

# Подключаемся к базе данных с полным абсолютным путем
con = sqlite3.connect('C:/Users/Marina/Documents/GitHub/HatedPython/TravelAgencyDB/db01.db')
cur = con.cursor()

# Получаем данные из формы
form = cgi.FieldStorage()
agency_id = form.getvalue("agency_id")
name = form.getvalue("name")
country_id = form.getvalue("country_id")

# Добавляем данные в таблицу TravelAgency, если все значения присутствуют
if agency_id and name and country_id:
    try:
        cur.execute(
            "INSERT INTO TravelAgency (аgency_id, name, country_id) VALUES (?, ?, ?)",
            (agency_id, name, country_id)
        )
        con.commit()
        print("<h2>Агентство успешно добавлено!</h2>")
    except sqlite3.IntegrityError:
        print("<h2>Ошибка: ID уже существует или другая ошибка.</h2>")
else:
    print("<h2>Ошибка: Заполните все поля формы.</h2>")

# Закрываем соединение с базой данных
cur.close()
con.close()

# Кнопка возврата к форме
print('<a href="/AddAgencyForm.html">Вернуться к форме</a>')
