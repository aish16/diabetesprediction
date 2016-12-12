import sqlite3
import cgi,cgitb
conn=sqlite3.connect('itt.db')
cur = conn.cursor()
cur.execute("SELECT * FROM project")
print(cur.fetchall())

