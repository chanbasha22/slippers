# init_db.py
import sqlite3
import os

# Ensure the folder exists
os.makedirs("database", exist_ok=True)

# Connect to (or create) a valid SQLite DB
conn = sqlite3.connect("database/hello.db")
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    product TEXT NOT NULL,
    size INTEGER NOT NULL,
    address TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("✅ hello.db created successfully with bookings table.")
