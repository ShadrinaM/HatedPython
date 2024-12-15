# import csv
# from datetime import datetime
# import os

# # Проверка наличия файла в текущем каталоге
# filename = '3 - 1.csv'  # Убедитесь, что файл находится в той же директории, что и ваш скрипт

# # Функция для чтения файла CSV и возврата данных в виде списка словарей
# def read_csv(filename):
#     records = []
#     if not os.path.isfile(filename):
#         print(f"File '{filename}' not found.")
#         return records
    
#     with open(filename, 'r', encoding='utf-8') as csvfile:
#         csvreader = csv.reader(csvfile, delimiter=';')
#         headers = next(csvreader)  # Пропустить заголовок
#         for row in csvreader:
#             if len(row) < 10:  # Проверяем, что строка содержит хотя бы 10 колонок
#                 print(f"Skipping malformed row: {row}")
#                 continue  # Пропускаем строки с недостаточным количеством данных
#             record = {
#                 'Фамилия': row[0],
#                 'Имя': row[1],
#                 'Завершено': datetime.strptime(row[6], '%d %B %Y %H:%M'),
#                 'Затраченное время': row[8]
#             }
#             records.append(record)
#     return records

# # Функция для сортировки слушателей по времени завершения
# def sort_by_completion_time(records):
#     return sorted(records, key=lambda x: x['Завершено'])

# # Чтение данных из CSV
# records = read_csv(filename)

# # Сортируем по времени завершения
# sorted_records = sort_by_completion_time(records)

# # Вывод результата
# for record in sorted_records:
#     print(f"{record['Фамилия']}, {record['Имя']}, {record['Завершено']}")







import csv
from datetime import datetime
import os

filename = '3 - 1.csv'

def read_csv(filename):
    records = []
    if not os.path.isfile(filename):
        print(f"File '{filename}' not found.")
        return records
    
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        headers = next(csvreader)  # Пропустить заголовок
        for row in csvreader:
            if len(row) < 10:  # Проверяем, что строка содержит хотя бы 10 колонок
                print(f"Skipping malformed row: {row}")
                continue  # Пропускаем строки с недостаточным количеством данных

            # Проверяем, что дата и время в правильном формате
            try:
                completed_date = datetime.strptime(row[6], '%d %B %Y %H:%M')
                time_spent = row[8]  # Времени затрачено
                records.append({
                    'Фамилия': row[0],
                    'Имя': row[1],
                    'Завершено': completed_date,
                    'Затраченное время': time_spent
                })
            except ValueError as e:
                print(f"Skipping malformed row due to ValueError: {row}")
                continue

    return records

def sort_by_completion_time(records):
    return sorted(records, key=lambda x: x['Завершено'])

# Чтение данных из CSV
records = read_csv(filename)

# Сортируем по времени завершения
sorted_records = sort_by_completion_time(records)

# Вывод результата
for record in sorted_records:
    print(f"{record['Фамилия']}, {record['Имя']}, {record['Завершено']}")
