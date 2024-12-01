#  & C:/Users/Marina/AppData/Local/Programs/Python/Python313/python.exe c:/Users/Marina/Documents/GitHub/HatedPython/IndividualTasks/DancingDB/FromXML.py
import sqlite3
import xml.etree.ElementTree as ET

def import_from_xml(database, xml_file):
    try:
        # Подключение к базе данных
        with sqlite3.connect(database) as con:
            cur = con.cursor()

            # Парсинг XML-файла
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Импорт данных в таблицу Groups
            groups = root.find("Groups")
            if groups is not None:
                for group in groups.findall("Group"):
                    group_id = int(group.find("GroupID").text)
                    name = group.find("Name").text
                    city = group.find("City").text
                    cur.execute(
                        "INSERT OR IGNORE INTO Groups (group_id, name, city) VALUES (?, ?, ?)",
                        (group_id, name, city),
                    )

            # Импорт данных в таблицу Dancers
            dancers = root.find("Dancers")
            if dancers is not None:
                for dancer in dancers.findall("Dancer"):
                    dancer_id = int(dancer.find("DancerID").text)
                    name = dancer.find("Name").text
                    age = int(dancer.find("Age").text)
                    style = dancer.find("Style").text
                    group_id = dancer.find("GroupID").text
                    group_id = int(group_id) if group_id else None
                    cur.execute(
                        "INSERT OR IGNORE INTO Dancers (dancer_id, name, age, style, group_id) VALUES (?, ?, ?, ?, ?)",
                        (dancer_id, name, age, style, group_id),
                    )

            # Импорт данных в таблицу Festivals
            festivals = root.find("Festivals")
            if festivals is not None:
                for festival in festivals.findall("Festival"):
                    festival_id = int(festival.find("FestivalID").text)
                    name = festival.find("Name").text
                    date = festival.find("Date").text
                    group_id = festival.find("GroupID").text
                    group_id = int(group_id) if group_id else None
                    cur.execute(
                        "INSERT OR IGNORE INTO Festivals (festival_id, name, date, group_id) VALUES (?, ?, ?, ?)",
                        (festival_id, name, date, group_id),
                    )

            # Сохранение изменений
            con.commit()
            print(f"Данные из {xml_file} успешно импортированы в базу данных.")

    except sqlite3.Error as e:
        print(f"Ошибка работы с базой данных: {e}")
    except ET.ParseError as e:
        print(f"Ошибка при парсинге XML: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")

# Вызов функции
if __name__ == "__main__":
    import_from_xml("dbdance.db", "database_import.xml")
