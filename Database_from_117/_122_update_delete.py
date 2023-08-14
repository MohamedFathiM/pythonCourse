import sqlite3

db = sqlite3.connect('app.db')

cr = db.cursor()

cr.execute('Update users set name = "Gamal" where user_id = 1')
cr.execute('delete from users where user_id = 1 and name = "Gamal" ')
users = cr.execute('select * from users').fetchall()
print(users)
db.commit()
db.close()
