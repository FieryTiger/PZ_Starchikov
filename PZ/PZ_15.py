"""Приложение ЮВЕЛИРНАЯ МАСТЕРСКАЯ для некоторой организации. БД
должна содержать таблицу Изделие со следующей структурой записи: ФИО клиента,
ФИО мастера, вид изделия, материал, стоимость работ."""
# import sqlite3 as sq
# from information import info
#
# with sq.connect('jewelry_shop.db') as con:
#     cur = con.cursor()
#     # cur.execute("DROP TABLE IF EXISTS Product")
#     # cur.execute("""CREATE TABLE IF NOT EXISTS Product (Name_client TEXT NOT NUll, Name_master TEXT NOT NULL, Type_product TEXT NOT NULL, Material TEXT NOT NULL, Price REAL NOT NUll)""")
#     # cur.executemany("""insert into Product values(?, ?, ?, ?, ?) """, info)
#
# with sq.connect('jewelry_shop.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT DISTINCT * FROM Product WHERE Price < 1500""")
#     result1 = cur.fetchall()
#
# with sq.connect('jewelry_shop.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT DISTINCT * FROM Product WHERE Type_product = 'Кольцо'""")
#     result2 = cur.fetchall()
#
# with sq.connect('jewelry_shop.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT DISTINCT * FROM Product WHERE Price = 3800""")
#     result3 = cur.fetchall()
#
#     print(result1)

# with sq.connect('jewelry_shop.db') as con:
#     cur = con.cursor()
#     cur.execute("""UPDATE Product SET Price = 100 WHERE Name_client LIKE 'Даша'""")
#     cur.execute("""SELECT DISTINCT * FROM Product WHERE Name_client = 'Даша'""")
#     result4 = cur.fetchall()
#
# with sq.connect('jewelry_shop.db') as con:
#     cur = con.cursor()
#     cur.execute("""UPDATE Product SET Name_client = 'Даша' WHERE Name_master LIKE 'Дима'""")
#     cur.execute("""SELECT DISTINCT * FROM Product WHERE Name_master = 'Дима'""")
#     result5 = cur.fetchall()
#
# with sq.connect('jewelry_shop.db') as con:
#     cur = con.cursor()
#     cur.execute("""UPDATE Product SET Type_product = 'Очки' WHERE Price > 200""")
#     cur.execute("""SELECT DISTINCT * FROM Product WHERE Price > 200 """)
#     result6 = cur.fetchall()
#
#     print(result4)
#
# with sq.connect('jewelry_shop.db') as con:
#     cur = con.cursor()
#     cur.execute("""DELETE FROM Product WHERE Type_product LIKE 'Кольцо'""")
#     cur.execute("""SELECT DISTINCT * FROM Product WHERE Type_product = 'Кольцо'""")
#     result7 = cur.fetchall()
#
# with sq.connect('jewelry_shop.db') as con:
#     cur = con.cursor()
#     cur.execute("""DELETE FROM Product WHERE Price = 1500 and 700""")
#     cur.execute("""SELECT DISTINCT * FROM Product WHERE Price = 1500 and 700 """)
#     result8 = cur.fetchall()
#
# with sq.connect('jewelry_shop.db') as con:
#     cur = con.cursor()
#     cur.execute("""DELETE FROM Product WHERE Name_client LIKE 'Даша'""")
#     cur.execute("""SELECT DISTINCT * FROM Product WHERE Name_client = 'Даша'""")
#     result9 = cur.fetchall()
#
#     print(result7)
































# class Note:
#     def __init__(self, text):
#         self.text = text
#         self.count = 0
#
#     def upcount(self):
#         self.count += 1
#
# note1 = Note("Задача 1")
# print(note1)
# print(note1.__dict__)
# print(dir(note1))
# print(note1.text)
#
# note1.upcount()
# print(note1.count)
# note1.upcount()
# print(note1.count)

# Привязанные методы
# print(note1.upcount)  # bound Метод является привязанным для экземпляра note1.
# print(Note.upcount)  # function с точки зрения класса Note upcount является обычной функцией.

# note2 = Note("Задача 2")
# print(note2)
# print(note2.__dict__)
# print(dir(note2))
# print(note2.text)



# class NoteTwo:
#     def __init__(self, iscompleted=True):
#         self.iscompleted = iscompleted
#         self.count = 0
#
#     def upcount(self):
#         self.upcount += 1
#
#     def reset_count(self):
#         self.count = 0
#
#
# note3 = NoteTwo(True)
# print(note3.iscompleted)
# print(note3.count)
# print(note3.__dict__)



# class Person:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.count += 1
#
#     @staticmethod
#     def total_people():
#         print(Person.count)
#
#
# pr = Person("")
# pr1 = Person("")
# pr2 = Person("")
# pr2.total_people()

class Image:

    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, resolution):
        self.resolution = resolution


    def title_upper(self, title):
        self.title = title.upper()


t = Image(100,"abcdf", 550)
t.title_upper("abcdf")
print(t.title)

r1 = Image(100, "A", 56)
r1.resize(100)
print(r1.resolution)
print(r1.resize)
print(r1.__dict__)
r2 = Image(700, "B", 56)
r2.resize(700)
print(r2.resolution)
print(r2.resize)
print(r2.__dict__)
r3 = Image(900, "C", 38)
r3.resize(900)
print(r3.resolution)
print(r3.resize)
print(r3.__dict__)















class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sex_1(self):
        return f'{self.name}, {self.age} - мужской'

class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, 'женский')

    def sex_1(self):
        return f'{self.name} - женщина'

man = Man('Иван', 25)
woman = Woman('Мария', 30)
print(man.sex_1())
print(woman.sex_1())



# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# class Man(Human):
#     def info(self):
#         print(f"Пол: {self.sex}")
#
#
# class Woman(Human):
#     def info(self):
#         print(f"Пол: {self.sex}")
#
#
# man = Man("Олег", 15, "Мужской")
# woman = Woman("Оля", 12, "Женский")
# man.info()
# woman.info()



































