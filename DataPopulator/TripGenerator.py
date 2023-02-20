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

mycursor.execute("CREATE TABLE IF NOT EXISTS TripRecords(trip_id INT PRIMARY KEY AUTO_INCREMENT, pick_up_location VARCHAR(255) NOT NULL,PickUpTime DATETIME NOT NULL,drop_off_location VARCHAR(255) NOT NULL,DropOffTime DATETIME NOT NULL,booking_id INT NOT NULL,dist INT NOT NULL,FOREIGN KEY (booking_id) REFERENCES bookings (booking_id))")

data = read_csv("Tripdata.csv")
Address=data['Address'].tolist()
PickUpTime=data['PickUpTime'].tolist()
DropOffTime=data['DropOffTime'].tolist()
length=len(Address)
for j in range(length):
    Addr=Address[j]
    PUT=PickUpTime[j]
    Addr2=Address[(j+1)%length]
    DOT=DropOffTime[j]
    Distance=(j%12)+1
    querydata=(j+1,Addr,PUT,Addr2,DOT,j+1,Distance)
    query="insert into TripRecords values(%s, %s, %s, %s, %s, %s,%s)"
    mycursor.execute(query,querydata)
    mydb.commit()
    #print(querydata)
    print("Inserted at ",j+1," row")
print("Trip Data Made")    
