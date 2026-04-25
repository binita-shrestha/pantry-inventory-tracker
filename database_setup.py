import sqlite3

connection = sqlite3.connect("database/pantry.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    date_received TEXT NOT NULL,
    expiration_date TEXT NOT NULL,
    minimum_stock INTEGER NOT NULL
)
""")

connection.commit()
connection.close()

print("Database and inventory table created successfully.")