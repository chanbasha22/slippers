import sqlite3
import os

# Make sure the database folder exists
os.makedirs("database", exist_ok=True)

# Connect to (or create) the database file
conn = sqlite3.connect("database/hello.db")
cursor = conn.cursor()

# Create the bookings table
cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    product TEXT,
    size TEXT,
    address TEXT
)
''')

conn.commit()
conn.close()
print("✅ Database created at: database/hello.db")
