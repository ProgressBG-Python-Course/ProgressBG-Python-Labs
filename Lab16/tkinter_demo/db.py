# --- Database Operations Class ---
import sqlite3


class DB:
    """Manages all database operations for user registration."""

    def __init__(self, db_name="registration.db"):
        self.db_name = db_name
        self._create_table()

    def _get_connection(self):
        """Establishes and returns a database connection."""
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        """Creates the users table if it doesn't exist."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        conn.commit()
        conn.close()

    def register_user(self, username, password, email):
        """Inserts a new user into the database. Returns True on success, False otherwise."""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                (username, password, email),
            )
            conn.commit()
            return True
        except sqlite3.Error:
            return False
        finally:
            conn.close()
