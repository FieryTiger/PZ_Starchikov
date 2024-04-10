"""Приложение ЮВЕЛИРНАЯ МАСТЕРСКАЯ для некоторой организации. БД
должна содержать таблицу Изделие со следующей структурой записи: ФИО клиента,
ФИО мастера, вид изделия, материал, стоимость работ."""
import sqlite3 as sq
from information import info

with sq.connect('../BD 2024/jewelry_shop.db') as con:
    cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS Product (Name_client TEXT NOT NUll, Name_master TEXT NOT NULL, Type_product TEXT NOT NULL, Material TEXT NOT NULL, Price REAL NOT NUll)""")
    # cur.executemany("""insert into Product values(?, ?, ?, ?, ?) """, info)
    cur.execute("""SELECT DISTINCT * FROM Product WHERE Price < 1500""")
    result1 = cur.fetchall()
    cur.execute("""SELECT DISTINCT * FROM Product WHERE Type_product = 'Кольцо'""")
    result2 = cur.fetchall()
    cur.execute("""SELECT DISTINCT * FROM Product WHERE Price = 3800 """)
    result3 = cur.fetchall()
    print(result1)
    # cur.execute("""UPDATE Product SET Price = 100 WHERE Name_client LIKE 'Даша'""")
    # cur.execute("""SELECT DISTINCT * FROM Product WHERE Name_client = 'Даша'""")
    # result4 = cur.fetchall()
    # cur.execute("""UPDATE Product SET Name_client = 'Даша' WHERE Name_master LIKE 'Дима'""")
    # cur.execute("""SELECT DISTINCT * FROM Product WHERE Name_master = 'Дима'""")
    # result5 = cur.fetchall()
    # cur.execute("""UPDATE Product SET Type_product = 'Очки' WHERE Price > 200""")
    # cur.execute("""SELECT DISTINCT * FROM Product WHERE Price > 200 """)
    # result6 = cur.fetchall()
    # print(result4)
    # cur.execute("""DELETE FROM Product WHERE Type_product LIKE 'Кольцо'""")
    # cur.execute("""SELECT DISTINCT * FROM Product WHERE Type_product = 'Кольцо'""")
    # result7 = cur.fetchall()
    # cur.execute("""DELETE FROM Product WHERE Price = 1500 and 700""")
    # cur.execute("""SELECT DISTINCT * FROM Product WHERE Price = 1500 and 700 """)
    # result8 = cur.fetchall()
    # cur.execute("""DELETE FROM Product WHERE Name_client LIKE 'Даша'""")
    # cur.execute("""SELECT DISTINCT * FROM Product WHERE Name_client = 'Даша'""")
    # result9 = cur.fetchall()
    # print(result7)