# TechStore Database Python Program
How it works!! The TechStoreProgram.py file is my python code which connects to my TechStore PostgreSQL database using psycopg2. I used Eclipse Python (imported psycopg2 into Eclipse Python) and a PostgreSQL Database to create this program. To start This program has a password that needs to be entered. If the password is entered incorrectly the user will be prompted "Wrong Password, please try again! and will have to enter the correct password. Once the user enters the correct password, they will be granted access and greeted with options to display specific queries of information from the database. Option “1” Displays the customers from the database. Option '2" Displays Product and supplier information from the database. Option “3” Displays Orders with customer, product, and order information from the database. Option “4” allows the user to add new customers to the CUSTOMER table. Option “5” allows users to delete customers from the CUSTOMER table. Option “6” Closes the program and gives the user a Goodbye message.

This program contains 8 functions:

1.) def key(): is a function that protects this application from unwanted users. This function takes user input as a password. This was done by using a user scanner aka “input” in python. If that password is not correct the user will be prompted to try again and will not gain access into the program unless the correct password is entered. This was done by creating a while loop. If the password is correct then the program will move to the ‘def options():’ function. This was done by using an if then statement.

2.) def options()   is a function that takes user input and allows them to select a specific option using a user scanner aka “input” in python. Option “1” calls def ciview():. Option “2” calls def psiview(): ”. Option “3” calls “def opciview():”. Option “4” calls def addcustomer():. Option “5” calls def delcustomer(): . Option “6” calls def exitprogram():.

This was done by using if and elif statements. If the user enters a value that does not equal one of these options, they will be prompted to enter the correct option and they will be prompted the options again. This was done by creating a while loop.

3.) def ciview(): This function is called by selecting Option “1”. This is a function that connects to the PostgreSQL database and displays customer information from that database. This is done by using psycopg2 to create a connection and creating a cursor to execute statements to communicate with the MySQL database. Then the cursor executes an SQL statement that pulls information from tables in the PostgreSQL database. After the cursor is executed, a record is created to fetch the data from the SQL statement and that record is printed to in the function. After the customer information is displayed the cursor and connection is closed and the options() function is called to display the options again.

4.) def psiview(): This function is called by selecting Option “2”. This is a function that connects to the PostgreSQL database and displays Products and supplier information from that database. This is done by using psycopg2 to create a connection and creating a cursor to execute statements to communicate with the MySQL database. Then the cursor executes an SQL statement that pulls information from tables in the PostgreSQL database. After the cursor is executed, a record is created to fetch the data from the SQL statement and that record is printed to in the function. After the Products and supplier information is displayed the cursor and connection is closed and the options() function is called to display the options again.

5.) def opciview(): This function is called by selecting Option “3”. This is a function that connects to the PostgreSQL database and displays customer information from that database. This is done by using psycopg2 to create a connection and creating a cursor to execute statements to communicate with the MySQL database. Then the cursor executes an SQL statement that pulls information from tables in the PostgreSQL database. After the cursor is executed, a record is created to fetch the data from the SQL statement and that record is printed to in the function. After the Products and supplier information is displayed the cursor and connection is closed and the options() function is called to display the Main Menu again.

6.) def addcustomer():  This function is called by selecting Option “4”. This is a function that connects to the PostgreSQL database and displays customer information as well as allowing users to add a customer to the Customer Table. This is done by taking user input for all the columns from the table, using psycopg2 to create a connection, and creating a cursor to execute statements to communicate with the PostgreSQL database. The cursor then executes an SQL statement which adds the users values into the CUSTOMERS table. After this the cursor and connection is closed and the ciview() function is called which shows customer information and sends the user back to the Main Menu.

If the user isn’t careful and enters an invalid phone number and or postal code the table will not be updated and an exception will be thrown sending the user back to the Main Menu and prompts the user that the customer was not added and to try again. This was done by using try and exceptions.

7.) def delcustomer():  This function is called by selecting Option “5”. This is a function that connects to the PostgreSQL database and displays customer information, deletes the customer depending on an ID the user provides, then displays updated customer information. This is done by taking user input for the ID column in the CUSTOMERS table, using psycopg2 to create a connection, and creating a cursor to execute statements to communicate with the PostgreSQL database. Two separate cursors then execute a SQL statement which displays customer information and a SQL statement that deletes customer information depending on the ID value entered.  After this the cursor and connection is closed and the ciview() function is called which shows customer information and sends the user back to the Main Menu. If an existing value is entered everything will still be successful

If a non-numerical value is entered for ID an exception will be thrown sending the user back to the Main Menu and prompts the user that the customer was not deleted and to try again. This was done by using try and exceptions.

8.) def exitprogram(): is a function that simply closes the program and prints a goodbye message. This function is called by selecting Option “4”.
