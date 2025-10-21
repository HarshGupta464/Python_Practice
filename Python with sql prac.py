import mysql.connector

#--------------------------------Connect mysql:-----------------------

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Mypass032@"
)

# ------------------ Creating database:-----------------------------
dbCursor=db.cursor()
# dbCursor.execute("Create database daMastersBooklist")
dbCursor.execute("use daMastersBooklist")

#---------------------Creating table------------------------
# dbCursor.execute("CREATE TABLE bookdetail(Rating INT(20), book VARCHAR(40), price DECIMAL(16,2))")
dbCursor.execute("SHOW TABLES")
for i in dbCursor:
    print(i)

#--------------------------Inserting values in table-------------------
# ins= "Insert into bookdetail (Rating, Book, Price) VALUES (%s,%s,%s)"
# val=[(4,"Power of Subconscious Mind", 99),
#      (3, "Attitude is Everything", 50),
#      (5, "Rich Dad Poor Dad", 149)]
# dbCursor.executemany(ins,val)
# db.commit()

#---------------------fetching data-------------------------------------
# dbCursor.execute("SELECT * FROM bookdetail ORDER BY PRICE")
# for i in dbCursor:
#     print(i)

dbCursor.execute("SELECT Book FROM bookdetail")
res= dbCursor.fetchall()
for i in res:
    print(i)

#----------------------Update and delete------------------------------

# dbCursor.execute("update bookdetail set Price=500 WHERE Rating > 4")
# db.commit()

# dbCursor.execute("DELETE FROM bookdetail WHERE Rating =3")
# db.commit()

dbCursor.execute("SELECT * FROM bookdetail")
for i in dbCursor:
    print(i)