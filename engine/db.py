import sqlite3


conn=sqlite3.connect("jarvis.db")

cursor=conn.cursor()
query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name varchar(100), path varchar(1000))"
cursor.execute(query)

# query= "INSERT INTO sys_command VALUES(null,'one note','C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# conn.commit()

query= "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name varchar(100), url varchar(1000))"
cursor.execute(query)

query= "INSERT INTO web_command VALUES(null,'codebasics','https://codebasics.io/')"
cursor.execute(query)
conn.commit()