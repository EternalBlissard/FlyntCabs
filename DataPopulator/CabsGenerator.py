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
mycursor.execute("create table IF NOT EXISTS Customer_Records(Id int PRIMARY KEY, FName varchar(30) NOT NULL, LName varchar(30),Gender varchar(10), PrimaryPhone long, Email varchar(60), Address varchar (80), Age int NOT NULL, JoiningDate DATE)")
data = read_csv("customerdata.csv")
Fname = data['first_name'].tolist()
Lname = data['Last_name'].tolist()
Gender= data['Gender'].tolist()
Phone = data['PhoneNumber'].tolist()
Email = data['Email'].tolist()
Address= data['Address'].tolist()
date = data['date'].tolist()
length=len(Fname)
for i in range(length):
    First_name=Fname[i]
    Last_name=Lname[i]
    Gender_ = Gender[i]
    Phone_ = Phone[i]
    Email_ = Email[i]
    Address_ = Address[i]
    date_ = date[i]
    Age= 13 +(i%2)+(i%3)+(i%5)+(i%7)+(i%11)+(i%13)+(i%17)
    querydata=(i+1, First_name, Last_name, Gender_, Phone_, Email_, Address_,Age, date_)
    query="insert into Customer_Records values(%s, %s, %s, %s, %s, %s,%s,%s,%s)"
    mycursor.execute(query,querydata)
    mydb.commit()
    print("Inserted at ",i+1," row")
print("User Data Make")    

    
