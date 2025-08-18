import sqlite3

# create connection
conn = sqlite3.connect("test.db")

# get cursor to execute quieries
cursor = conn.cursor()

# execute query
cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """)
conn.commit()


data = [("ivan", 23), ("maria", 43)]
cursor.executemany("""INSERT INTO users (name, age) VALUES (?,?)""", data)
conn.commit()

conn.close()
