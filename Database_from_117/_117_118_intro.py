import sqlite3


db = sqlite3.connect('app.db')
db.execute('CREATE TABLE IF NOT EXISTS skills (name TEXT,progress INTEGER,user_id INTEGER)')
db.close()
