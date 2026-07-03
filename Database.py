import sqlite3
import os

DB_NAME = "railway.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    """Reads railway.sql and initializes the database if it doesn't exist."""
    if not os.path.exists(DB_NAME):
        print("Initializing database...")
        conn = get_db_connection()
        with open("railway.sql", "r") as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    else:
        print("Database already exists.")

if __name__ == "__main__":
    initialize_database()
