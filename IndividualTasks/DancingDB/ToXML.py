# & C:/Users/Marina/AppData/Local/Programs/Python/Python313/python.exe c:/Users/Marina/Documents/GitHub/HatedPython/IndividualTasks/DancingDB/ToXML.py

import sqlite3
import xml.etree.ElementTree as ET

def export_to_xml(database, output_file):
    try:
        # Подключение к базе данных
        with sqlite3.connect(database) as con:
            cur = con.cursor()

            # Создание корневого элемента XML
            root = ET.Element("Database")

            # Экспорт таблицы Groups
            cur.execute("SELECT * FROM Groups")
            groups = ET.SubElement(root, "Groups")
            for row in cur.fetchall():
                group = ET.SubElement(groups, "Group")
                ET.SubElement(group, "GroupID").text = str(row[0])
                ET.SubElement(group, "Name").text = row[1]
                ET.SubElement(group, "City").text = row[2]

            # Экспорт таблицы Dancers
            cur.execute("SELECT * FROM Dancers")
            dancers = ET.SubElement(root, "Dancers")
            for row in cur.fetchall():
                dancer = ET.SubElement(dancers, "Dancer")
                ET.SubElement(dancer, "DancerID").text = str(row[0])
                ET.SubElement(dancer, "Name").text = row[1]
                ET.SubElement(dancer, "Age").text = str(row[2])
                ET.SubElement(dancer, "Style").text = row[3]
                ET.SubElement(dancer, "GroupID").text = str(row[4]) if row[4] else ""

            # Экспорт таблицы Festivals
            cur.execute("SELECT * FROM Festivals")
            festivals = ET.SubElement(root, "Festivals")
            for row in cur.fetchall():
                festival = ET.SubElement(festivals, "Festival")
                ET.SubElement(festival, "FestivalID").text = str(row[0])
                ET.SubElement(festival, "Name").text = row[1]
                ET.SubElement(festival, "Date").text = row[2]
                ET.SubElement(festival, "GroupID").text = str(row[3]) if row[3] else ""

            # Запись данных в XML-файл
            tree = ET.ElementTree(root)
            with open(output_file, "wb") as f:
                tree.write(f, encoding="utf-8", xml_declaration=True)

            print(f"Данные успешно экспортированы в {output_file}")

    except sqlite3.Error as e:
        print(f"Ошибка работы с базой данных: {e}")
    except Exception as e:
        print(f"Ошибка при экспорте в XML: {e}")

# Вызов функции
if __name__ == "__main__":
    export_to_xml("dbdance.db", "database_export.xml")
