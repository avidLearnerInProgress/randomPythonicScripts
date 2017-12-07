import sqlite3
conn=sqlite3.connect('a.db')
c=conn.cursor()
c.execute('''
	CREATE TABLE IF NOT EXISTS student(id REAL, name TEXT)
	''')

c.execute(''' 
	INSERT INTO student VALUES(1,'A')
	''')

conn.commit()
c.close()
conn.close()
