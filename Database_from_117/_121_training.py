import sqlite3

def get_all_data():
    try:
        db = sqlite3.connect('app.db')
        print('Connected')
        cr = db.cursor()
        query = cr.execute('select * from users')
        results = query.fetchall()
        print(f"{len(results)} Rows")
        print('Showing Data')

        for row in results:
            print(f"UserId => {row[0]} UserName => {row[1]}")

    except sqlite3.Error as er:
        print('Error Reading Data {er}')

    finally:
        if(db) :
            db.close()
            print("Connection is closed")

get_all_data()
