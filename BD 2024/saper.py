import sqlite3 as sq
from data_users import info_users
with sq.connect('saper.db') as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, sex INTEGER NOT NULL DEFAULT 1, old INTEGER, score INTEGER)""")
    # cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE score < 1000 ORDER BY old DESC")
    result = cur.fetchall()
    print(result)
    # for result in cur:
    #     print(result)