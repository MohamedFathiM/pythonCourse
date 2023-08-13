import sqlite3


users = [
    'Ahmed',
    'Mohamed',
    'Ali',
    'Soaad',
    'Hanya',
    'Aziza'
]

db = sqlite3.connect('app.db')
cr = db.cursor()
cr.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)')
cr.execute('CREATE TABLE IF NOT EXISTS skills (id INTEGER,name TEXT,user_id INTEGER)')

# insert
# for index,user in enumerate(users,1):
#     cr.execute(f'INSERT INTO users (id,name) VALUES ({index},"{user}")')

# Fetch
cr.execute('SELECT * from users')
# print(cr.fetchone())
# print(cr.fetchmany(2))
print(cr.fetchall())

db.commit()
db.close
