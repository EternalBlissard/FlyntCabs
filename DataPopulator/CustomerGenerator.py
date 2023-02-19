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
for i in range(1,length+1):
    l=len(Fname)
    j=random.randint(0,l-1)
    First_name=Fname.pop(j)
    Last_name=Lname.pop((j+10)%l)
    Gender_ = Gender.pop((j+15)%l)
    Phone_ = Phone.pop((j+20)%l)
    Email_ = Email.pop((j+25)%l)
    Address_ = Address.pop((j+30)%l)
    date_ = date.pop((j+50)%l)
    Age= random.randint(13,60)
    querydata=(i, First_name, Last_name, Gender_, Phone_, Email_, Address_,Age, date_)
    query="insert into Customer_Records values(%s, %s, %s, %s, %s, %s,%s,%s,%s)"
    mycursor.execute(query,querydata)
    mydb.commit()
    print("Inserted at ",i," row")
print("Done Data Make")    

    
