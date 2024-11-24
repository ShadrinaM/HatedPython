# & "C:\Users\Марина\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\Марина\Desktop\TravelAgencyDB\СreatingDatabase.py"
import sqlite3 
con = sqlite3.connect('db01.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Country') 
cur.execute('DROP TABLE IF EXISTS TravelAgency') 

cur.execute('CREATE TABLE Country (country_id INTEGER PRIMARY KEY, name VARCHAR2(50), country_description VARCHAR2(200))')
cur.execute('CREATE TABLE TravelAgency (аgency_id INTEGER PRIMARY KEY, name VARCHAR2(50), country_id INTEGER REFERENCES Country(country_id ))')

var1=(1, "Россия", "Очень красивая, самая большая страна в мире")
sql1='''INSERT INTO Country VALUES (?,?,?)'''
cur.execute(sql1,var1) 
con.commit() 

var_list = [
    (2,"Япония","Островная страна, родина аниме"),
    (3,"Китай", "Знаменита Великой Китайской стеной"),
    (4,"Италия","Страна очень вкусных блюд")
]
sql='''\
INSERT INTO Country(country_id, name, country_description)
VALUES (?,?,?)
'''
cur.executemany(sql,var_list)
con.commit() 


var_list2 = [
    (1,"Авиасейлс", 1),
    (2,"Авиасейлс", 2),
    (3,"АвтоПоездки", 4),
    (4,"РЖД", 3 )
]
sql2='''\
INSERT INTO TravelAgency(аgency_id, name, country_id)
VALUES (?,?,?)
'''
cur.executemany(sql2,var_list2)
con.commit() 




cur.execute('''
SELECT * FROM Country ''')
for i in cur.fetchall():
    print(i)

print("\n")
cur.execute('''
SELECT * FROM TravelAgency ''')
for i in cur.fetchall():
    print(i)









cur.close()
con.close()