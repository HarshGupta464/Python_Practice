import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Mypass032@"
)

dbCursor=db.cursor()
# dbCursor.execute("Create database daMastersBooklist")

dbCursor.execute("Show databases")
for i in dbCursor:
    print(i)