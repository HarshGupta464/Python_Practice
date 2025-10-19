import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Mypass032@"
)

dbCursor=db.cursor()
# dbCursor.execute("Create database daMastersBooklist")

dbCursor.execute("use daMastersBooklist")
# dbCursor.execute("CREATE TABLE bookdetail(Rating INT(20), book VARCHAR(40), price DECIMAL(16,2))")
dbCursor.execute("SHOW TABLES")
for i in dbCursor:
    print(i)


