import mysql.connector
def user_input(id):
    print("Please select an option from the menu below")
    print("1. View your previous bookings")
    print("2. View your profile")
    print("3. Update your profile")
    print("4. Delete your account")
    print("5. Provide feedback for your previous bookings")
    print("6. View your spendings each month for the past year")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="20203001",
        database="f1yntcabs"
    )
    mycursor = mydb.cursor()
    if choice == 1:
        mycursor.execute("SELECT * FROM Bookings WHERE user_id = "+str(id))
        bookings = mycursor.fetchall()
        if bookings:
            for booking in bookings:
                print("-------------------------")
                print("Booking ID:", booking[0])
                print("Cab ID:", booking[2])
                print("Booking Time:", booking[2])
                print("Amount Paid:", booking[3])
                print("-------------------------")
                mycursor.execute("Select * from triprecords where booking_id = "+str(booking[0]))
                trip = mycursor.fetchone()
                print("Pickup Location:", trip[1])
                print("Pickup Time:",trip[2])
                print("Drop off Location:", trip[3])
                print("Drop off Time:", trip[4])
                print("Distance Travelled:", trip[6])
            print("-------------------------")
        else:
            print("Oops! No previous bookings found.")
    elif choice == 2:
        mycursor.execute("SELECT * FROM Customer_Records WHERE Id= "+str(id))
        result = mycursor.fetchone()
        print("Customer ID:", result[0])
        print("First Name:", result[1])
        print("Last Name:", result[2])
        print("Gender:", result[3])
        print("Age:", result[7])
        print("Email:", result[5])
        print("Primary Phone:", result[4])
        print("Address:", result[6])
        print("Joined On:",result[8])
    elif choice == 3:
        print("Please select an option from the menu below")
        print("1. Update first name")
        print("2. Update last name")
        print("3. Update Gender")
        print("4. Update age")
        print("5. Update email")
        print("6. Update address")
        print("7. Update primary phone")
        print("8. return back")
        choicein = int(input("Enter your choice: "))
        if choicein == 1:
            new_fname = input("Enter new first name: ")
            mycursor.execute("UPDATE Customer_Records SET FName = '" +str(new_fname)+ "'  WHERE Id = "+ str(id))
            mydb.commit()
            print("Profile updated successfully.")
        elif choicein == 2:
            new_lname = input("Enter new last name: ")
            mycursor.execute("UPDATE Customer_Records SET LName = '"+str(new_lname) +"' WHERE Id = "+ str(id))
            mydb.commit()
            print("Profile updated successfully.")
        elif choicein == 3:
            new_gender = input("Enter new gender: ")
            mycursor.execute("UPDATE Customer_Records SET Gender = '"+ new_gender+ "' WHERE Id = " + str(id))
            mydb.commit()
            print("Profile updated successfully.")
        elif choicein == 4:
            new_age = input("Enter new age: ")
            mycursor.execute("UPDATE Customer_Records SET Age = "+ new_age+ " WHERE Id = " + str(id))
            mydb.commit()
            print("Profile updated successfully.")
        elif choicein == 5:
            new_email = input("Enter new email: ")
            mycursor.execute("UPDATE Customer_Records SET Email = '"+ new_email+ "' WHERE Id = " + str(id))
            mydb.commit()
            print("Profile updated successfully.")
        elif choicein == 6:
            new_address = input("Enter new address: ")
            mycursor.execute("UPDATE Customer_Records SET Address = '"+  new_address+ "' WHERE Id = "+ str(id))
            mydb.commit()
            print("Profile updated successfully.")
        elif choicein == 7:
            new_primary_phone = input("Enter new primary phone: ")
            mycursor.execute("UPDATE Customer_Records SET PrimaryPhone = "+ new_primary_phone+ " WHERE Id = "+ str(id))
            mydb.commit()
            print("Profile updated successfully.")
        else:
            print("Returning back...")
    elif choice == 4:
        try:
            a=int(input("Are you sure you want to delete your account? Press 1 to confirm or 0 to cancel: "))
            if a==1:
                mycursor.execute("DELETE FROM Customer_Records WHERE Id = "+str(id))
                mydb.commit()
                print("Account deleted successfully.")
                return False
            else:
                print("Returning back...")
        except:
            print("Invalid value entered")
    elif choice == 5:
        mycursor.execute("SELECT * FROM Bookings WHERE user_id = "+str(id))
        bookings = mycursor.fetchall()
        if bookings:
            print("Please select booking ID from the list below")
            for booking in bookings:
                print("-------------------------")
                print("Booking ID:", booking[0])
                print("Cab ID:", booking[2])
                print("Booking Time:", booking[2])
                print("Amount Paid:", booking[3])
                print("-------------------------")
                mycursor.execute("Select * from triprecords where booking_id = "+str(booking[0]))
                trip = mycursor.fetchone()
                print("Pickup Location:", trip[1])
                print("Pickup Time:",trip[2])
                print("Drop off Location:", trip[3])
                print("Drop off Time:", trip[4])
                print("Distance Travelled:", trip[6])
            print("-------------------------")
            try:
                booking_id = int(input("Enter booking ID: "))
                mycursor.execute("SELECT cab_id FROM bookings WHERE booking_iD = "+str(booking_id))
                cab = mycursor.fetchone()
                cab_id = cab[0]
                mycursor.execute("SELECT driver_id FROM drivers WHERE cab_id = "+str(cab_id))
                driver= mycursor.fetchone()
                mycursor.execute("SELECT COUNT(*) FROM bookings WHERE cab_id = "+str(cab_id))
                booking= mycursor.fetchone()
                num_of_booking=int(booking[0])
                driver_id = driver[0]
                rating=int(input("Enter rating (On scale of 0-5):"))
                if(rating>5 or rating<0):
                    print("Invalid rating")
                    return True
                mycursor.execute("SELECT rating FROM drivers WHERE driver_id = "+str(driver_id))
                getrating=mycursor.fetchone()
                gr=getrating[0]
                mycursor.execute("UPDATE drivers SET rating = "+str((gr+rating)/num_of_booking)+ " WHERE driver_id = "+str(driver_id))
                mydb.commit()
                print("Rating submitted successfully.")
            except: 
                print("Something went wrong. Please try again.")
                return True
        else:
            print("Oops! No previous bookings found.")
    elif choice == 6:
        sql = "SELECT user_id, \
                DATE_FORMAT(BookingTime, '%Y-%m') AS month, \
                SUM(fare) AS total_spending  \
                FROM  \
                bookings  \
                WHERE  \
                BookingTime >= DATE_SUB(NOW(), INTERVAL 1 YEAR) \
                AND user_id = "+str(id) +" \
                GROUP BY \
                user_id, \
                month \
                ORDER BY \
                month DESC;"
        mycursor.execute(sql)
        results = mycursor.fetchall()
        total = 0.0
        for row in results:
            print("Month: %s, Total Spending: %s" %(row[1], row[2]))
            total+=float(row[2])
            print("Total spending for the last year: %s" % total)
    else:
        return False
    return True
def main():
    print("Welcome to Flynt Cabs User Interface")
    print("Please select an option from the menu below")
    print("1. Login Into Existing Account")
    print("2. Create New Account")  
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="20203001",
        database="f1yntcabs"
        )
        mycursor = mydb.cursor()
        try:
            id = int(input("User please enter your customer ID: "))
        except:
            print("Invalid ID")
            return True
        mycursor.execute("SELECT * FROM Customer_Records WHERE Id = "+str(id))
        result = mycursor.fetchone()
        if result:
            print("Please enter your password(Password is your primary phone number)")
            password = input("Enter password: ")
            print(result[4])
            if str(password) == str(result[4]):
                print("Login successful!")
                print("Welcome "+result[2]+" "+result[3])
                while(user_input(str(id))):
                    pass
        
                           

    elif choice == 2:
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="20203001",
        database="f1yntcabs"
        )
        mycursor = mydb.cursor()
        try:
            id = int(input("Enter customer ID: "))
        except:
            print("Invalid ID")
            return True
        mycursor.execute("SELECT * FROM Customer_Records WHERE Id = "+str(id))
        result = mycursor.fetchone()
        if result:
            print("ID in use!! Please enter different ID")
            return True
        email = input("Enter email: ")
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        gender = input("Enter gender: ")
        primary_phone = input("Enter primary phone: ")
        address = input("Enter address: ")
        age = input("Enter age: ")
        joining_date = input("Enter joining date (YYYY-MM-DD): ")
        mycursor.execute("INSERT INTO Customer_Records (Id, Email, FName, LName, Gender, PrimaryPhone, Address, Age, JoiningDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, email, f_name, l_name, gender, primary_phone, address, age, joining_date))
        mydb.commit()
        print("Registration successful!")
    else:
        return False
    return True

while main():
    pass
print("Thank you for using Flynt Cabs")