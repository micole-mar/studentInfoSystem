import sqlite3

# Create a connection to the SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('student_info.db')
cursor = conn.cursor()

# Create the "students" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        student_last_name TEXT,
        student_id TEXT UNIQUE NOT NULL,
        student_email TEXT,
        student_number TEXT,
        parent_name TEXT,
        parent_last_name TEXT,
        parent_email TEXT,
        parent_phone TEXT,
        year_level TEXT,
        subjects TEXT
    )
''')

# Commit the changes and close the database connection
conn.commit()
conn.close()
