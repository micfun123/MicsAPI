import sqlite3
#make sqlite3 database
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS QOTD_Questions(Question text, Aw1 text, Aw2 text, Aw3 text, Aw4 text, CorrectAW text, Category text)''')
c.execute('''CREATE TABLE IF NOT EXISTS Users(Email text, APIKey text, Uses int, UsesLimit int)''')
conn.commit()
conn.close()