import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('employee.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Creating table
table = """ CREATE TABLE employee (
            Employee_id INT(255) NOT NULL,
			Name CHAR(25) NOT NULL,
			Email VARCHAR(255) NOT NULL,
			Mobile INT(25) NOT NULL,
			Job_title CHAR(25) NOT NULL,
            Experience VARCHAR(200) NOT NULL,
			Score INT
		); """

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()
