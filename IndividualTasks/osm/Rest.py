import xml.etree.ElementTree as ET
from collections import defaultdict
import re

# Функция для парсинга времени открытия
def parse_opening_hours(opening_hours):
    # Поиск времени открытия (например, "10:00" или "10:00-22:00")
    match = re.search(r'(\d{1,2}):\d{2}', opening_hours)
    if match:
        return int(match.group(1))  # Возвращает только часы
    return None

# Чтение и обработка XML файла
def group_restaurants_by_opening_hours(osm_file):
    tree = ET.parse(osm_file)
    root = tree.getroot()
    
    # Словарь для группировки по часам открытия
    grouped_restaurants = defaultdict(list)
    no_time_group = "Без времени работы"
    
    # Поиск ресторанов
    for element in root.findall('node'):
        is_restaurant = False
        opening_hours = None
        restaurant_name = None
        
        for tag in element.findall('tag'):
            if tag.attrib.get('k') == 'amenity' and tag.attrib.get('v') == 'restaurant':
                is_restaurant = True
            if tag.attrib.get('k') == 'opening_hours':
                opening_hours = tag.attrib.get('v')
            if tag.attrib.get('k') == 'name':
                restaurant_name = tag.attrib.get('v')
        
        if is_restaurant:
            if opening_hours:
                hour = parse_opening_hours(opening_hours)
                if hour is not None:
                    grouped_restaurants[hour].append(restaurant_name or "Unknown Restaurant")
                else:
                    grouped_restaurants[no_time_group].append(restaurant_name or "Unknown Restaurant")
            else:
                grouped_restaurants[no_time_group].append(restaurant_name or "Unknown Restaurant")
    
    return grouped_restaurants

# Пример вызова функции
osm_file_path = "3.osm"  # Замените на путь к вашему файлу OSM
grouped = group_restaurants_by_opening_hours(osm_file_path)

# Печать результатов
for hour, restaurants in sorted(grouped.items(), key=lambda x: (isinstance(x[0], int), x[0])):
    if isinstance(hour, int):
        print(f"Открываются с {hour}:00:")
    else:
        print(f"{hour}:")
    for restaurant in restaurants:
        print(f"  - {restaurant}")
