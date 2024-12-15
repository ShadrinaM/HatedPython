# import csv
# import re
# from datetime import datetime


# def process_row(row, unique_entries):
#     try:
#         # Игнорируем строки с "Среднее по группе" или "Общее среднее" в столбце Фамилия
#         if row.get('Фамилия') in ['Среднее по группе', 'Общее среднее']:
#             return None

#         # Обработка фамилии: первая буква заглавная, остальные строчные
#         last_name = row.get('Фамилия', '').strip().capitalize()

#         # Обработка имени: удаляем пробелы в начале и в конце, и берем только первое слово
#         first_name = row.get('Имя', '').strip().split()[0].capitalize() if row.get('Имя') else ''

#         # Проверка состояния и уникальности записи
#         email = row.get('Адрес электронной почты', '')
#         full_name = f"{row.get('Фамилия', '')} {first_name}"
#         key = (full_name, email)
#         # Если запись с таким полным именем и email уже была обработана, игнорируем эту строку
#         if key in unique_entries:
#             return None
#         # Если состояние "Завершено", то добавляем запись в уникальные записи
#         if row.get('Состояние') == 'Завершено':
#             unique_entries[key] = row

#         # Обработка оценки
#         score = 0
#         if 'Оценка/10,00' in row:
#             score_str = row.get('Оценка/10,00', '0').replace(',', '.')
#             score = float(score_str) if score_str.replace('.', '').isdigit() else 0
#         elif 'Оценка/100,00' in row:
#             score_str = row.get('Оценка/100,00', '0').replace(',', '.')
#             score = float(score_str) / 10 if score_str.replace('.', '').isdigit() else 0

#         # Пример обработки времени
#         time_spent = parse_time_to_seconds(row.get('Затраченное время', '0 мин. 0 сек.'))

#         # Возврат обработанных данных
#         return {
#             'Фамилия': last_name,
#             'Имя': first_name,
#             'Оценка': score,
#             'Затраченное время (сек)': time_spent
#         }
#     except Exception as e:
#         print(f"Ошибка при обработке строки: {row}. Ошибка: {e}")
#         return None


# def parse_time_to_seconds(time_str):
#     minutes = 0
#     seconds = 0
#     hours = 0  # Для хранения количества часов

#     if time_str == '-' or not time_str.strip():
#         return 0
    
#     # Ищем количество часов в строке (можно использовать "ч." и "час." с возможными пробелами)
#     match_hours = re.search(r'(\d+)\s*(ч\.|час\.)', time_str)
#     if match_hours:
#         hours = int(match_hours.group(1))  # Извлекаем количество часов

#     # Ищем количество минут
#     match_minutes = re.search(r'(\d+)\s*мин', time_str)
#     if match_minutes:
#         minutes = int(match_minutes.group(1))  # Извлекаем количество минут

#     # Если секунд нет в строке, оставляем их равными 0
#     match_seconds = re.search(r'(\d+)\s*сек', time_str)
#     if match_seconds:
#         seconds = int(match_seconds.group(1))  # Извлекаем количество секунд

#     # Конвертируем всё в секунды
#     total_seconds = hours * 3600 + minutes * 60 + seconds
#     return total_seconds


# processed_data = []
# unique_entries = {}

# # Каждая строка обрабатывается функцией process_row. 
# # Если функция возвращает результат (None игнорируется), он добавляется в список processed_data
# with open('3 - 2.csv', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         result = process_row(row, unique_entries)
#         if result:
#             processed_data.append(result)

# # Сортировка данных по затраченному времени в порядке возрастания
# processed_data.sort(key=lambda x: x['Затраченное время (сек)'])

# # Вывод обработанных и отсортированных данных
# for item in processed_data:
#     print(item)





import csv
import re
from datetime import datetime


def process_row(row, unique_entries):
    try:
        # Игнорируем строки с "Среднее по группе" или "Общее среднее" в столбце Фамилия
        if row.get('Фамилия') in ['Среднее по группе', 'Общее среднее']:
            return None

        # Обработка фамилии: первая буква заглавная, остальные строчные
        last_name = row.get('Фамилия', '').strip().capitalize()

        # Обработка имени: удаляем пробелы в начале и в конце, и берем только первое слово
        first_name = row.get('Имя', '').strip().split()[0].capitalize() if row.get('Имя') else ''

        # Проверка состояния и уникальности записи
        email = row.get('Адрес электронной почты', '')
        full_name = f"{row.get('Фамилия', '')} {first_name}"
        key = (full_name, email)
        # Если запись с таким полным именем и email уже была обработана, игнорируем эту строку
        if key in unique_entries:
            return None
        # Если состояние "Завершено", то добавляем запись в уникальные записи
        if row.get('Состояние') == 'Завершено':
            unique_entries[key] = row

        # Обработка оценки
        score = 0
        if 'Оценка/10,00' in row:
            score_str = row.get('Оценка/10,00', '0').replace(',', '.')
            score = float(score_str) if score_str.replace('.', '').isdigit() else 0
        elif 'Оценка/100,00' in row:
            score_str = row.get('Оценка/100,00', '0').replace(',', '.')
            score = float(score_str) / 10 if score_str.replace('.', '').isdigit() else 0

        # Пример обработки времени
        time_spent = parse_time_to_seconds(row.get('Затраченное время', '0 мин. 0 сек.'))

        # Возврат обработанных данных
        return {
            'Фамилия': last_name,
            'Имя': first_name,
            'Оценка': score,
            'Затраченное время (сек)': time_spent
        }
    except Exception as e:
        print(f"Ошибка при обработке строки: {row}. Ошибка: {e}")
        return None


def parse_time_to_seconds(time_str):
    minutes = 0
    seconds = 0
    hours = 0  # Для хранения количества часов

    if time_str == '-' or not time_str.strip():
        return 0
    
    # Ищем количество часов в строке (можно использовать "ч." и "час." с возможными пробелами)
    match_hours = re.search(r'(\d+)\s*(ч\.|час\.)', time_str)
    if match_hours:
        hours = int(match_hours.group(1))  # Извлекаем количество часов

    # Ищем количество минут
    match_minutes = re.search(r'(\d+)\s*мин', time_str)
    if match_minutes:
        minutes = int(match_minutes.group(1))  # Извлекаем количество минут

    # Если секунд нет в строке, оставляем их равными 0
    match_seconds = re.search(r'(\d+)\s*сек', time_str)
    if match_seconds:
        seconds = int(match_seconds.group(1))  # Извлекаем количество секунд

    # Конвертируем всё в секунды
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


def process_file(file_name):
    processed_data = []
    unique_entries = {}

    print(f"Обрабатывается файл {file_name}...")
    with open(file_name, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            result = process_row(row, unique_entries)
            if result:
                processed_data.append(result)

    # Сортировка данных по затраченному времени в порядке возрастания
    processed_data.sort(key=lambda x: x['Затраченное время (сек)'])

    # Вывод обработанных и отсортированных данных
    print(f"Результат обработки файла {file_name}:")
    for item in processed_data:
        print(item)


# Обработка файлов
process_file('3 - 1.csv')
process_file('3 - 2.csv')
