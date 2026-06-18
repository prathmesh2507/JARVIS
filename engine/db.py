import sqlite3

conn = sqlite3.connect('jarvis.db')
cursor = conn.cursor()

#query = "CREATE TABLE IF NOT EXISTS sys_command (id INTEGER PRIMARY KEY, name varchar(100), path varchar(1000))"
#cursor.execute(query)

#query = "insert into sys_command values (null, 'vs code', 'C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')"
#cursor.execute(query)
#conn.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command (id INTEGER PRIMARY KEY, name varchar(100), url varchar(1000))"
#cursor.execute(query)

#query = "insert into web_command values (null, 'github', 'https://www.github.com/')"
#cursor.execute(query)
#conn.commit()


# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')