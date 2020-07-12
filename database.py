import sqlite3
connect=sqlite3.connect("library.db")

cursor=connect.cursor()

def createmember():

    cursor.execute(" CREATE TABLE IF NOT EXISTS members(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL ,Location TEXT  NOT NULL,status  TEXT DEFAULT 'Active') ")
    connect.commit()
def createbooktbl():
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL ,writer TEXT NOT NULL,quantity TEXT NULL,status TEXT DEFAULT 'Active')")
    connect.commit()

createmember()
createbooktbl()
connect.close()