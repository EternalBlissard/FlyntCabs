from pandas import *
import mysql.connector
import random
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rootpassword",
  database="f1yntcabs"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS payments (payment_id INT PRIMARY KEY AUTO_INCREMENT,booking_id INT NOT NULL, payment_method VARCHAR(50) NOT NULL,FOREIGN KEY (booking_id) REFERENCES bookings (booking_id))")
PayMethod=["Credit Card", "Cash", "UPI", "PayTM"]
mycursor.execute("Select * from TripRecords")
i=0
for x in mycursor:
    i=i+1
for j in range(i):
    querydata=(j+1,j+1,PayMethod[(j%5)%4])
    query="insert into payments values(%s, %s, %s)"
    mycursor.execute(query,querydata)
    mydb.commit()
    #print(querydata)
    print("Inserted at ",j+1," row")
print("Payment Data Made")

