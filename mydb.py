import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'root99',
	)
cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE relco")

print("done")

