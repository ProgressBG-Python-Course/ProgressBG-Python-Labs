import sqlite3

connection = sqlite3.connect("python_course.db")

cursor = connection.cursor()

def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        office TEXT,
        age INTEGER,
        start_date TEXT
    )
    ''')
    connection.commit()

def insert_data(data):
    cursor.executemany('''
        INSERT INTO employees (name, position, office, age, start_date)
        VALUES (:name, :position, :office, :age, :start_date)
    ''', data)

    connection.commit()

def select_data():
    cursor.execute("""
         select * from employees;
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    users = (
        {
            'name': 'Maria1',
            'position': 'Python Dev',
            'office': 'Plovdiv',
            'age': 34,
            'start_date': '2022-01-01'
        },
        {
            'name': 'Maria2',
            'position': 'Python Dev',
            'office': 'Plovdiv',
            'age': 34,
            'start_date': '2022-01-01'
        }
    )

    insert_data(users)
    select_data()
    connection.close()

