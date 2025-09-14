import sqlite3

# Create in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create table with raw SQL
cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        grade REAL
    )
''')

# Insert data
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Alice', 20, 8.5)")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Bob', 19, 7.2)")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Noah', 20, 6.5)")


# Query data
cursor.execute("SELECT * FROM students WHERE age > 19")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()
