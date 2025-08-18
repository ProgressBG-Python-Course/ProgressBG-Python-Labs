import sqlite3


class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create users table if it doesn't exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """)
        self.conn.commit()

    def create_user(self, name, age):
        """Add a new user to the database."""
        self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    def create_users(self, users):
        """Add multiple users to the database."""
        self.cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)
        self.conn.commit()

    def get_user_by_name(self, name):
        """Retrieve a user by their name."""
        self.cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        return self.cursor.fetchone()

    def get_all_users(self):
        """Retrieve all users from the database."""
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def update_user(self, user_id, name, age):
        """Update a user's information in the database."""
        self.cursor.execute(
            "UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id)
        )
        self.conn.commit()

    def delete_user(self, user_id):
        """Delete a user from the database."""
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

    def __del__(self):
        """Close the database connection when the object is deleted."""
        self.conn.close()


if __name__ == "__main__":
    # Create db object to work with 'user_demo_1.db'
    db = DB("user_demo_1.db")

    # Create single user
    db.create_user("Ivan", 30)

    # # Create multiple users
    # users = [("Georgi", 25), ("Maria", 28), ("Petar", 35)]
    # db.create_users(users)

    # # Read all users
    # print(db.get_all_users())

    # # get single user id
    # user_id = db.get_user_by_name("Ivan")

    # # Update
    # db.update_user(1, "Ivan Petrov", 31)

    # # Delete user
    # db.delete_user(2)

    # print(db.get_all_users())
