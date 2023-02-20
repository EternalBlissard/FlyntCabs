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
mycursor.execute("CREATE TABLE IF NOT EXISTS drivers (driver_id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255) NOT NULL,phone_number LONG NOT NULL,email VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL, license_number VARCHAR(50) NOT NULL, address VARCHAR(255) NOT NULL,years_of_experience INT NOT NULL,cab_id INT NOT NULL,rating DECIMAL(3, 2) DEFAULT 0.0,FOREIGN KEY (cab_id) REFERENCES cabs (cab_id))")

data = read_csv("Driver Data.csv")
Name = data['Name'].tolist()
Phone = data['Phone'].tolist()
Email= data['Email'].tolist()
Password = data['Password'].tolist()
License = data['License'].tolist()
Address = data['Address'].tolist()
Status=["online","active","offline"]
length = len(Name)
for i in range(length):
    Name_=Name[i]
    Phone_=Phone[i]
    Email_=Email[i]
    Password_=Password[i]
    License_=License[i]
    Address_=Address[i]
    Year_=1+((i%37)%7)
    querydata=(i+1,Name_,Phone_, Email_,Password_, License_, Address_,Year_,i+1,0)
    query="insert into drivers values(%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
    mycursor.execute(query,querydata)
    mydb.commit()
    print("Inserted in",i+1,"row")
print("Driver Data Made Done")    


