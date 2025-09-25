import sqlite3

#connect to sql and get the permission
conn=sqlite3.connect('product_info.db')
cursor=conn.cursor()

#using permission to execute sql instruction
cursor.execute('SELECT * FROM product_info')

#grab execute result and save to python variable, print variable
records=cursor.fetchall()
print (records)