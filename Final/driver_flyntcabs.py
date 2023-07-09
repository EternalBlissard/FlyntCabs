import mysql.connector
mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="f1yntcabs"
)
cursor = mydb.cursor()
def view_profile(driver_id):
    cursor.execute("SELECT * FROM drivers WHERE driver_id = "+str(driver_id))
    result = cursor.fetchall()
    if(len(result)==0):
        print("No such driver exists")
        return
    print("Driver id: ", result[0][0])
    print("Name: ", result[0][1])
    print("Phone number: ", result[0][2])
    print("Email: ", result[0][3])
    print("Password: ", result[0][4])
    print("License number: ", result[0][5])
    print("Address: ", result[0][6])
    print("Years of experience: ", result[0][7])
    print("Cab id: ", result[0][8])
    print("Rating: ", result[0][9])
def update_profile(driver_id):
    cursor.execute("SELECT * FROM drivers WHERE driver_id = "+ str(driver_id,))
    result = cursor.fetchall()
    if(len(result)==0):
        print("No such driver exists")
        return
    print("Enter new details")
    name = input("Enter driver name: ")
    phone_number = input("Enter driver phone: ")
    email = input("Enter driver email: ")
    password = input("Enter driver password: ")
    license_number = input("Enter driver license number: ")
    address = input("Enter driver address: ")
    years_of_experience = int(input("Enter driver years of experience: "))
    cursor.execute("UPDATE drivers SET name = '" + name + "', phone_number = '"+ phone_number + "', email = '"+ email +"', password = '"+password+"', license_number = '"+license_number+"', address = '"+address+"', years_of_experience = "+str(years_of_experience)+" WHERE driver_id = "+str(driver_id))
    mydb.commit()
    print("Profile updated successfully")
def view_cab_details(driver_id):
    cursor.execute("SELECT * FROM drivers WHERE driver_id = "+(driver_id))
    result = cursor.fetchall()
    if(len(result)==0):
        print("No such driver exists")
        return
    cab_id = result[0][8]
    cursor.execute("SELECT * FROM cabs WHERE cab_id = "+str(cab_id))
    result = cursor.fetchall()
    if(len(result)==0):
        print("No such cab exists")
        return
    print("Cab id: ", result[0][0])
    print("Type: ", result[0][1])
    print("Model: ", result[0][2])
    print("Capacity: ", result[0][3])
    print("Color: ", result[0][4])
    print("License plate: ", result[0][5])
    print("Make: ", result[0][6])
    print("Year: ", result[0][7])
    print("Status: ", result[0][8])
    print("Base rate: ", result[0][9])
def update_cab_details(driver_id):
    cursor.execute("SELECT * FROM drivers WHERE driver_id = "+ str(driver_id))
    result = cursor.fetchall()
    if(len(result)==0):
        print("No such driver exists")
        return
    cab_id = result[8]
    cursor.execute("SELECT * FROM cabs WHERE cab_id = "+str(cab_id))
    result = cursor.fetchall()
    if(len(result)==0):
        print("No such cab exists")
        return
    print("Enter new details")
    cab_type = input("Enter cab type: ")
    model = input("Enter cab model: ")
    capacity = int(input("Enter cab capacity: "))
    color = input("Enter cab color: ")
    license_plate = input("Enter cab license plate: ")
    make = input("Enter cab make: ")
    year = int(input("Enter cab year: "))
    status = 'Active'
    base_rate = int(input("Enter cab base rate: "))
    cursor.execute("UPDATE cabs SET type = '"+cab_type+"', model = '"+model+"', capacity = "+capacity+", color = '"+color+"', license_plate = '"+license_plate+"', make = '"+make+"', year = "+year+", status = '"+status+"', BaseRate = "+base_rate+" WHERE cab_id = "+str(cab_id))
    mydb.commit()
    print("Cab details updated successfully")
def get_cab_earnings(cab_id):
    cursor = mydb.cursor()
    query = "SELECT SUM(fare) AS total_earnings FROM bookings INNER JOIN cabs ON bookings.cab_id = cabs.cab_id WHERE bookings.cab_id = "+str(cab_id)
    cursor.execute(query)
    earning = cursor.fetchone()
    earnings=earning[0]
    if(earnings==None):
        earnings=0
    return earnings

def view_earnings(driver_id):
    cursor.execute("SELECT * FROM drivers WHERE driver_id = "+str(driver_id))
    result = cursor.fetchall()
    if(len(result)==0):
        print("No such driver exists")
        return
    cab_id = result[0][8]
    earnings = get_cab_earnings(cab_id)
    print("Total earnings: ", earnings)
def view_trips(driver_id):
    cursor = mydb.cursor()
    query = "SELECT * FROM TripRecords INNER JOIN bookings ON TripRecords.booking_id = bookings.booking_id WHERE bookings.cab_id IN (SELECT cab_id FROM drivers WHERE driver_id = "+str(driver_id) +")"
    cursor.execute(query)
    trips = cursor.fetchall()
    if(len(trips)==0):
        print("No trips made yet")
        return
    print("Trips made by driver: ")
    for trip in trips:
        print("Trip id: ", trip[0])
        print("Booking id: ", trip[5])
        print("Pickup Location: ", trip[1])
        print("Pickup Time:" ,trip[2])
        print("Drop Location: ", trip[3])
        print("Drop Time: ", trip[4])
        print("Distance: ", trip[6])
def delete_account(driver_id):
    choice=int(input("Are you sure you want to delete your account? (1 for Yes, 0 for No): "))
    if(choice==1):
        cursor.execute("DELETE FROM drivers WHERE driver_id = "+str(driver_id))
        mydb.commit()
        print("Account deleted successfully")
        return False
    else:
        print("Account not deleted")
        return True

def login():
    print("Enter your login details")
    driver_id = input("Enter your unique driver id: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT * FROM drivers WHERE driver_id = "+str(driver_id)+" AND password = '"+ password+"'")
    result = cursor.fetchall()
    if(len(result) == 0):
        print("Invalid driver id or password")
    else:
        print("Login successful")
        ok=True
        while(ok):
            print("Enter your choice from menu:")
            print("1. View profile")
            print("2. Update profile")
            print("3. View cab details")
            print("4. Update cab details")
            print("5. View earnings")
            print("6. View trips")
            print("7. Delete account")
            print("8. Logout")
            choice = int(input("Enter your choice: "))
            if(choice == 1):
                view_profile(driver_id)
            elif(choice == 2):
                update_profile(driver_id)
            elif(choice == 3):
                view_cab_details(driver_id)
            elif(choice == 4):
                update_cab_details(driver_id)
            elif(choice == 5):
                view_earnings(driver_id)
            elif(choice == 6):
                view_trips(driver_id)
            elif(choice == 7):
                ok=delete_account(driver_id)
            else:
                ok=False    

def add_cab():
    cab_type = input("Enter cab type: ")
    model = input("Enter cab model: ")
    capacity = int(input("Enter cab capacity: "))
    color = input("Enter cab color: ")
    license_plate = input("Enter cab license plate: ")
    make = input("Enter cab make: ")
    year = int(input("Enter cab year: "))
    status = 'Active'
    base_rate = int(input("Enter cab base rate: "))
    cursor.execute("INSERT INTO cabs (type, model, capacity, color, license_plate, make, year, status, BaseRate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (cab_type, model, capacity, color, license_plate, make, year, status, base_rate))
    mydb.commit()
    cab_id = cursor.lastrowid
    print("Cab added successfully with cab_id: ", cab_id)
    return cab_id
def add_driver():
    cab_id=add_cab()
    print("Enter driver details")
    name = input("Enter driver name: ")
    phone_number = input("Enter driver phone: ")
    email = input("Enter driver email: ")
    password = input("Enter driver password: ")
    license_number = input("Enter driver license number: ")
    address = input("Enter driver address: ")
    years_of_experience = int(input("Enter driver years of experience: "))
    cursor.execute("INSERT INTO drivers (name, phone_number, email, password, license_number, address, years_of_experience, cab_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (name, phone_number, email, password, license_number, address, years_of_experience, cab_id))
    mydb.commit()   
    print("Driver added successfully. Your driver id is: ", cursor.lastrowid)

def open():
    print("Welcome to FLYNTCABS")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if(choice == 1):
            login()
        elif(choice == 2):
            add_driver()
        else:
            return False
    except:
        print("Something went wrong. Please try again")
    return True
while(open()):
    pass
print("Thank you for using FLYNTCABS") 
