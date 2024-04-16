import sqlite3

class SQLiteDB:
    def __init__(self, db_name='./python_course.db') -> None:
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.create_table()

    def __del__(self):
        self.connection.close()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )
        ''')
        self.connection.commit()

    def insert_row(self, user_data):
        """Create"""
        sql = '''
            INSERT INTO user (name, age)
            VALUES (?, ?)
        '''
        self.cursor.execute(sql, user_data)

        self.connection.commit()

    def read(self):
        """Read"""
        self.cursor.execute('SELECT * FROM employees')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def update_data(self):
        """Update"""
        self.cursor.execute('''
        UPDATE employees SET age = 31 WHERE name = 'Ivan Ivanov'
        ''')
        self.connection.commit()

    def delete_data(self):
        """Delete"""
        self.cursor.execute('''
        DELETE FROM employees WHERE position = 'HR'
        ''')
        self.connection.commit()

if __name__=="__main__":
    db = SQLiteDB()

    db.insert_row(['Ivan', 23])
    db.insert_row(['Maria', 27])
    db.insert_row(['Pesho', 20])


