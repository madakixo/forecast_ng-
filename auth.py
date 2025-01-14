import logging
from config import get_db_connection, hash_password, check_password

def authenticate_user(username, password):
    """Check if user credentials are correct using the database."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    
    if result and check_password(password, result[0]):
        return True
    return False

def register_user(username, password):
    """Register a new user with a hashed password in the database."""
    conn = get_db_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                  (username, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        conn.rollback()
        return False
    finally:
        conn.close()
