from pandas import *
import mysql.connector
    
def q1():
    print("You selected number of Cabs Booked by user/customer in input specified months")
    try:
        print("Please enter the duration in months")
        dur=int(input())
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="f1yntcabs"
        )
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT c.FName, c.LName, COUNT(*) AS total_bookings \
            FROM customer_records c \
            JOIN bookings b ON c.Id = b.user_id \
            WHERE b.bookingtime >= DATE_SUB(NOW(), INTERVAL "+str(dur)+ " MONTH) \
            GROUP BY c.Id \
            ORDER BY total_bookings DESC;")
        results = mycursor.fetchall()
        print("FName |"," LName |", " Total Bookings")
        
        for row in results:
            print(row[0]," | ",row[1]," | ",row[2])
    except:
        print("Please enter a valid input")
        return True

def q2():
    print("You selected Driver and Cab details for the driver who are currently driving")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=""
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT d.*, c. * \
    FROM drivers d \
    INNER JOIN cabs c ON d.cab_id = c.cab_id \
    WHERE d.status = 'active'; ")
    results = mycursor.fetchall()
    print("FName |"," LName |", " Total Bookings")   
    for row in results:
        print(row[0]," | ",row[1]," | ",row[2])
    #Not working


def q3():
    print("You selected Customer with 0 booking till date")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customer_records c WHERE c.Id NOT IN (SELECT user_id FROM bookings);")
    results = mycursor.fetchall()
    print("ID | FName | LName | Gender | Primary_Ph. | Email | Address | Age | Joining Date")
    for row in results:
        print(row[0]," | ",row[1]," | ",row[2]," | ",row[3]," | ",row[4]," | ",row[5]," | ",row[6]," | ",row[7]," | ",row[8])

def q4():
    print(" Number of Bookings by a single customer")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT c.*, COUNT(b.booking_id) AS total_bookings\
    FROM customer_records c\
    LEFT JOIN bookings b ON c.Id = b.user_id\
    GROUP BY c.Id;")
    results = mycursor.fetchall()
    print("ID | FName | LName | Gender | Primary_Ph. | Email | Address | Age | Joining Date | Total Bookings")
    for row in results:
        print(row[0]," | ",row[1]," | ",row[2]," | ",row[3]," | ",row[4]," | ",row[5]," | ",row[6]," | ",row[7]," | ",row[8]," | ",row[9])
    

def q5():
    print("Driver with no booking in the last 24 hours")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *\
    FROM cabs c\
    WHERE NOT EXISTS (\
    SELECT 1 FROM bookings b\
    WHERE b.cab_id = c.cab_id AND b.bookingtime >= DATE_SUB(NOW(),INTERVAL 24 HOUR));")
    results = mycursor.fetchall()
    print("Cab ID | Cab Type | Cab Model | Cab Year | Cab Color | Cab Number | Cab Status")
    for row in results:
        print(row[0]," | ",row[1]," | ",row[2]," | ",row[3]," | ",row[4]," | ",row[5]," | ",row[6])
def q6():
    print("Total revenue generated by the cab in an year")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    cursor = mydb.cursor()
    cab_id=int(input("Enter Cab Id"))
    query = "SELECT SUM(fare) AS total_earnings FROM bookings INNER JOIN cabs ON bookings.cab_id = cabs.cab_id WHERE bookings.cab_id = "+str(cab_id)
    cursor.execute(query)
    earning = cursor.fetchone()
    earnings=earning[0]
    if(earnings==None):
        earnings=0
    print("Total earning of Cab with Cab_ID="+str(cab_id) +"is "+str(earnings))

def q7():
    print("You selected Details with Fare higher than avg fare of all the cabs")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT u.FName, u.PrimaryPhone, b.bookingtime\
    FROM customer_records AS u\
    INNER JOIN Bookings AS b ON u.id = b.user_id\
    WHERE b.bookingtime <= date_add(NOW(), INTERVAL 1 DAY) AND b.fare > (\
    SELECT AVG(fare) FROM Bookings);\
    ")
    results = mycursor.fetchall()
    print("FName |"," PrimaryPhone |", " Booking Time")
    for row in results:
        print(row[0]," | ",row[1]," | ",row[2])

def q8():
    print("You selected Deletes cabs as well as drivers for car older than specified year")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    year=int(input("Enter year:"))
    mycursor.execute("DELETE C, d FROM Cabs AS C INNER JOIN drivers AS d WHERE\
    C.cab_id=d.driver_id & C.year<"+str(year))
    print("Cabs deleted successfully")

def q9():
    print("You selected Total number of trips each driver has completed in the past month")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT d.name, COUNT(t.trip_id) AS total_trips FROM drivers d JOIN bookings b ON d.cab_id = b.cab_id JOIN TripRecords t ON b.booking_id = t.booking_id  WHERE t.drop_off_location IS NOT NULL AND t.drop_off_location <> '' AND b.bookingtime >= DATE_SUB(NOW(), INTERVAL 1 MONTH) GROUP BY d.driver_id ORDER BY total_trips DESC;")
    results = mycursor.fetchall()
    if(len(results)==0):
        print("No active driver in last month")
        return
    print("Name |"," Total Trips")
    for row in results:
        print(row[0]," | ",row[1])
   

def q10():
    print("You selected Driver details for those haven't been active (have not got a ride ) for a week and updating those as non active")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SET SQL_SAFE_UPDATES=0; \
    DROP TABLE IF EXISTS temp_drivers; \
    CREATE TEMPORARY TABLE temp_drivers \
    SELECT DISTINCT d.driver_id \
    FROM drivers d \
    JOIN bookings b ON d.cab_id = b.cab_id \
    WHERE b.bookingtime >= DATE_SUB(NOW(), INTERVAL 7 DAY) \
    GROUP BY d.driver_id \
    HAVING COUNT(DISTINCT b.booking_id) >= 1; \
    UPDATE drivers \ SET status = 'non-active' \
    WHERE driver_id NOT IN ( \
    SELECT driver_id FROM temp_drivers \
    ); \
    DROP TABLE temp_drivers; \
    SET SQL_SAFE_UPDATES=1;")
    #Need to update this one according to result . 
    #status is not in drivers table, need to add that

def q11():
    print("")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()

def q12():
    print("")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()

def o1():
    print("You selected Identify the top 5 pick-up locations by number of trips, broken down by month and driver rating.")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute(" \
    SELECT pick_up_location, MONTHNAME(PickUpTime) AS month, ROUND(d.rating, 1) AS driver_rating, COUNT(*) AS num_trips \
    FROM TripRecords tr \
    JOIN bookings b ON tr.booking_id = b.booking_id \
    JOIN drivers d ON d.cab_id = b.cab_id \
    GROUP BY pick_up_location, month, driver_rating \
    HAVING pick_up_location IS NOT NULL AND driver_rating IS NOT NULL \
    ORDER BY num_trips DESC \
    LIMIT 5;\
    ")
    results = mycursor.fetchall()
    print("Pick Up Location |"," Month |", " Driver Rating |", " Number of Trips")
    for row in results:
        print(row[0]," | ",row[1]," | ",row[2]," | ",row[3])

def o2():
    print("You selected determine total number of trips taken from each placeDetermine total number of trips taken from each place")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT pick_up_location, COUNT(trip_id) AS total_trips \
        FROM TripRecords \
        WHERE YEAR(PickUpTime) = 2023 \
        GROUP BY pick_up_location;"
    )
    results = mycursor.fetchall()
    print("Pick Up Location |"," Total Trips")
    for row in results:
        print(row[0]," | ",row[1])

def o3():
    print("You selected give list of top 3 customers who have longest trips for particular quarter of year")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT CONCAT(c.FName, ' ', c.LName) AS customer_name, SUM(tr.dist) AS total_distance  \
        FROM TripRecords tr  \
        JOIN bookings b ON tr.booking_id = b.booking_id \
        JOIN Customer_Records c ON b.user_id = c.Id \
        WHERE YEAR(DropOffTime) = 2023 AND QUARTER(DropOffTime) = 1\
        GROUP BY CONCAT(c.FName, ' ', c.LName) \
        ORDER BY total_distance DESC \
        LIMIT 3;"
    )
    results = mycursor.fetchall()
    print("Customer Name |"," Total Distance")
    for row in results:
        print(row[0]," | ",row[1])

def o4():
    print("You selected give average trip duration on each hour of day ")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT HOUR(PickUpTime) AS hour_of_day, AVG(TIMESTAMPDIFF(MINUTE, PickUpTime, DropOffTime)) AS avg_trip_duration \
    FROM TripRecords\
    WHERE YEAR(PickUpTime) = 2023 AND MONTH(PickUpTime) = 2\
    GROUP BY HOUR(PickUpTime)\
    ORDER BY hour_of_day asc;"
    )
    results = mycursor.fetchall()
    print("Hour of Day |"," Average Trip Duration")
    for row in results:
        print(row[0]," | ",row[1])

def o5():
    print("You selected number of trips made by each driver with each cab ")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT d.name, c.type, COUNT(tr.trip_id) AS num_trips \
        FROM drivers d \
        JOIN cabs c ON c.cab_id = d.cab_id \
        JOIN bookings b ON b.cab_id = c.cab_id \
        JOIN TripRecords tr ON tr.booking_id = b.booking_id \
        GROUP BY d.name, c.type WITH ROLLUP \
        HAVING GROUPING(d.name) = 0 AND GROUPING(c.type) = 0;"
    )
    results = mycursor.fetchall()
    print("Driver Name |"," Cab Type |", " Number of Trips")
    for row in results:
        print(row[0]," | ",row[1]," | ",row[2])

def o6():
    print("You selected for each combination of driver and cab type, showing the number of trips and revenue generated for that combination")
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=" ",
    database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT \
        d.name,\
        c.type,\
        COUNT(tr.trip_id) AS num_trips,\
        SUM(b.fare) AS revenue\
        FROM drivers d\
        JOIN cabs c ON c.cab_id = d.cab_id\
        JOIN bookings b ON b.cab_id = c.cab_id\
        LEFT JOIN TripRecords tr ON tr.booking_id = b.booking_id\
        GROUP BY d.name, c.type WITH ROLLUP\
        HAVING (GROUPING(d.name) = 0 OR GROUPING(c.type) = 0) AND (c.type IS NOT NULL AND d.name IS NOT NULL);"
    )
    results = mycursor.fetchall()
    print("Driver Name |"," Cab Type |", " Number of Trips |", " Revenue")
    for row in results:
        print(row[0]," | ",row[1]," | ",row[2]," | ",row[3])


def Normal():
    print("Please select your choice:")
    print("1. Number of Cabs Booked by user/customer in input specified months")
    print("2. Driver and Cab details for the driver who are currently driving")
    print("3. Customer with 0 booking till date")
    print("4. Number of Bookings by a single customer")
    print("5. Driver with no booking in the last 24 hours")
    print("6. Total revenue generated by the cab in an year")
    print("7. Details with Fare higher than avg fare of all the cabs")
    print("8. Deletes cabs as well as drivers for car older than 2008")
    print("9. Total number of trips each driver has completed in the past month")
    print("10. Driver details for those haven't been active (have not got a ride ) for a week and updating those as non active")
    print("11. ")
    print("12. ")
    print("13. Go back to previous menu")
    try:
        tt=int(input())
        if(tt==1):
            q1()
        elif(tt==2):
            q2()
        elif(tt==3):
            q3()
        elif(tt==4):
            q4()
        elif(tt==5):
            q5()
        elif(tt==6):
            q6()
        elif(tt==7):
            q7()
        elif(tt==8):
            q8()
        elif(tt==9):
            q9()
        elif(tt==10):
            q10()
        elif(tt==11):
            q11()
        elif(tt==12):
            q12()
        else:
            return False
    except:
        print("Please enter a valid choice")
    return True

def OLAP():
    print("Please select your choice:")
    print("1. Identify the top 5 pick-up locations by number of trips, broken down by month and driver rating.")
    print("2. Determine total number of trips taken from each place.")
    print("3. Give list of top 3 customers who have longest trips for particular quarter of year.")
    print("4. Give average trip duration on each hour of day.")
    print("5. Number of trips made by each driver with each cab.")
    print("6. For each combination of driver and cab type, showing the number of trips and revenue generated for that combination.")
    print("7. return back")
    try:
        tt=int(input())
        if(tt==1):
            o1()
        elif(tt==2):
            o2()
        elif(tt==3):
            o3()
        elif(tt==4):
            o4()
        elif(tt==5):
            o5()
        elif(tt==6):
            o6()
        else:
            return False
    except:
        print("Please enter a valid choice")
    return True

def OuterFunction():
    print("Hello! Welcome to FlyntCabs")
    print("Please select your choice:")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    try:
        t=int(input())
        if(t==1):
            print("You have selected Login")
            print("Please enter your username")
            username=input()
            print("Please enter your password")
            password=input()
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password=" ",
                database="f1yntcabs"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s", (username, password))
            result = mycursor.fetchone()
            if(result):
                print("You have successfully logged in")
                login=True
                while(login):
                    print("Please select your choice:")
                    print("1. Normal Queries")
                    print("2. OLAP Queries")
                    print("3. Logout")
                    try:
                        tt=int(input())
                        if(tt==1):
                            while(Normal()):
                                pass
                        elif(tt==2):
                            while(OLAP()):
                                pass
                        else:
                            login=False
                    except:
                        print("Please enter a valid choice")
            else:
                print("Invalid username or password")
        elif(t==2):
            print("You have selected Register")
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password=" ",
                database="f1yntcabs"
            )
            mycursor = mydb.cursor()

            print("Please enter your username")
            username=input()
            mycursor.execute("SELECT * FROM admin WHERE username = %s", (username,))
            result = mycursor.fetchone()
            if result:
                print("Username already exists")
                return True
            else:
                print("Please enter your password")
                password=input()
                print("Please enter your name")
                name=input()
                mycursor.execute(
                    "INSERT INTO admin (username, password, name) VALUES (%s, %s, %s)", (username, password, name))
                mydb.commit()
                print("You have successfully registered")
        else:
            return False
    except:
        print("Please enter a valid choice")
        return True
    return True
runApp =True
while(runApp):
    runApp=OuterFunction()
print("Thank you for using FlyntCabs")
