import sqlite3

connection = sqlite3.connect('database.db')

with open('shema.sql') as f:
    connection.execute(f.read())

cursor = connection.cursor()

cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
('First post', 'Content to first post')
)


cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
('Second post', 'Content for the second post')
)

connection.commit()
connection.close()
