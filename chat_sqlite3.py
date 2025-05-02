import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# Create table (fix 'a' to just 'CREATE TABLE')
table_info = """
CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""

cursor.execute(table_info)

# Insert records
cursor.execute('''INSERT INTO STUDENT VALUES('NJ', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Balram', 'Data Science', 'A', 70)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Akash', 'Data Science', 'A', 80)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Benjamin', 'MLOPS', 'A', 59)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Ahmad', 'Data Science', 'A', 67)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Junior', 'Devops', 'A', 87)''')

# Display records
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit and close
connection.commit()
connection.close()
