# Deontae M Cocroft Connecting to Postgresql Database With Python 5 December 2022
import psycopg2
import sys

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
    
    print('\nCustomer Information View')
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

    print('\nProducts and supplier information view')
    print('\nProductID | SupplierID | CategoryID | ContactID | CompanyName | CategoryName | Descrition | ProductName | MSRP | Color | Style | Manufacturer | QuantityOnHand | Description\n')

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
    
    print('\nOrders with product and customer information view')
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


def exitprogram():
    print('\nGoodbye, have a great day!')
    sys.exit()

def key():
    userpass = input('Enter password to view database content: ')


    while userpass != "hello":
        print ('\nWrong Password, Please try again!')
        userpass = input('\nEnter password to view database content: ')

    if userpass == "hello":
        print('\nACCESS GRANTED!!!')
        

key()

def options():
    print('\nOPTIONS: ')
    print('\n1 to view customers \n2 to view products and supplier information \n3 to view order with product and customer information \n4 to exit')
    option = input('\nSelect an option: ')
    
        
    while option < '1' or option > '4':
        print('\nPlease select correct option! \n 1 to view customers \n 2 to view products and supplier information \n 3 to view order with product and customer information \n 4 to exit')
        option = input('Select an option: ')
    
    if option == '1':
        ciview()
    elif option == '2':
        psiview()
    elif option == '3':
        opciview()
    elif option == '4':
        exitprogram()
        
options()