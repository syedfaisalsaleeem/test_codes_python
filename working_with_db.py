import sqlite3
conn = sqlite3.connect('sqlite.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS faisal(id TEXT,Income INT)")
conn.commit()
c.close()

def alter_table():
# 	ALTER TABLE Customers
# ADD Email varchar(255);
	c = conn.cursor()
	# c.execute("Alter TABLE faisal ADD NAME INT ")
	c.execute("Alter TABLE faisal drop COLUMN ID ")
	conn.commit()
	c.close()

alter_table()
def f1():
	c = conn.cursor()
	c.execute("INSERT INTO faisal(Income) values(123)")
	conn.commit()
	c.close()

f1()
# def f2():
