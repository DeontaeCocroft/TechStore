# Deontae M Cocroft Connecting to Postgresql Database With Python 5 December 2022
import psycopg2

hostname = 'localhost'
database = 'TechStore'
username = 'postgres'
pwd = 'Char8305@'
port_id = 5432


def ciview():
    connection = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    
    cur = connection.cursor()
    
    print('\n| CUSTOMER INFORMATION VIEW |')
    print('\nCustomerID | FirstName | LastName | Address | PostalCode | City | State | Country | Email | PhoneNumber\n')
    
    cur.execute('Select * FROM CUSTOMERS')
    
    for record in cur.fetchall():
        print(record)
    
    cur.close()
    connection.close()  
    
    options()
            
def psiview():
    connection = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )

    cur = connection.cursor()

    print('\n| PRODUCTS AND SUPPLIER INFORMATION VIEW |')
    print('\nProductID | SupplierID | CategoryID | ContactID | CompanyName | CategoryName | Description | ProductName | MSRP | Color | Style | Manufacturer | QuantityOnHand | Description\n')

    cur.execute('SELECT PRODUCTS.ProductID, PRODUCTS.SupplierID, PRODUCTS.CategoryID, SUPPLIERS.ContactID, SUPPLIERS.CompanyName, CATEGORY.CategoryName, CATEGORY.Description\
                , PRODUCTS.ProductName, PRODUCTS.MSRP, PRODUCTS.Color, PRODUCTS.Style, PRODUCTS.Manufacturer, PRODUCTS.QuantityOnHand, PRODUCTS.UnitsOrdered, PRODUCTS.Description\
                FROM PRODUCTS\
                INNER JOIN SUPPLIERS ON PRODUCTS.SupplierID = SUPPLIERS.SupplierID\
                INNER JOIN CATEGORY ON PRODUCTS.CategoryID = CATEGORY.CategoryID;')
    
    for record in cur.fetchall():
        print(record)

    cur.close()
    connection.close()
        
    options()

def opciview():
    connection = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    
    cur = connection.cursor()
    
    print('\n| ORDERS WITH PRODUCT AND CUSTOMER INFORMATION VIEW |')
    print('\nOrderID | OrderDate | ProductName | Style | Manufacturer | OrderInfoID | ProductID | Quantity | Price | SalesTax | Total | CustomerID | FirstName | LastName | Address | PostalCode | City | State | Country | Email | PhoneNumber\n')
    
    cur.execute('SELECT ORDERS.OrderID, ORDERS.OrderDate, PRODUCTS.ProductName, PRODUCTS.Style, PRODUCTS.Manufacturer, ORDER_INFO.*, CUSTOMERS.*\
                FROM ORDERS\
                INNER JOIN CUSTOMERS ON ORDERS.CustomerID = CUSTOMERS.CustomerID\
                INNER JOIN ORDER_INFO ON ORDERS.OrderInfoID = ORDER_INFO.OrderInfoID\
                INNER JOIN PRODUCTS ON ORDER_INFO.ProductID = PRODUCTS.ProductID;')
    
    for record in cur.fetchall():
        print(record)
        
    cur.close()
    connection.close()
    
    options()
       
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
        
        connection.commit();
        cur.close()
        connection.close()
        
        ciview()
        
    except: 
        print("\n| Customer NOT added returning to main menu! | \n| Please try again and enter valid numerical value for postal code and or phone number. |")
        
        cur.close()
        connection.close()
        
        options()

def delcustomer():
    connection = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
    )
     
    cur = connection.cursor()
    
    print('\n| CUSTOMER INFORMATION VIEW |')
    print('\nCustomerID | FirstName | LastName | Address | PostalCode | City | State | Country | Email | PhoneNumber\n')
    
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
        
        connection.commit();
        cur.close()
        connection.close()
        
        ciview()
        
    except:
        print("\n| Customer NOT deleted, Please enter numerical value for ID. |")
        cur.close()
        connection.close()
        
        options()
        
def exitprogram():
    try:
        print('\nGoodbye, have a great day!')
        quit()
    except:
        print()
        
def options():
    print('\n| MAIN MENU |')
    print('\nOPTIONS: ')
    print('1 to view customers \n2 to view products and supplier information \n3 to view order with product and customer information \n4 to add customer \n5 to delete customer \n6 to exit')
    
    option = input('\nSelect an option: ')
    
    while option < "1" or option > "6":
        print('\nPlease select correct option!\n \nOPTIONS:\n1 to view customers \n2 to view products and supplier information \n3 to view order with product and customer information \n4 to add customer \n5 to delete customer \n6 to exit')
        option = input('\nSelect an option: ')
            
    if option == "1":
        ciview() 
    elif option == "2":
        psiview()     
    elif option == "3":
        opciview()     
    elif option == "4":
        addcustomer()    
    elif option == "5":
        delcustomer()    
    elif option == "6":
        exitprogram()
        
def key():
    userpass = input('\nEnter password to access TechStore database:  ')

    while userpass != "hello":
        print ('\nWrong password, please try again!')
        userpass = input('\nEnter password to access TechStore database:  ')
        
    if userpass == "hello":
        print('\nACCESS GRANTED!')
        
def main():
    key()
    options()
main()
