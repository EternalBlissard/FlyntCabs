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
mycursor.execute("CREATE TABLE IF NOT EXISTS bookings (booking_id INT PRIMARY KEY AUTO_INCREMENT,user_id INT NOT NULL,cab_id INT NOT NULL,BookingTime DATETIME NOT NULL,fare DECIMAL(10, 2) NOT NULL,FOREIGN KEY (user_id) REFERENCES Customer_Records(Id),FOREIGN KEY (cab_id) REFERENCES cabs (cab_id));")
Baserate=[12,18,30,45]
data = read_csv("booker.csv")
DateTime = data['DateTime'].tolist()
length=len(DateTime)
for j in range(length):
    User=4+(j%2)+(j%5)+(j%11)+(j%17)+(j%23)+(j%37)
    Cab= 6+(j%3)+(j%7)+(j%13)+(j%19)+(j%47)
    Date_=DateTime[j]
    Fare =Baserate[(j%6)%4]*((j%12)+1)
    querydata=(j+1,User,Cab, Date_, Fare)
    query="insert into bookings values(%s, %s, %s, %s, %s)"
    mycursor.execute(query,querydata)
    mydb.commit()
    #print(querydata)
    print("Inserted at ",j+1," row")
print("Data Made")    
    
