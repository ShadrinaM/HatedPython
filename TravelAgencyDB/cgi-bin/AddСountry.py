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
con = sqlite3.connect('C:/Users/Марина/Desktop/питон/db01.db')  # Убедитесь, что путь правильный
cur = con.cursor()

# Получаем данные из формы
form = cgi.FieldStorage()
country_id = form.getvalue("country_id")
name = form.getvalue("name")
country_description = form.getvalue("country_description")

# Добавляем данные в таблицу Country, если все значения присутствуют
if country_id and name and country_description:
    try:
        cur.execute(
            "INSERT INTO Country (country_id, name, country_description) VALUES (?, ?, ?)",
            (country_id, name, country_description)
        )
        con.commit()
        print("<h2>Данные успешно добавлены!</h2>")
    except sqlite3.IntegrityError:
        print("<h2>Ошибка: ID уже существует или другая ошибка.</h2>")
else:
    print("<h2>Ошибка: Заполните все поля формы.</h2>")

# Закрываем соединение с базой данных
cur.close()
con.close()

# Кнопка возврата к форме
print('<a href="/AddСountryForm.html">Вернуться к форме</a>')
