# Deontae M Cocroft Connecting to Postgresql Database With Python 16 February 2023
import psycopg2
import sys, os

hostname = 'localhost'
database = 'TechStore'
username = 'postgres'
pwd = 'Char8305@'
port_id = 5432
admincounter = int
admincounter = 0

def ciview():
    connection = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    
    cur = connection.cursor()
    
    print("\n| CUSTOMER INFORMATION VIEW |")
    print("\nCustomerID | FirstName | LastName | Address | PostalCode | City | State | Country | Email | PhoneNumber\n")
    
    cur.execute('Select * FROM CUSTOMERS')
    
    for record in cur.fetchall():
        print(record)
    
    cur.close()
    connection.close()

    if admincounter == 1:
        adminmenu()
    if admincounter == 0:
        menu()


def psiview():
    connection = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )

    cur = connection.cursor()

    print("\n| PRODUCTS AND SUPPLIER INFORMATION VIEW |")
    print("\nProductID | SupplierID | CategoryID | ContactID | CompanyName | CategoryName | Description | ProductName | MSRP | Color | Style | Manufacturer | QuantityOnHand | Description\n")

    cur.execute('SELECT PRODUCTS.ProductID, PRODUCTS.SupplierID, PRODUCTS.CategoryID, SUPPLIERS.ContactID, SUPPLIERS.CompanyName, CATEGORY.CategoryName, CATEGORY.Description\
                , PRODUCTS.ProductName, PRODUCTS.MSRP, PRODUCTS.Color, PRODUCTS.Style, PRODUCTS.Manufacturer, PRODUCTS.QuantityOnHand, PRODUCTS.UnitsOrdered, PRODUCTS.Description\
                FROM PRODUCTS\
                INNER JOIN SUPPLIERS ON PRODUCTS.SupplierID = SUPPLIERS.SupplierID\
                INNER JOIN CATEGORY ON PRODUCTS.CategoryID = CATEGORY.CategoryID;')
    
    for record in cur.fetchall():
        print(record)

    cur.close()
    connection.close()

    if admincounter == 1:
        adminmenu()
    if admincounter == 0:
        menu()


def opciview():
    connection = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    
    cur = connection.cursor()
    
    print("\n| ORDERS WITH PRODUCT AND CUSTOMER INFORMATION VIEW |")
    print("\nOrderID | OrderDate | ProductName | Style | Manufacturer | OrderInfoID | ProductID | Quantity | Price | SalesTax | Total | CustomerID | FirstName | LastName | Address | PostalCode | City | State | Country | Email | PhoneNumber\n")
    
    cur.execute('SELECT ORDERS.OrderID, ORDERS.OrderDate, PRODUCTS.ProductName, PRODUCTS.Style, PRODUCTS.Manufacturer, ORDER_INFO.*, CUSTOMERS.*\
                FROM ORDERS\
                INNER JOIN CUSTOMERS ON ORDERS.CustomerID = CUSTOMERS.CustomerID\
                INNER JOIN ORDER_INFO ON ORDERS.OrderInfoID = ORDER_INFO.OrderInfoID\
                INNER JOIN PRODUCTS ON ORDER_INFO.ProductID = PRODUCTS.ProductID;')
    
    for record in cur.fetchall():
        print(record)
        
    cur.close()
    connection.close()

    if admincounter == 1:
        adminmenu()
    if admincounter == 0:
        menu()
       

def addcustomer():
    connection = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
    )
     
    cur = connection.cursor()
     
    print("\n| NEW CUSTOMER FORM |\n \nNo blank values and please use numeric value for postal code and phone number!")
    fname = input("\nEnter First Name: ")
    lname = input("Enter Last Name: ")
    address = input ("Enter Address: ")
    postal = input("Enter Postal Code: ")
    city = input("Enter City: ")
    state = input ("Enter State: ")
    country = input("Enter Country: ")
    email = input("Enter Email: ")
    phone = input ("Enter Phone Number: ")
    
    try:
        cur.execute("INSERT INTO CUSTOMERS (FirstName, LastName, Address, PostalCode, City, State, Country, Email, PhoneNumber)\
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (fname, lname, address, postal, city, state, country, email, phone))
        print("\n| Customer successfully added! Now displaying Customer Information View. |")
        
        connection.commit()
        cur.close()
        connection.close()
        
        ciview()
        
    except: 
        print("\n| Customer NOT added returning to main menu! | \n| Please try again and enter valid numerical value for postal code and or phone number! |\n| Make sure no fields are left empty! |")
        cur.close()
        connection.close()
        if admincounter == 1:
            adminmenu()
        if admincounter == 0:
            menu()
        

def delcustomer():
    connection = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
    )

    cur = connection.cursor()
    
    print("\n| CUSTOMER INFORMATION VIEW |")
    print("\nCustomerID | FirstName | LastName | Address | PostalCode | City | State | Country | Email | PhoneNumber\n")
    
    cur.execute('Select * FROM CUSTOMERS')
    
    for record in cur.fetchall():
        print(record)
    
    print("\n| DELETE CUSTOMER FORM |")
    
    cusid = input("\nEnter the ID of the Customer you want to delete: ")
    
    delquery = "DELETE FROM CUSTOMERS\
                WHERE CustomerID = %s"
                
    value = (cusid,)
    
    try:
        cur.execute(delquery, value)
        print("\n| Customer successfully deleted or already deleted! Now displaying Customer Information View. |")
        
        connection.commit()
        cur.close()
        connection.close()
        
        ciview()
        
    except:
        print("\n| Customer NOT deleted, Please enter numerical value for ID. |")
        cur.close()
        connection.close()

        if admincounter == 1:
            adminmenu()
        if admincounter == 0:
            menu()    


def menu():
    print("\n| MAIN MENU |")
    print("\nOPTIONS: ")
    print("1 to view customers \n2 to view products and supplier information \n3 to view order with product and customer information \n4 to logout \n5 to exit")
    try:
        option = int(input('\nSelect an option: '))

        if option == 1:
                ciview()
        elif option == 2:
            psiview()   
        elif option == 3:
            opciview()           
        elif option == 4:
            login() 
        elif option == 5:
            exitprogram()
        else:
            print("\nPlease select correct option!")
            menu()

    except ValueError:
        print("\nPlease select correct option!")
        menu()


def adminmenu():
    global admincounter
    print("\n| Admin Mode |")
    print("| MAIN MENU  |")
    print("\nOPTIONS: ")
    print("1 to view customers \n2 to view products and supplier information \n3 to view order with product and customer information \n4 to add customer \n5 to delete customer \n6 to logout \n7 to exit")
    try:
        option = int(input("\nSelect an option: "))
                    
        if option == 1:
            ciview()
        elif option == 2:
            psiview()    
        elif option == 3:
            opciview()   
        elif option == 4:
            addcustomer()    
        elif option == 5:
            delcustomer()   
        elif option == 6:
            admincounter -= 1
            login()
        elif option == 7:
            exitprogram()
        else:
            print("\nPlease select correct option!")
            adminmenu()

    except ValueError:
        print("\nPlease select correct option!")
        adminmenu()


def login():
    global admincounter
    choice = input("\nType '1' login as an admin. \nType any other key to login normally. \n\nSelection: ")
    if choice == "1":
        print("\n| Admin Login |")
        useruname = input("\nType '0000' to go back \nEnter admin username to acess TechStore database: ")

        if useruname == "0000":
            login()

        while useruname != "admin":
            print("\nWrong username, please try again!")
            useruname = input("Enter admin username to acess TechStore database: ")
            if useruname == "0000":
                login()
        
        print("\nCorrect Username!")

        userpass = input('\nEnter admin password to access TechStore database:  ')
            

        while userpass != "hello":
            print ("\nWrong password, please try again!")
            userpass = input("Enter admin password to access TechStore database:  ")

        if userpass == "hello":
            print('\nACCESS GRANTED!')
            admincounter += 1
            adminmenu()

    else:
        useruname2 = input("\nType '0000' to go back \nEnter username to acess TechStore database: ")

        if useruname2 == "0000":
            login()

        while useruname2 != "dcocroft":
            print("\nWrong username, please try again!")
            useruname2 = input("Enter username to acess TechStore database: ")
            if useruname2 == "0000":
                login()

        print("\nCorrect Username!")

        userpass2 = input('\nEnter password to access TechStore database:  ')

        while userpass2 != "hi":
            print ("\nWrong password, please try again!")
            userpass2 = input("Enter password to access TechStore database:  ")
            

        if userpass2 == "hi":
            print('\nACCESS GRANTED!')
            menu()


def exitprogram():
        print("Goodbye, have a good day!")
        sys.stdout = open(os.devnull, 'w')
        exit()


def main():
    try:
        login()
    except RecursionError:
        pass
main()
