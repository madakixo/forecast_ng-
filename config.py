import os
import bcrypt
import sqlite3

GROQ_API_KEY = os.getenv('GROQ_API_KEY', 'your_api_key')
GROQ_API_URL = "https://api.groq.com/v1"
CSV_FILE_PATH = 'your_time_series_data.csv'
DATABASE_PATH = 'user_database.db'

def get_db_connection():
    """Return a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_PATH)

def hash_password(password):
    """Hash the password using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_password(password, hashed):
    """Check if the provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def init_db():
    """Initialize the database if it doesn't exist."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on module import
init_db()
