from database import get_db_connection
import sqlite3

def register_user(username, password, email):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, password, email)
        )
        conn.commit()
        conn.close()
        return {"status": "success", "message": "User registered successfully!"}
    except sqlite3.IntegrityError:
        return {"status": "error", "message": "Username or Email already exists."}

def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?", 
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return {"status": "success", "message": "Login successful!", "user_id": user["user_id"]}
    return {"status": "error", "message": "Invalid credentials."}
