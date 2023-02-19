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
mycursor.execute("CREATE TABLE IF NOT EXISTS cabs (cab_id INT PRIMARY KEY AUTO_INCREMENT,type VARCHAR(50) NOT NULL,model VARCHAR(50) NOT NULL,capacity INT NOT NULL,color VARCHAR(50) NOT NULL,license_plate VARCHAR(20) NOT NULL,make VARCHAR(50) NOT NULL,year INT NOT NULL,status VARCHAR(50) NOT NULL,BaseRate INT NOT NULL);")

Type=["Mini","Sedan","SUV","Lux"]
Capacity=[3,4,6,2]
Baserate=[12,18,30,45]
Status=["online","active","offline"]
data = read_csv("Cabdata.csv")
Model = data['Model'].tolist()
Color = data['Color'].tolist()
License= data['License_plate'].tolist()
Make = data['Make'].tolist()
Year = data['Year'].tolist()
length = len(Model)
for i in range(length-1,0,-1):
    Model_=Model.pop(i)
    Color_=Color.pop(i)
    License_=License.pop(i)
    Make_=Make.pop(i)
    Year_ = Year.pop(i)
    querydata=(length-i+1,Type[i%4],Model_, Capacity[i%4], Color_, License_, Make_,Year_,Status[(i%5)%3],Baserate[i%4])
    query="insert into cabs values(%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
    mycursor.execute(query,querydata)
    mydb.commit()
    #print(querydata)
    print("Inserted at ",length-i+1," row")
print("Data Made")    
