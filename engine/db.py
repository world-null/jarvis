import csv
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

# query= "INSERT INTO web_command VALUES(null,'codebasics','https://codebasics.io/')"
# cursor.execute(query)
# conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# desired_columns_indices = [3, 19]

# Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts1.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
# conn.commit()
# conn.close()

query = 'Prasenjit  Riju'
query = query.strip().lower()

cursor.execute(
    "SELECT mobile_no FROM contacts WHERE name LIKE ? COLLATE NOCASE", 
    ('%' + query + '%',)
)
results = cursor.fetchall()

if results:
    cursor.execute(
        "DELETE FROM contacts WHERE name LIKE ? COLLATE NOCASE", 
        ('%' + query + '%',)
    )
    conn.commit()  # Make sure to commit the change
    print("Contact deleted successfully.")
else:
    print("No contact found to delete!")

# if results:
#     print(results[0][0])
# else:
#     print("No contact found!")
