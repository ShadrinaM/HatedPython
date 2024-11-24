#!/usr/bin/env python3

import cgi
import sqlite3
import json

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('C:/Users/Marina/Documents/GitHub/HatedPython/IndividualTasks/DancingDB/dbdance.db')  # Укажите путь к вашей базе данных
    conn.row_factory = sqlite3.Row  # Чтобы строки возвращались как словари
    return conn

# Функция для получения данных из базы
def fetch_data_from_table(table_name):
    # Проверим, что имя таблицы корректное
    valid_tables = ['Groups', 'Festivals', 'Dancers']
    if table_name not in valid_tables:
        return {"error": "Invalid table name"}

    conn = get_db_connection()
    cursor = conn.cursor()

    # Выполним запрос для выбранной таблицы
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()

    # Преобразуем данные в список словарей
    result = [dict(row) for row in rows]
    conn.close()

    return result

# CGI-скрипт для вывода данных
def main():
    # Заголовки для правильного отображения данных
    print("Content-Type: application/json")  # Ожидаем JSON
    print()  # Пустая строка после заголовков

    # Получаем параметры запроса
    form = cgi.FieldStorage()
    table_name = form.getvalue("table")

    if not table_name:
        print(json.dumps({"error": "No table specified"}))
        return

    # Получаем данные из таблицы
    data = fetch_data_from_table(table_name)

    # Отправляем результат в виде JSON
    print(json.dumps(data))

if __name__ == "__main__":
    main()
